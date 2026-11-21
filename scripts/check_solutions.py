"""Run every solution against its challenge's examples.

For each challenge with an examples/ folder, every file in solutions/ written in a
supported language is run once per example:
  examples/<case>.in    sent to standard input
  examples/<case>.out   expected standard output
  examples/<case>.args  optional command-line arguments (one line)

Usage: python scripts/check_solutions.py
"""
import os
import pathlib
import shlex
import subprocess
import sys

ROOT = pathlib.Path(__file__).resolve().parent.parent
RUNNERS = {".py": [sys.executable], ".js": ["node"]}
ENV = {**os.environ, "PYTHONIOENCODING": "utf-8"}


def read(path):
    return path.read_text(encoding="utf-8") if path.exists() else ""


def check(solution, case):
    args = shlex.split(read(case.with_suffix(".args")))
    try:
        result = subprocess.run(
            RUNNERS[solution.suffix] + [str(solution)] + args,
            input=read(case),
            capture_output=True,
            text=True,
            encoding="utf-8",
            env=ENV,
            timeout=10,
        )
    except subprocess.TimeoutExpired:
        return "timed out after 10 seconds"
    if result.returncode != 0:
        return f"exited with code {result.returncode}\n{result.stderr}"
    expected = read(case.with_suffix(".out"))
    # Ignore only the final newline, so "print nothing" and "print one line" stay distinct.
    if result.stdout.rstrip("\n") != expected.rstrip("\n"):
        return f"expected:\n{expected}\ngot:\n{result.stdout}"
    return None


def main():
    passed = failed = 0
    for examples in sorted(ROOT.glob("challenges/*/examples")):
        solutions = sorted((examples.parent / "solutions").glob("*"))
        for solution in solutions:
            if solution.suffix not in RUNNERS or solution.name.startswith("test_"):
                continue
            for case in sorted(examples.glob("*.in")):
                name = f"{solution.relative_to(ROOT).as_posix()} [{case.stem}]"
                error = check(solution, case)
                if error:
                    failed += 1
                    print(f"FAIL {name}: {error}")
                else:
                    passed += 1
                    print(f"PASS {name}")
    print(f"\n{passed} passed, {failed} failed")
    return 1 if failed or not passed else 0


if __name__ == "__main__":
    sys.exit(main())
