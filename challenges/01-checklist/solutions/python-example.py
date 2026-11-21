# Reference solution, written with Claude Code to show the format.
# What it shows: strip() trims spaces, and `if line.strip()` skips blank lines.
# Run: python python-example.py < input.txt
import sys


def checklist(text):
    return [f"- [ ] {line.strip()}" for line in text.splitlines() if line.strip()]


if __name__ == "__main__":
    print("\n".join(checklist(sys.stdin.read())))
