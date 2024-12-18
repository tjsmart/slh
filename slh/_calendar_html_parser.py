import re
from collections import defaultdict
from html.parser import HTMLParser

from ._random_shit import logger


__all__ = [
    "parse_calendar_stars_html_to_star_count",
]

_NoStarRegex = re.compile(r"^Day (\d\d?)$")
_OneStarRegex = re.compile(r"^Day (\d\d?), one star$")
_TwoStarRegex = re.compile(r"^Day (\d\d?), two stars$")


def parse_calendar_stars_html_to_star_count(html: str) -> list[int]:
    parser = _CalendarStarsHTMLParser()
    parser.feed(html)
    return parser.get_result()


class _CalendarStarsHTMLParser(HTMLParser):
    def __init__(self) -> None:
        super().__init__()
        self._stars: defaultdict[int, int] = defaultdict(int)

    def handle_starttag(self, tag: str, attrs: list[tuple[str, str | None]]) -> None:
        attrdict = dict(attrs)

        if (
            tag != "a"
            or not (label := attrdict.get("aria-label"))
            or not label.startswith("Day")
        ):
            logger.debug(f"Ignoring tag: {tag=}, {attrs=}")
            return

        for regex, star_value in zip(
            (_NoStarRegex, _OneStarRegex, _TwoStarRegex), (0, 1, 2)
        ):
            if not (re_match := regex.match(label)):
                continue
            (day_number,) = re_match.groups()
            day_number = int(day_number)
            self._stars[day_number] = star_value

    def get_result(self) -> list[int]:
        return [self._stars[i] for i in range(1, 26)]
