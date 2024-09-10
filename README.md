# markdown-footnote-sorter

A script to sort footnotes in a markdown file.

Reads a Markdown file passed as a first argument and sorts footnotes.
The reference links will be numbered in
the order they appear in the text and placed at the bottom
of the file.

Based on <https://github.com/derdennis/sort-markdown-footnotes>



https://github.com/user-attachments/assets/2ccb1782-1d85-499c-ba09-3be94c34a591



## How to use?

You can use the container image provided:

```bash
docker run --rm -v $(pwd):/work ghcr.io/hellt/markdown-footnote-sorter path/to/doc.md
```

Or download the script and put it in your `$PATH`:

```bash
curl -sL https://raw.githubusercontent.com/hellt/markdown-footnote-sorter/main/fnsort.py
```

## Development and Testing
All code modifications should be accompanied by unit tests.

It is recommended to verify tests are successful before making any code changes. From there make your changes and run the unit tests to validate there is not code regression.

For minimal dependencies, the "batteries included" Python unittest framework is utilized. (Other testing frameworks could be considered should additional testing features be needed.)

### Running Unit Tests
Discover and run unit tests (from the top level of the project directory)

`python -m unittest discover`

Verbose version of unit test discovery

`python -m unittest discover -v`

For additional command line options, refer to the [official Python unittest documentation](https://docs.python.org/3/library/unittest.html#command-line-interface).
