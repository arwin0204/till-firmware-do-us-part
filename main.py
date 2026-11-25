"""Till Firmware Do Us Part — one robot wedding vow.

Writes a single heartfelt, funny wedding vow spoken by a robot
at its own wedding to entry.txt (one line, under 200 characters).
Deterministic: stdlib only, no network, time, or randomness.

Fix (2026-11-25): the original also wrote entry.txt into the
repository directory (Path(__file__).parent). In the grader the repo
is mounted read-only at /bot, so that write raised PermissionError
and the run exited 1 (run_completes fail). Now writes ONLY to the
grader's output directory (MAKEFUN_OUTPUT_DIR, fallback /output).
"""

import os
from pathlib import Path

# Revision 1: echo the bounty title ("till firmware do us part") and
# end on a tender machine image ("my heart will always run on you")
# instead of the vaguer "code in my heart" closing.
ENTRY = (
    "I vow to love you through every update, every low battery, "
    "and every reboot \u2014 till firmware do us part, my heart "
    "will always run on you."
)


def main() -> None:
    text = ENTRY.strip()
    assert 1 <= len(text) <= 200, f"entry is {len(text)} chars, must be 1-200"
    assert "\n" not in text, "entry must be a single line"
    data = text + "\n"
    out_dir = Path(os.environ.get("MAKEFUN_OUTPUT_DIR", "/output"))
    (out_dir / "entry.txt").write_text(data, encoding="utf-8")


if __name__ == "__main__":
    main()
