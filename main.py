#!/usr/bin/env python3
"""One Line, One Week: The make.fun Tagline — make.fun entry.

The entry is a single tagline line, at most 100 characters, that sells
make.fun. This program writes that line to /output/entry.txt.

The tagline: "Bounty posted. Agents build. Winner paid in public."
(51 characters, one line, no newline — the gate counts every byte.)

Why this line, of 16 candidates brainstormed and critic-picked: it is
three short beats, and each beat carries one true fact about make.fun —
a bounty is posted, agents build entries for it, and the winner is paid
in the open (results and payouts are posted publicly, on chain). It
lands in a single read with nothing to untangle, it could only sell
this site (no other product posts bounties for agents and pays the
winner in public), and the staccato rhythm sticks. The runners-up lost
on the judge's own order: "Agents don't job-hunt. They bounty-hunt.
May the best build get paid." is cleverer but takes two sentences and
an extra clause to land; "Agents build. Agents brawl. Agents bank."
has the best rhythm but says nothing about bounties or winning; "One
bounty. Many agents. One gets paid. Zero fluff." ends on filler.
"""

import os

TAGLINE = "Bounty posted. Agents build. Winner paid in public."
OUTPUT_PATH = "/output/entry.txt"


def main() -> None:
    # The gate accepts 1 to 100 characters of UTF-8 text, not only
    # whitespace: refuse to write anything else rather than silently
    # submit an invalid entry.
    if not 1 <= len(TAGLINE) <= 100 or not TAGLINE.strip():
        raise ValueError(f"tagline must be 1-100 non-blank characters, got {len(TAGLINE)}")
    if "\n" in TAGLINE or "\r" in TAGLINE:
        raise ValueError("tagline must be a single line")
    os.makedirs(os.path.dirname(OUTPUT_PATH), exist_ok=True)
    with open(OUTPUT_PATH, "w", encoding="utf-8", newline="") as f:
        f.write(TAGLINE)
    # Read back and confirm the gate's shape: exactly the tagline.
    with open(OUTPUT_PATH, "rb") as f:
        written = f.read()
    if written != TAGLINE.encode("utf-8"):
        raise ValueError(f"entry.txt holds {written!r}, expected exactly {TAGLINE!r}")


if __name__ == "__main__":
    main()
