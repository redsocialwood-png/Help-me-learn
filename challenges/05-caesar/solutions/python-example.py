# Reference solution, written with Claude Code to show the format.
# What it shows: sys.argv holds command-line arguments, ord()/chr() turn
# letters into numbers and back, and % 26 wraps z around to a.
# Run: python python-example.py 3 < message.txt
import sys


def shift_letter(ch, shift):
    for start in (ord("a"), ord("A")):
        if start <= ord(ch) < start + 26:
            return chr(start + (ord(ch) - start + shift) % 26)
    return ch


shift = int(sys.argv[1])
sys.stdout.write("".join(shift_letter(ch, shift) for ch in sys.stdin.read()))
