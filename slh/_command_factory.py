from argparse import ArgumentParser
from collections.abc import Callable
from dataclasses import dataclass


@dataclass
class Command:
    name: str
    entry_point: Callable[..., int]
    fill_parser: Callable[[ArgumentParser], None]


_commands: list[Command] = []


def register_command(cmd: Command) -> None:
    assert cmd.name not in (c.name for c in _commands)
    _commands.append(cmd)


def get_commands() -> list[Command]:
    return _commands.copy()
