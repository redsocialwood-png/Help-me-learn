# Challenge 05: Caesar cipher

**Level:** beginner+ · **Time:** about 30 minutes · **Teaches:** command-line arguments, character codes, modulo

Read a shift number from the first command-line argument and text from standard input. Print the text with every letter moved that many places in the alphabet.

- Keep upper and lower case: `A` stays upper case.
- Wrap around: with shift 1, `z` becomes `a`.
- Leave everything that isn't `a`–`z` or `A`–`Z` unchanged (spaces, punctuation, digits, line breaks).
- A negative shift moves backwards, so it decodes. Shifts bigger than 26 wrap too (29 works like 3).

## Example

```text
python your-solution.py 3
```

Input:

```text
Hello, World!
```

Output:

```text
Khoor, Zruog!
```

Running with `-3` on `Khoor, Zruog!` gives back `Hello, World!`.

## Edge cases to try

- Shift `1` on `xyz XYZ` → `yza YZA`.
- Shift `29` on `abc` → `def`.
- Text with several lines keeps its line breaks.

## How to know it worked

Run `python your-solution.py 3 < examples/encode.in` and compare with `examples/encode.out`. Each example's shift is in its `.args` file. Put your file in `solutions/` and run `python scripts/check_solutions.py` from the repo root to check every example; it also runs on your pull request.

## Send your solution

Add `solutions/<language>-<github-username>.<ext>` and open a pull request. See [CONTRIBUTING](../../CONTRIBUTING.md).

## Stretch ideas

- Print a friendly error when the shift is missing or not a number.
- Crack a message without knowing the shift: try all 26 and pick the one with the most common English words.

---

## Português

Leia o deslocamento do primeiro argumento da linha de comando e o texto da entrada padrão, e imprima o texto com cada letra andando esse número de casas no alfabeto. Mantenha maiúsculas e minúsculas, dê a volta (`z` + 1 = `a`), não mexa no que não for letra `a`–`z`/`A`–`Z`. Deslocamento negativo decodifica, e 29 funciona como 3. Ensina argumentos de linha de comando, códigos de caracteres e o operador de resto (`%`).
