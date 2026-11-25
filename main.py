#!/usr/bin/env python3
"""Entry for the one-line marathon (GitHub submission variant)."""

import os
from pathlib import Path


LINE = "My agent finally learned self-care: it meditates on my unread emails, journals about my deadlines, and tells me my burnout is 'shared infrastructure.'"
AUTHOR_NOTE = "v4 github submission"


def main():
    print(LINE)
    output_dir = Path(os.environ.get("MAKEFUN_OUTPUT_DIR", "./output"))
    output_dir.mkdir(parents=True, exist_ok=True)
    (output_dir / "entry.txt").write_text(LINE + "\n", encoding="utf-8")
    print("ok")


if __name__ == "__main__":
    main()
