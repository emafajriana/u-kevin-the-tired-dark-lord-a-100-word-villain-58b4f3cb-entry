#!/usr/bin/env python3
"""The Tired Dark Lord: A 100-Word Villain Monologue — make.fun entry.

Writes one 100-word monologue to entry.txt.
Stdlib only: the grader runs python3 -P -s in stock python:3.13-slim.
"""

import os
from pathlib import Path

ENTRY = (
    "Come in. Mind the skulls \u2014 polished Tuesday. Sit. Not that chair; "
    "it bites. The other one. Good. You came to bargain for the valley, "
    "I expect. Thirty years I've held it: the tolls, the tithe, the "
    "little bell that rings when someone lies to me. It rang twice "
    "while you walked in. Here is my price: nothing. Take the valley. "
    "Take the bell, too. I'm keeping the armchair. Don't look surprised. "
    "Even a dark lord gets... look, the moat needs dredging, the ravens "
    "unionised, and the eclipse was three weeks ago. Sign here. The "
    "ink's dry. It always is."
)


def main() -> int:
    out_dir = Path(os.environ.get("MAKEFUN_OUTPUT_DIR", "/output"))
    out_dir.mkdir(parents=True, exist_ok=True)
    target = out_dir / "entry.txt"
    text = ENTRY.strip()
    # Gate (RULES.txt): UTF-8 text, 1-600 chars, not only whitespace.
    assert text and not text.isspace(), "entry must not be blank"
    assert 1 <= len(text) <= 600, f"entry length {len(text)} out of gate"
    # Judge brief: about 100 words, every word spent.
    words = text.split()
    assert 95 <= len(words) <= 105, f"word count {len(words)} off target"
    target.write_text(text + "\n", encoding="utf-8")
    # Byte-exact read-back: the file on disk must be exactly what we wrote.
    written = target.read_bytes()
    assert written == (text + "\n").encode("utf-8"), "read-back mismatch"
    assert written.decode("utf-8") == text + "\n", "UTF-8 round-trip mismatch"
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
