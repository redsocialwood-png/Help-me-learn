# Challenge format

Each challenge should be small enough to complete in about 30 minutes.

Use this structure in `challenges/<number>-<name>/`:

- `README.md` with:
  - **Level** and estimated time
  - What the learner must build (input from standard input, output to standard output)
  - A complete input and expected output example
  - Edge cases that should be tried
  - A practical way to verify the result
  - Stretch ideas that are optional
  - Portuguese translation
- `examples/<case>.in` and `examples/<case>.out`: input and expected output for each example and edge case. Add `examples/<case>.args` when the program takes command-line arguments.
- `solutions/`: community solutions, named `<language>-<github-username>.<ext>`.

`python scripts/check_solutions.py` runs every Python and JavaScript solution against every example. GitHub Actions runs it on each pull request.

Add a reference solution only after the challenge examples and edge cases are clear.
