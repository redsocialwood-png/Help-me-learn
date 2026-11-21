# Challenge 01: Messy list to Markdown checklist

**Level:** beginner · **Time:** about 30 minutes · **Teaches:** strings, loops, edge cases

Use any programming language. Start with a string containing one item per line. Trim extra spaces, skip blank lines, and print each remaining item as `- [ ] item`.

## Example

Input:

```text
read a file

  rename a variable
write a test
```

Output:

```markdown
- [ ] read a file
- [ ] rename a variable
- [ ] write a test
```

## Edge cases to try

- Only blank lines → print nothing.
- Lines with only spaces or tabs → skip them.
- A single item with no trailing newline.

## How to know it worked

Run your program on the example above and compare the output by eye. Then try each edge case. Bonus: turn those into tests.

## Send your solution

Add one file to [`solutions/`](solutions/) named `<language>-<yourname>.<ext>` and open a pull request. See [CONTRIBUTING](../../CONTRIBUTING.md). A reference solution in Python is there to show the format.

## Stretch ideas

- Read the list from a file or from standard input.
- Support `- ` or `* ` bullets already in the input without doubling them.
- Number the items instead of using checkboxes.

---

## Português

Transforme uma lista bagunçada em checklist Markdown, em qualquer linguagem. Receba um texto com um item por linha, remova espaços extras, ignore linhas em branco e imprima cada item como `- [ ] item`. Casos de borda: só linhas em branco (imprime nada), linhas só com espaços ou tabs, item único sem quebra de linha no fim. Mande sua solução em `solutions/` com o nome `linguagem-seunome.ext`.
