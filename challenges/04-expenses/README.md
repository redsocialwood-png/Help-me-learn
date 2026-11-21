# Challenge 04: Expense totals

**Level:** beginner+ · **Time:** about 30 minutes · **Teaches:** parsing, dictionaries, money and decimals

Read lines from standard input, each in the form `category,amount`. Print the total for each category, sorted alphabetically, then a final `total:` line. Every amount has exactly 2 decimals.

- Category names ignore case and surrounding spaces: `Food` and ` food` are the same.
- Amounts may have spaces around them and may have no decimals (`4`).
- Skip blank lines. You can assume every other line is valid.

## Example

Input:

```text
food, 12.50
transport,4
Food,7.25

rent,800
```

Output:

```text
food: 19.75
rent: 800.00
transport: 4.00
total: 823.75
```

## Edge cases to try

- `coffee,0.10` and `coffee,0.20` → `coffee: 0.30`. Check what your language does with `0.1 + 0.2`.
- Only blank lines → `total: 0.00`.

## Why money is tricky

Most languages store `0.1` as a binary float that is very slightly wrong, so `0.1 + 0.2` gives `0.30000000000000004`. Rounding when you print hides it here, but real money code uses a decimal type (Python `decimal.Decimal`) or whole cents (integers).

## How to know it worked

Run `python your-solution.py < examples/example.in` and compare with `examples/example.out`. Put your file in `solutions/` and run `python scripts/check_solutions.py` from the repo root to check every example; it also runs on your pull request.

## Send your solution

Add `solutions/<language>-<github-username>.<ext>` and open a pull request. See [CONTRIBUTING](../../CONTRIBUTING.md).

## Stretch ideas

- Read from a file whose name comes from a command-line argument.
- Report invalid lines (`skipped line 3`) instead of crashing.
- Sort categories by total, biggest first.

---

## Português

Leia linhas `categoria,valor` da entrada padrão e imprima o total de cada categoria em ordem alfabética, e no fim uma linha `total:`, sempre com 2 casas decimais. Categoria ignora maiúsculas e espaços; valor pode ter espaços e pode vir sem decimais; pule linhas em branco. Teste `0.10 + 0.20` na sua linguagem: dinheiro em float dá diferenças pequenas, por isso código de verdade usa tipo decimal ou centavos inteiros.
