# Reference solution, written with Claude Code to show the format.
# What it shows: a stack (a list where you add and remove at the end)
# remembers which bracket must close next.
# Run: python python-example.py < input.txt
import sys

PAIRS = {")": "(", "]": "[", "}": "{"}


def balanced(line):
    stack = []
    for ch in line:
        if ch in "([{":
            stack.append(ch)
        elif ch in PAIRS:
            if not stack or stack.pop() != PAIRS[ch]:
                return False
    return not stack


for line in sys.stdin.read().splitlines():
    if line.strip():
        print("balanced" if balanced(line) else "not balanced")
