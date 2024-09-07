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
