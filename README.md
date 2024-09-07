# markdown-footnote-sorter

A script to sort footnotes in a markdown file.

Reads a Markdown file passed as a first argument and sorts footnotes.
The reference links will be numbered in
the order they appear in the text and placed at the bottom
of the file.

Based on <https://github.com/derdennis/sort-markdown-footnotes> which is
based on "Tidying Markdown reference links" by Dr. Drang available at:

<http://www.leancrew.com/all-this/2012/09/tidying-markdown-reference-links/>

Do *not* place footnote reference links at the start of a line, bad things will
happen, your footnotes will be eaten by a grue.

## How to use?

You can use the container image provided:

```bash
docker run --rm -v $(pwd):/work ghcr.io/hellt/markdown-footnote-sorter path/to/doc.md
```

Or download the script and put it in your `$PATH`:

```bash
curl -sL https://raw.githubusercontent.com/hellt/markdown-footnote-sorter/main/fnsort.py
```
