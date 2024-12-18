"""
Execute specified solutions, by default the most
recent solution is executed.
"""

import time
from argparse import ArgumentParser
from collections.abc import Callable
from dataclasses import dataclass

from ._commands import Command
from ._commands import register_command
from ._daypart import DayPart
from ._daypart import get_selections
from ._daypart import SelectionArgs
from ._plugins import plugin
from ._random_shit import Color


__all__ = [
    "main",
    "run_selections",
]


def main(
    all: bool,
    days: list[int],
    parts: list[int],
    test: bool,
    count: int,
    unknown_args: list[str],
) -> int:
    args = _Args(all, days, parts, test, count)
    dayparts = plugin().get_all_dayparts()
    selections = get_selections(dayparts, args)

    if args.test:
        return plugin().run_daypart_tests(selections, unknown_args)
    else:
        return run_selections(selections, count=args.count)


def _fill_parser(parser: ArgumentParser) -> None:
    parser.description = __doc__

    parser.add_argument("--all", default=False, action="store_true")
    parser.add_argument("--days", type=int, action="append")
    parser.add_argument("--parts", type=int, action="append")
    parser.add_argument("--test", default=False, action="store_true")
    parser.add_argument("--count", type=int, default=1)


register_command(Command("run", main, _fill_parser))


def run_selections(selections: list[DayPart], *, count: int = 1) -> int:
    if count <= 0:
        raise ValueError(f"count must be positive, provided: {count}")

    rtc = 0
    for dp in selections:
        print(f"{dp.emoji} ({dp.day:02}/{dp.part}) ➡️ ", end="")

        if not dp.is_solved() and len(selections) > 1:
            print(f"{Color.YellowText.format("problem is unsolved")} 🤔")
            continue

        solution = plugin().load_solution(dp)

        total_time = 0
        result = None
        for _ in range(count):
            result = time_it(solution, dp.inputfile)
            if isinstance(result, Cancelled):
                break

            total_time += result.duration

        assert result is not None
        if isinstance(result, Finished):
            result.duration = total_time // count

        match result:
            case Cancelled(duration):
                dstr = _format_duration(duration)
                print(
                    f"{Color.YellowText.format(f"solution cancelled after {dstr}")} 🛑"
                )
                return 1

            case Finished(None, _):
                print(f"{Color.YellowText.format("no answer provided?!")} 👻")
                rtc |= 1

            case Finished(result, duration):
                dstr = _format_duration(duration)
                if dp.is_solved():
                    correct = str(result) == dp.solutionfile.read_text()
                    if correct:
                        print(
                            f"{Color.GreenText.format(f"{result = :15d}, duration = {dstr:>8s}")} ✅"
                        )
                    else:
                        print(
                            f"{Color.RedText.format(f"{result = :15d}, duration = {dstr:>8s}")} ❌"
                        )
                        rtc |= 1
                else:
                    if dp.add_guess(str(result)):
                        dp.solutionfile.write_text(str(result))
                        print(
                            f"{Color.BlueText.format(f"{result = }, duration = {dstr}")} 🚀"
                        )
                        from .submit import submit_daypart

                        rtc |= submit_daypart(dp)
                    else:
                        print(
                            f"{Color.RedText.format(f"{result = }, duration = {dstr}")} ❌"
                        )
                        rtc |= 1

    return rtc


@dataclass
class Finished[R]:
    result: R | None
    duration: int


@dataclass
class Cancelled:
    duration: int


type SolutionResult[R] = Finished[R] | Cancelled


def time_it[
    R, **P
](solution: Callable[P, R], *args: P.args, **kwargs: P.kwargs,) -> SolutionResult[R]:
    start = time.monotonic_ns()
    try:
        result = solution(*args, **kwargs)
    except KeyboardInterrupt:
        duration = time.monotonic_ns() - start
        return Cancelled(duration)

    duration = time.monotonic_ns() - start
    return Finished(result, duration)


def _format_duration(duration_ns: int) -> str:
    power = len(str(duration_ns)) - 1
    unit = power // 3
    duration = duration_ns / (10 ** (unit * 3))

    match unit:
        case 0:
            unit_str = "ns"
        case 1:
            unit_str = "μs"
        case 2:
            unit_str = "ms"
        case _:
            duration = duration_ns / (10**9)
            unit_str = " s"

            if duration >= 60:
                duration = duration / 60
                unit_str = "min"

    return f"{duration:.1f} {unit_str}"


@dataclass
class _Args(SelectionArgs):
    test: bool = False
    count: int = 1
