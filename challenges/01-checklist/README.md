# Challenge 01: Messy list to Markdown checklist

**Level:** beginner · **Time:** about 30 minutes · **Teaches:** strings, loops, edge cases

Use any programming language. Read text from standard input, one item per line. Trim extra spaces, skip blank lines, and print each remaining item as `- [ ] item`.

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

Run `python your-solution.py < examples/example.in` and compare with `examples/example.out`. To check every example at once, put your file in `solutions/` and run `python scripts/check_solutions.py` from the repo root. The same check runs automatically on your pull request (Python and JavaScript).

## Send your solution

Add one file to [`solutions/`](solutions/) named `<language>-<github-username>.<ext>` and open a pull request. See [CONTRIBUTING](../../CONTRIBUTING.md). A reference solution in Python is there to show the format.

## Stretch ideas

- Support `- ` or `* ` bullets already in the input without doubling them.
- Number the items instead of using checkboxes.

---

## Português

Transforme uma lista bagunçada em checklist Markdown, em qualquer linguagem. Leia o texto da entrada padrão (stdin), um item por linha, remova espaços extras, ignore linhas em branco e imprima cada item como `- [ ] item`. Casos de borda: só linhas em branco (imprime nada), linhas só com espaços ou tabs, item único sem quebra de linha no fim. Mande sua solução em `solutions/` com o nome `linguagem-usuario-github.ext`. Para conferir, rode `python scripts/check_solutions.py` na raiz do repo; o mesmo teste roda sozinho no seu pull request.
