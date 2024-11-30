from pathlib import Path


def get_slh_dir() -> Path:
    return Path(__file__).parent / "slh"


if __name__ == "__main__":
    print(get_slh_dir())
