# Reference solution, written with Claude Code to show the format.
# What it shows: a dictionary (Counter) counts things, and sorting by
# (-count, word) puts the biggest count first and breaks ties alphabetically.
# Run: python python-example.py < input.txt
import re
import sys
from collections import Counter

counts = Counter(re.findall(r"[a-z]+", sys.stdin.read().lower()))
for word, count in sorted(counts.items(), key=lambda item: (-item[1], item[0]))[:3]:
    print(f"{word}: {count}")
