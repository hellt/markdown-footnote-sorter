import unittest

import fnsort

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

        # allow for full diff output
        # self.maxDiff = None


    def test_replace_reference(self):
        """ Inline reference replacement """
        # use the link regex from the fnsort import
           
        # "search" function only returns the first match
        match = fnsort.link.search(self.text)
        order = ["1", "3", "4", "2"]

        # hedgehogs[^1]
        self.assertEqual(
            fnsort.reference_replace(match, order),
            "s[^1]"
        )


    def test_footnote_sort(self):
        """ Entire footnote sort process """
        self.assertEqual(fnsort.sort_footnotes(self.text), self.expected_text)


class TestDuplicates(unittest.TestCase):
    @classmethod
    def setUpClass(self):
        path = "tests/duplicates"

        with open(f"{path}/duplicates.md") as fh:
            self.text = fh.read()

        with open(f"{path}/duplicates_expected.md") as fh:
            self.expected_text = fh.read()

        # allow for full diff output
        # self.maxDiff = None


    def test_replace_references_with_dups(self):
        """ Multiple reference replacements with duplicate tags """
        # find all matches
        matches = fnsort.link.finditer(self.text)
        order = ["1", "3", "2", "5", "4"]

        # should be seven regex matches in duplicates.md
        expected = [
            "s[^1]", "s[^2]", " [^1]", "s[^3]", "s[^4]", "s[^5]", " [^2]"
        ]

        # multiple assertions
        for i, match in enumerate(matches):
            self.assertEqual(
                fnsort.reference_replace(match, order),
                expected[i]
            )


    def test_footnote_sort_with_dups(self):
        """ Entire footnote sort process with duplicate tags """
        self.assertEqual(fnsort.sort_footnotes(self.text), self.expected_text)


class TestFootnotesMustBeLast(unittest.TestCase):
    @classmethod
    def setUpClass(self):
        path = "tests/fn_must_be_last"

        with open(f"{path}/must_be_last.md") as fh:
            self.text = fh.read()

        with open(f"{path}/must_be_last_expected.md") as fh:
            self.expected_text = fh.read()

        # allow for full diff output
        # self.maxDiff = None


    def test_footnote_sort_trailing_text(self):
        """ [negative test] Entire footnote sort process with text after the footnotes """

        """
        negative test

        text after the last footnote will be captured as part of that
          footnote creating a choppy looking list

        in short this is not expected to return the desired output

        just so happened to luck out that the last footnote reference of the
            "duplicates" example was indeed the last footnote :shrug:
        """
        self.assertNotEqual(fnsort.sort_footnotes(self.text), self.expected_text)


if __name__ == "__main__":
    unittest.main()
