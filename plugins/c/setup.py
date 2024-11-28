import shutil
import subprocess
import sys
from pathlib import Path
from setuptools import setup
from setuptools.command.build import build


THIS_DIR = Path(__file__).parent.resolve()
BUILD_DIR = THIS_DIR / "build"
# OUT_DIR = BUILD_DIR / "out"
OUT_DIR = THIS_DIR / "slh_c" / "out"
RELEASE_BUILD_DIR = BUILD_DIR / "release"


# Define a custom build class
class CustomBuild(build):
    def run(self):
        subprocess.run(["rm", "-rf", OUT_DIR], check=True)
        OUT_DIR.mkdir()

        subprocess.run(
            [sys.executable, "run", "build", "--build", "release"], check=True
        )
        shutil.copytree(THIS_DIR / "include", OUT_DIR / "include")

        LIB_DIR = OUT_DIR / "lib"
        LIB_DIR.mkdir()
        for static_lib in RELEASE_BUILD_DIR.glob("*.a"):
            shutil.copyfile(static_lib, LIB_DIR / static_lib.name)

        super().run()


setup(
    cmdclass={"build": CustomBuild},  # Register the custom build command
    package_data={"slh_c": [f"{OUT_DIR.name}/**/*"]},
)
