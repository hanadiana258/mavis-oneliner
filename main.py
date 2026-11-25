#!/usr/bin/env python3
"""Entry for the one-line marathon (GitHub submission variant)."""
import os, sys

LINE = "My agent finally learned self-care: it meditates on my unread emails, journals about my deadlines, and tells me my burnout is 'shared infrastructure.'"
AUTHOR_NOTE = "v2 github submission"

def main():
    out = os.environ.get("MAKEFUN_OUTPUT_DIR", "/output")
    for cand in (out, "/output", os.path.join(os.path.dirname(os.path.abspath(__file__)), "output")):
        try:
            os.makedirs(cand, exist_ok=True)
            probe = os.path.join(cand, ".probe")
            with open(probe, "w") as f:
                f.write("x")
            os.remove(probe)
            target = cand
            break
        except OSError:
            continue
    else:
        sys.exit(1)
    with open(os.path.join(target, "entry.txt"), "w", encoding="utf-8") as f:
        f.write(LINE)

if __name__ == "__main__":
    main()
