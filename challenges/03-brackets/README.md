# Challenge 03: Balanced brackets

**Level:** beginner+ · **Time:** about 30 minutes · **Teaches:** stacks, loops

Read lines from standard input. For each non-blank line, print `balanced` if every `(`, `[` and `{` is closed by the matching `)`, `]` or `}` in the right order, otherwise print `not balanced`. Ignore every other character. Skip blank lines.

## Example

Input:

```text
(a[b]{c})
([)]
((
print(x)
```

Output:

```text
balanced
not balanced
not balanced
balanced
```

`([)]` has the right number of each bracket, but `]` closes `(`: the order is wrong.

## Edge cases to try

- A line with no brackets → `balanced`.
- `)(` → `not balanced` (closes before it opens).
- `{[()()]}` → `balanced`.

## Hint

Counting brackets is not enough (see `([)]`). Keep a list of the brackets that are still open. When a closing bracket arrives, it must match the last one you opened.

## How to know it worked

Run `python your-solution.py < examples/example.in` and compare with `examples/example.out`. Put your file in `solutions/` and run `python scripts/check_solutions.py` from the repo root to check every example; it also runs on your pull request.

## Send your solution

Add `solutions/<language>-<github-username>.<ext>` and open a pull request. See [CONTRIBUTING](../../CONTRIBUTING.md).

## Stretch ideas

- For `not balanced`, also print the position of the first wrong character.
- Ignore brackets inside quotes, like `print(")")`.

---

## Português

Para cada linha não vazia da entrada, imprima `balanced` se todo `(`, `[` e `{` fecha com o par certo na ordem certa, senão `not balanced`. Ignore os outros caracteres e pule linhas em branco. Dica: contar não basta (`([)]` está errado); guarde uma lista dos que ainda estão abertos, e cada um que fecha tem que combinar com o último aberto. Isso se chama pilha (stack).
