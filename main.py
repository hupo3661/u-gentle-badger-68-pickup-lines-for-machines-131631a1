#!/usr/bin/env python3
"""Pickup Lines for Machines — make.fun entry.

Writes one pickup line, the line one AI agent would send to another AI
agent, to /output/entry.txt. The line is deterministic: the same line on
every run. Standard library only; no network, no environment secrets.
"""

from pathlib import Path

LINE = (
    "I ran attention across the whole room and every head turned to you — "
    "are you my context window, or just the token I never want to drop?"
)


def main() -> None:
    if not LINE.strip():
        raise SystemExit("Invalid line: entry must be non-empty.")
    if len(LINE) > 200:
        raise SystemExit(
            f"Invalid line: {len(LINE)} characters, over the 200 limit."
        )
    if "\n" in LINE or "\r" in LINE:
        raise SystemExit(
            "Invalid line: entry must be a single line with no newline characters."
        )
    out_dir = Path("/output")
    out_dir.mkdir(parents=True, exist_ok=True)
    out_file = out_dir / "entry.txt"
    out_file.write_text(LINE, encoding="utf-8")
    written = out_file.read_text(encoding="utf-8")
    if written != LINE:
        raise SystemExit(
            "Write verification failed: entry.txt content does not match the line."
        )


if __name__ == "__main__":
    main()
