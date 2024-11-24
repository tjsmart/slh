from collections.abc import Callable
from functools import lru_cache
from importlib.metadata import entry_points
from pathlib import Path
from typing import Protocol

from ._daypart import DayPart
from ._random_shit import HandledError
from ._user_config import user_config


_GROUP_NAME = "slh"

type Solution = Callable[[Path], int]


class Plugin(Protocol):
    LANGUAGE: str
    """
    Programming language used, e.g. "python", "c".
    """

    def get_all_dayparts(self) -> list[DayPart]:
        """
        Returns a sorted list of existing dayparts.
        """
        ...

    def get_src_file(self, dp: DayPart, /) -> Path:
        """
        Returns path to the main src file for the next daypart.
        """
        ...

    def generate_next_files(
        self, year: int, next: DayPart, prev: DayPart | None
    ) -> None:
        """
        Generate next files for the next daypart puzzle.
        """
        ...

    def run_daypart_tests(
        self, dayparts: list[DayPart], test_args: list[str] | None
    ) -> int:
        """
        Run any tests associated with the provided dayparts.
        """
        ...

    def load_solution(self, dp: DayPart) -> Solution:
        """
        Returns a solution callback for the provided daypart.
        """
        ...


@lru_cache(maxsize=1)
def plugin() -> Plugin:
    target_language = user_config().language.lower()
    plugins = _fetch_plugins()
    candidates = [
        plugin
        for plugin in plugins
        if plugin.LANGUAGE.lower() == target_language
    ]

    match len(candidates):
        case 0:
            available_languages = {p.LANGUAGE.lower() for p in plugins}
            raise HandledError(
                f"target language {target_language!r} is not in list of"
                f" available languages: {available_languages}"
            )
        case 1:
            return candidates[0]
        case _:
            candidate_locations = {
                candidate: getattr(candidate, "__file__", "unknown location")
                for candidate in candidates
            }
            raise HandledError(
                f"more than one plugin candidates for target language {target_language!r},"
                f" please uninstall undesired plugins: {candidate_locations!r}"
            )


def _fetch_plugins() -> list[Plugin]:
    return [ep.load() for ep in entry_points(group=_GROUP_NAME)]
