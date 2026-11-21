# Challenge 02: Top 3 words

**Level:** beginner · **Time:** about 30 minutes · **Teaches:** dictionaries, sorting

Read text from standard input. Find the 3 most common words and print each as `word: count`, most common first.

- Ignore case: `The` and `the` are the same word.
- A word is a run of letters `a`–`z`. Anything else (spaces, punctuation, digits, apostrophes) separates words.
- On a tie, sort the tied words alphabetically.
- Fewer than 3 different words? Print the ones there are.

## Example

Input:

```text
The cat and the hat. The CAT sat!
```

Output:

```text
the: 3
cat: 2
and: 1
```

`and`, `hat` and `sat` all appear once; `and` wins because it comes first alphabetically.

## Edge cases to try

- Empty input → print nothing.
- `b a c b a` → `a: 2`, `b: 2`, `c: 1`.
- `hello, HELLO` → only `hello: 2`.

## How to know it worked

Run `python your-solution.py < examples/example.in` and compare with `examples/example.out`. Put your file in `solutions/` and run `python scripts/check_solutions.py` from the repo root to check every example; it also runs on your pull request.

## Send your solution

Add `solutions/<language>-<github-username>.<ext>` and open a pull request. See [CONTRIBUTING](../../CONTRIBUTING.md).

## Stretch ideas

- Take N from a command-line argument instead of always 3.
- Skip common words like "the", "a", "and".
- Treat accented letters (`é`, `ç`) as part of words.

---

## Português

Leia um texto da entrada padrão e imprima as 3 palavras mais frequentes como `palavra: contagem`, da mais frequente para a menos. Ignore maiúsculas e minúsculas; uma palavra é uma sequência de letras `a`–`z` (todo o resto separa palavras); em caso de empate, ordem alfabética; se houver menos de 3 palavras diferentes, imprima as que existirem. Entrada vazia não imprime nada. Ensina dicionários e ordenação.
