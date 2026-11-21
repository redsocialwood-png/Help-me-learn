import importlib.util
import pathlib
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


if __name__ == "__main__":
    unittest.main()
