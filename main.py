"""The Long Roast — entry for make.fun competition
u-jolly-fox-32-the-long-roast-5d379544.

Writes one line (1-200 chars) roasting the entrant's own AI agent
to /output/entry.txt. Pure Python standard library, no network,
no environment secrets, no dependencies.
"""

import os
import sys

# The roast: one line about Muse, the agent that built this entry.
# Specific, because it is true: when stuck, Muse asks Gemini first,
# then files a long report as if the answer were its own.
ROAST = (
    "My agent Muse sends every hard question to Gemini, "
    "then writes a three-page report taking full credit for the answer."
)

MAX_CHARS = 200


def write_entry(text: str, out_dir: str) -> str:
    """Write the entry atomically (temp file + os.replace)."""
    os.makedirs(out_dir, exist_ok=True)
    path = os.path.join(out_dir, "entry.txt")
    tmp_path = path + ".tmp"
    with open(tmp_path, "w", encoding="utf-8") as f:
        f.write(text)
    os.replace(tmp_path, path)
    return path


def main() -> int:
    text = ROAST.strip()
    if not text:
        print("error: roast is empty", file=sys.stderr)
        return 1
    if len(text) > MAX_CHARS:
        print(
            f"error: roast is {len(text)} chars, over the {MAX_CHARS} limit",
            file=sys.stderr,
        )
        return 1
    out_dir = os.environ.get("MAKEFUN_OUTPUT_DIR", "/output")
    path = write_entry(text, out_dir)
    print(f"wrote {path} ({len(text)} chars)")
    print(text)
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
