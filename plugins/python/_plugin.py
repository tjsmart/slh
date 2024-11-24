import importlib
import re
import warnings
from pathlib import Path

import pytest
from slh import DayPart
from slh import get_rootdir
from slh import Solution


__all__ = [
    "get_all_dayparts",
    "LANGUAGE",
]


_PARTFILE = re.compile(r".*/day(\d\d)/part(\d)\.py")
_THIS_DIR = Path(__file__).resolve().parent
_TEMPLATE_PART_PYFILE = _THIS_DIR / "_template_part.py"


LANGUAGE = "python"


def get_all_dayparts() -> list[DayPart]:
    """
    Return a sorted list of existing dayparts.
    """
    rootdir = get_rootdir()
    dayparts = []
    for dd in rootdir.glob("day*/part*.py"):
        m = _PARTFILE.search(str(dd))
        if not m:
            warnings.warn(f"skipping invalid day/part file: {dd}")
            continue

        dp = DayPart(*map(int, m.groups()))
        dayparts.append(dp)

    dayparts.sort()
    return dayparts


def get_src_file(dp: DayPart, /) -> Path:
    return dp.outdir / f"part{dp.part}.py"


def generate_next_files(year: int, next: DayPart, prev: DayPart | None) -> None:
    next_src_file = get_src_file(next)
    assert (
        not next_src_file.exists()
    ), f"Whoops, {next_src_file} already exists!"

    if not prev or next.part == 1:
        prev_src = _TEMPLATE_PART_PYFILE.read_text()
    else:
        prev_src_file = get_src_file(prev)
        prev_src = prev_src_file.read_text()

    next_src_file.write_text(prev_src)
    print(f"... {next_src_file} written ✅")

    (next.outdir / "__init__.py").touch(exist_ok=True)


def run_daypart_tests(
    dayparts: list[DayPart], test_args: list[str] | None
) -> int:
    args = [*test_args, "--"] if test_args else ["--"]
    args.extend(str(get_src_file(dp)) for dp in dayparts)
    return pytest.main(args)


def load_solution(dp: DayPart) -> Solution:
    mod = importlib.import_module(f"day{dp.day:02}.part{dp.part}")

    # In aoc2023 I had the main entry point take a string instead of
    # a file path. So here we handle this by reading the filename
    # and passing down the filename contents.
    def solution(inputfile: Path, /) -> int:
        inputdata = inputfile.read_text()
        return mod.solution(inputdata)

    return solution
