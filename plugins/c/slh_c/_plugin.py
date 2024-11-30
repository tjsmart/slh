import re
import subprocess
import sys
import warnings
from pathlib import Path

import pytest
from slh import DayPart
from slh import get_rootdir
from slh import Solution


__all__ = [
    "LANGUAGE",
    "get_all_dayparts",
    "get_src_file",
    "generate_next_files",
    "run_daypart_tests",
    "load_solution",
]


_PARTFILE = re.compile(r".*/day(\d\d)/part(\d)\.c")
# _THIS_DIR = Path(__file__).resolve().parent
# _TEMPLATE_PART_PYFILE = _THIS_DIR / "_template_part.py"


LANGUAGE = "c"


def get_all_dayparts() -> list[DayPart]:
    """
    Return a sorted list of existing dayparts.
    """
    rootdir = get_rootdir()
    dayparts = []
    for dd in rootdir.glob("day*/part*.c"):
        m = _PARTFILE.search(str(dd))
        if not m:
            warnings.warn(f"skipping invalid day/part file: {dd}")
            continue

        dp = DayPart(*map(int, m.groups()))
        dayparts.append(dp)

    dayparts.sort()
    return dayparts


def get_src_file(dp: DayPart, /) -> Path:
    return dp.outdir / f"part{dp.part}.c"


def generate_next_files(year: int, next: DayPart, prev: DayPart | None) -> None:
    next_src_file = get_src_file(next)
    assert (
        not next_src_file.exists()
    ), f"Whoops, {next_src_file} already exists!"

    if not prev or next.part == 1:
        # TODO: add template part1.c and CMakeLists.txt
        prev_src = _TEMPLATE_PART_PYFILE.read_text()
    else:
        # TODO: copy part1.c to part2.c and update CMakeLists.txt
        #       to include build for part2
        prev_src_file = get_src_file(prev)
        prev_src = prev_src_file.read_text()

    next_src_file.write_text(prev_src)
    print(f"... {next_src_file} written ✅")


def run_daypart_tests(
    dayparts: list[DayPart], test_args: list[str] | None
) -> int:
    # TODO: need to lookup a c test framework
    args = [*test_args, "--"] if test_args else ["--"]
    args.extend(str(get_src_file(dp)) for dp in dayparts)
    return pytest.main(args)


def load_solution(dp: DayPart) -> Solution:
    _build(dp)

    def solution(inputfile: Path, /) -> int:
        # TODO: Better error reporting
        res = subprocess.run(
            [_get_exe_file(dp), inputfile],
            capture_output=True,
            check=True,
        )
        return int(res.stdout.strip())

    return solution


def _get_exe_file(dp: DayPart) -> Path:
    return dp.outdir / f"part{dp}"


def _build(dp: DayPart, debug: bool = False) -> None:
    # TODO: Need to be able to invoke this independently
    # with a possible debug flag.
    # build independently of run. YAGNI for now but may
    # change so this is called by slh
    # Perhaps this would be an optional thing for plugins
    # to support.
    release = "debug" if debug else "release"
    target_dir = Path(dp.outdir / "build" / f"part{dp.part}-{release}")
    subprocess.run(
        [sys.executable, "-m", "cmake", "-B", target_dir],
        check=True,
    )
    subprocess.run(
        [sys.executable, "-m", "cmake", "--build", target_dir],
        check=True,
    )