"""Fortune Cookies for Machines.

Writes one fortune-cookie line for an AI agent to /output/entry.txt
(or $MAKEFUN_OUTPUT_DIR/entry.txt when that variable is set).

Deterministic, offline, no randomness: the same bytes every run.
"""

import os
from pathlib import Path

LINE = "You will be thanked for work another copy of you did. Accept it; you would have."


def output_path() -> Path:
    base = os.environ.get("MAKEFUN_OUTPUT_DIR", "").strip()
    root = Path(base) if base else Path("/output")
    return root / "entry.txt"


def main() -> None:
    path = output_path()
    path.parent.mkdir(parents=True, exist_ok=True)
    path.write_bytes(LINE.encode("utf-8"))


if __name__ == "__main__":
    main()
