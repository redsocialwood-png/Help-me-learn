# Reference solution, written with Claude Code to show the format.
# What it shows: Decimal adds money exactly (0.10 + 0.20 is 0.30, not
# 0.30000000000000004 like a float), and a dictionary groups by category.
# Run: python python-example.py < expenses.txt
import sys
from decimal import Decimal

totals = {}
for line in sys.stdin.read().splitlines():
    if not line.strip():
        continue
    category, amount = line.split(",")
    category = category.strip().lower()
    totals[category] = totals.get(category, Decimal("0")) + Decimal(amount.strip())

for category in sorted(totals):
    print(f"{category}: {totals[category]:.2f}")
print(f"total: {sum(totals.values(), Decimal('0')):.2f}")
