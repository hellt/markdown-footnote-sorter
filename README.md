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

fnsort.py path/to/doc.md
```

## Command Line Arguments
### --adjacent
Adjacent inline references that are not separated by other characters become problematic (by default).
This option adds spacing between those inline references so they are properly identified during sorting.

`fnsort.py path/to/doc.md --adjacent`

### --keepnames
Retain or keep inline reference and footnote names.
This prevents the default behavior of replacing the names with numbers.
Footnotes at the end of the markdown are **still sorted**.

`fnsort.py path/to/doc.md --keepnames`

## Contributing
For information about contributing to this project, see the [contributing guidelines](CONTRIBUTING.md).
