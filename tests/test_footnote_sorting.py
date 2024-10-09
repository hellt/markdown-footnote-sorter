import argparse
import unittest

import fnsort


def set_command_line_args(args):
    """Set (what would otherwise be) command-line arguments"""
    return argparse.Namespace(**args)


class TestDefaults(unittest.TestCase):
    @classmethod
    def setUpClass(self):
        # example markdown files intentionally have had trailing EOL trimmed
        #   from the end of the file (EOF)

        path = "tests/default"

        with open(f"{path}/example.md") as fh:
            self.text = fh.read()

        with open(f"{path}/example_expected.md") as fh:
            self.expected_text = fh.read()

        # technically there is also a "file" kwarg by default
        args = {"adjacent": False, "keepnames": False}
        self.args = set_command_line_args(args)
        if self.args.adjacent:
            self.text = fnsort.space_adjacent_references(self.text)

        # allow for full diff output
        # self.maxDiff = None

    def test_replace_reference(self):
        """Inline reference replacement"""
        # use the link regex from the fnsort import

        # "search" function only returns the first match
        match = fnsort.link.search(self.text)
        order = ["1", "3", "4", "2"]

        # hedgehogs[^1]
        self.assertEqual(fnsort.replace_reference(match, order), "s[^1]")

    def test_footnote_sort(self):
        """Entire footnote sort process"""
        self.assertEqual(
            fnsort.sort_footnotes(self.text, self.args), self.expected_text
        )


class TestDuplicates(unittest.TestCase):
    @classmethod
    def setUpClass(self):
        path = "tests/duplicates"

        with open(f"{path}/duplicates.md") as fh:
            self.text = fh.read()

        with open(f"{path}/duplicates_expected.md") as fh:
            self.expected_text = fh.read()

        # technically there is also a "file" kwarg by default
        args = {"adjacent": False, "keepnames": False}
        self.args = set_command_line_args(args)
        if self.args.adjacent:
            self.text = fnsort.space_adjacent_references(self.text)

        # allow for full diff output
        # self.maxDiff = None

    def test_replace_references_with_dups(self):
        """Multiple reference replacements with duplicate tags"""
        # find all matches
        matches = fnsort.link.finditer(self.text)
        order = ["1", "3", "2", "5", "4"]

        # should be seven regex matches in duplicates.md
        expected = [
            "s[^1]",
            "s[^2]",
            " [^1]",
            "s[^3]",
            "s[^4]",
            "s[^5]",
            " [^2]",
        ]

        # multiple assertions
        for i, match in enumerate(matches):
            self.assertEqual(
                fnsort.replace_reference(match, order), expected[i]
            )

    def test_footnote_sort_with_dups(self):
        """Entire footnote sort process with duplicate tags"""
        self.assertEqual(
            fnsort.sort_footnotes(self.text, self.args), self.expected_text
        )


class TestFootnotesMustBeLast(unittest.TestCase):
    @classmethod
    def setUpClass(self):
        path = "tests/fn_must_be_last"

        with open(f"{path}/must_be_last.md") as fh:
            self.text = fh.read()

        with open(f"{path}/must_be_last_expected.md") as fh:
            self.expected_text = fh.read()

        # technically there is also a "file" kwarg by default
        args = {"adjacent": False, "keepnames": False}
        self.args = set_command_line_args(args)
        if self.args.adjacent:
            self.text = fnsort.space_adjacent_references(self.text)

        # allow for full diff output
        # self.maxDiff = None

    def test_footnote_sort_trailing_text(self):
        """[negative test] Entire footnote sort process with text after the footnotes"""

        """
        negative test

        text after the last footnote will be captured as part of that
          footnote creating a choppy looking list

        in short this is not expected to return the desired output
        """
        self.assertNotEqual(
            fnsort.sort_footnotes(self.text, self.args), self.expected_text
        )


class TestAdjacentFootnotes(unittest.TestCase):
    @classmethod
    def setUpClass(self):
        # example markdown files intentionally have had trailing EOL trimmed
        #   from the end of the file (EOF)

        path = "tests/adjacent"

        with open(f"{path}/adjacent.md") as fh:
            self.text = fh.read()

        with open(f"{path}/adjacent_expected.md") as fh:
            self.expected_text = fh.read()

        # technically there is also a "file" kwarg by default
        args = {"adjacent": True, "keepnames": False}
        self.args = set_command_line_args(args)

        # allow for full diff output
        # self.maxDiff = None

    def test_adjacent_inline_reference_spacing(self):
        """Test spacing out adjacent inline references"""
        with open("tests/adjacent/adjacent_spacing.md") as fh:
            spacing_text = fh.read()

        self.assertEqual(
            fnsort.space_adjacent_references(self.text), spacing_text
        )

    def test_adjacent_footnote_sort(self):
        """Entire footnote sort process with adjacent footnote references"""
        if self.args.adjacent:
            self.text = fnsort.space_adjacent_references(self.text)

        self.assertEqual(
            fnsort.sort_footnotes(self.text, self.args), self.expected_text
        )


class TestKeepFootnoteNames(unittest.TestCase):
    @classmethod
    def setUpClass(self):
        path = "tests/keep_fn_names"

        with open(f"{path}/keep_fn_names.md") as fh:
            self.text = fh.read()

        with open(f"{path}/keep_fn_names_expected.md") as fh:
            self.expected_text = fh.read()

        # technically there is also a "file" kwarg by default
        args = {"adjacent": False, "keepnames": True}
        self.args = set_command_line_args(args)

        # allow for full diff output
        # self.maxDiff = None

    def test_keep_footnote_names(self):
        """Entire footnote sort process while retaining footnote names"""
        if self.args.adjacent:
            self.text = fnsort.space_adjacent_references(self.text)

        self.assertEqual(
            fnsort.sort_footnotes(self.text, self.args), self.expected_text
        )


class TestMissingFootnotes(unittest.TestCase):
    @classmethod
    def setUpClass(self):
        path = "tests/missing"

        with open(f"{path}/missing.md") as fh:
            self.text = fh.read()

        # missing footnotes or inline refs throw exceptions so there's no
        #   sense in "expected" test file

        # technically there is also a "file" kwarg by default
        args = {"adjacent": False, "keepnames": False}
        self.args = set_command_line_args(args)

        # allow for full diff output
        # self.maxDiff = None

    def test_missing_footnotes(self):
        """
        [negative test] Entire footnote sort process with missing footnotes and inline references
        """
        if self.args.adjacent:
            self.text = fnsort.space_adjacent_references(self.text)

        with self.assertRaises(fnsort.MissingFootnoteError):
            fnsort.sort_footnotes(self.text, self.args)


if __name__ == "__main__":
    unittest.main()
