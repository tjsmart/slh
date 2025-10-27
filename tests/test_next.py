from functools import partial
from unittest.mock import patch

import pytest

from slh import next
from slh._daypart import DayPart

patch_mut = partial(patch.object, next)


@pytest.fixture(autouse=True)
def mock_input():
    with patch_mut("_get_input") as mock:
        mock.return_value = "input\nyeah!"
        yield mock.return_value


@pytest.fixture(autouse=True)
def mock_prompt():
    with patch_mut("_get_prompt") as mock:
        mock.return_value = "# AOC prompt\nyeah!"
        yield mock.return_value


@pytest.fixture
def mock_plugin():
    with patch_mut("plugin") as mock:
        yield mock.return_value


@pytest.fixture(autouse=True)
def mock_open():
    with patch_mut("_open"):
        yield


@pytest.fixture(autouse=True)
def auto_rootdir(rootdir):
    pass


def test_next_can_create_first_thing(mock_plugin):
    mock_plugin.get_all_dayparts.return_value = []

    next._main()

    mock_plugin.generate_next_files.assert_called_once_with(1994, DayPart(1, 1), None)


@pytest.mark.parametrize(
    ("last_created", "expected_next"),
    [
        (DayPart(1, 1), DayPart(1, 2)),
        (DayPart(1, 2), DayPart(2, 1)),
        (DayPart(2, 1), DayPart(2, 2)),
    ],
)
def test_next_can_create_part1(last_created, expected_next, mock_plugin):
    mock_plugin.get_all_dayparts.return_value = [last_created]

    next._main()

    mock_plugin.generate_next_files.assert_called_once_with(
        1994, expected_next, last_created
    )
