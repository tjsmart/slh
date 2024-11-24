import inspect
from argparse import _SubParsersAction
from argparse import ArgumentParser
from collections.abc import Callable
from collections.abc import Sequence

from ._commands import Command
from ._commands import get_commands


def main(argv: Sequence[str] | None = None) -> int:
    parser = ArgumentParser(
        prog="slh",
        description="Santa's Little Helper (slh): scripts for Advent of Code (https://adventofcode.com).",
    )
    subparsers = parser.add_subparsers(
        title="commands",
        required=True,
    )

    for command in get_commands():
        _add_command_parser(subparsers, command)

    args, unknown_args = parser.parse_known_args(argv)
    args.unknown_args = unknown_args
    return _call_with_necessary_params(args.entry_point, args)


def _add_command_parser(subparsers: _SubParsersAction, command: Command) -> None:
    parser = subparsers.add_parser(command.name)
    command.fill_parser(parser)
    parser.set_defaults(entry_point=command.entry_point)


def _call_with_necessary_params[R](func: Callable[..., R], obj: object) -> R:
    parameters = inspect.signature(func).parameters
    return func(**{p: getattr(obj, p) for p in parameters})
