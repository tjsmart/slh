import shutil
import subprocess
import sys
from collections.abc import Iterator
from contextlib import contextmanager
from pathlib import Path
from setuptools import setup
from setuptools.command.bdist_wheel import bdist_wheel


THIS_DIR = Path(__file__).parent.resolve()

BUILD_DIR = THIS_DIR / "build"
RELEASE_BUILD_DIR = BUILD_DIR / "release"

SLH_DIR = THIS_DIR / "slh_c" / "slh"


def build() -> None:
    subprocess.run(
        [sys.executable, "run", "build", "--build", "release"],
        check=True,
    )


@contextmanager
def temp_include() -> Iterator[None]:
    dest = SLH_DIR / "include"
    if dest.exists():
        shutil.rmtree(dest)
    try:
        shutil.copytree(THIS_DIR / "include", dest)
        yield
    finally:
        shutil.rmtree(dest, ignore_errors=True)


@contextmanager
def temp_lib() -> Iterator[None]:
    dest = SLH_DIR / "lib"
    if dest.exists():
        shutil.rmtree(dest)
    dest.mkdir()
    try:
        for static_lib in RELEASE_BUILD_DIR.glob("*.a"):
            shutil.copyfile(static_lib, dest / static_lib.name)
        yield
    finally:
        shutil.rmtree(dest)


class IncludeExtraFiles(bdist_wheel):
    def run(self):
        build()

        with temp_lib(), temp_include():
            super().run()


setup(
    cmdclass={
        "bdist_wheel": IncludeExtraFiles,
    },
    package_data={"slh_c": [f"slh/**/*"]},
)
