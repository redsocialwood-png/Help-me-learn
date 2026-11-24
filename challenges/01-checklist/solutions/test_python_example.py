import importlib.util
import pathlib
import subprocess
import sys
import unittest

spec = importlib.util.spec_from_file_location(
    "python_example", pathlib.Path(__file__).with_name("python-example.py")
)
mod = importlib.util.module_from_spec(spec)
spec.loader.exec_module(mod)


class ChecklistTest(unittest.TestCase):
    def test_example(self):
        text = "read a file\n\n  rename a variable\nwrite a test"
        self.assertEqual(
            mod.checklist(text),
            ["- [ ] read a file", "- [ ] rename a variable", "- [ ] write a test"],
        )

    def test_only_blank_lines(self):
        self.assertEqual(mod.checklist("\n  \n\t\n"), [])

    def test_single_item_no_newline(self):
        self.assertEqual(mod.checklist("one"), ["- [ ] one"])

    def test_command_line_input(self):
        result = subprocess.run(
            [sys.executable, pathlib.Path(__file__).with_name("python-example.py")],
            input="read a file\n\n write a test ",
            capture_output=True,
            text=True,
            check=True,
        )

        self.assertEqual(
            result.stdout,
            "- [ ] read a file\n- [ ] write a test\n",
        )

    def test_command_line_blank_input_prints_nothing(self):
        result = subprocess.run(
            [sys.executable, pathlib.Path(__file__).with_name("python-example.py")],
            input="\n  \n\t\n",
            capture_output=True,
            text=True,
            check=True,
        )

        self.assertEqual(result.stdout, "")


if __name__ == "__main__":
    unittest.main()
