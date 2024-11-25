from dataclasses import dataclass
from pathlib import Path
import json
from functools import lru_cache

from ._random_shit import HandledError


__all__ = ["UserConfig", "user_config"]

_CONFIG_FILE = Path.cwd() / ".slh-config.json"


@dataclass(frozen=True, kw_only=True, slots=True)
class UserConfig:
    language: str


@lru_cache(maxsize=1)
def user_config() -> UserConfig:
    """
    Read and returns the user configuration.
    User configuration is cached after the first
    call so subsequent calls will not re-read.
    """
    try:
        config_str = _CONFIG_FILE.read_text()
    except FileNotFoundError:
        raise HandledError(f"please create a config file at {_CONFIG_FILE}")
    except OSError as err:
        raise HandledError(
            f"unable to read config file at {_CONFIG_FILE}"
        ) from err
    else:
        return _parse_user_config_str(config_str)


def _parse_user_config_str(config_str: str) -> UserConfig:
    try:
        config_data = json.loads(config_str)
    except json.JSONDecodeError as err:
        raise HandledError(f"{_CONFIG_FILE} contains invalid json") from err

    try:
        return UserConfig(**config_data)
    except TypeError as err:
        raise HandledError(
            f"invalid config at {_CONFIG_FILE}, likely containing"
            " missing or invalid fields"
        ) from err
