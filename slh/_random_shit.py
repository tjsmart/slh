from __future__ import annotations

import logging
import subprocess
import sys
from enum import Enum
from functools import lru_cache
from pathlib import Path

logger = logging.getLogger("slh")
THIS_DIR = Path(__file__).resolve().parent


class HandledError(RuntimeError): ...


@lru_cache(maxsize=1)
def get_rootdir() -> Path:
    result = subprocess.run(
        ["git", "rev-parse", "--show-toplevel"],
        check=True,
        capture_output=True,
        text=True,
    )
    return Path(result.stdout.strip())


def get_cookie_headers() -> dict[str, str]:
    session_file = get_rootdir() / ".session"
    return {"Cookie": f"session={session_file.read_text().strip()}"}


class Color(Enum):
    RedText = 31
    GreenText = 32
    YellowText = 33
    BlueText = 34

    RedBack = 41
    GreenBack = 42
    YellowBack = 43
    BlueBack = 44

    def format(self, text: str) -> str:
        if sys.stdout.isatty():
            return f"\033[{self.value}m{text}\033[0m"  # ]]
        else:
            return text
