# markdown-footnote-sorter

A script to sort footnotes in a markdown file.

Reads a Markdown file passed as the first argument and sorts footnotes.
The reference links will be numbered in
the order they appear in the text and placed at the bottom
of the file.

Based on <https://github.com/derdennis/sort-markdown-footnotes>

Inspired by <http://www.leancrew.com/all-this/2012/09/tidying-markdown-reference-links/>

[Example video](https://github.com/user-attachments/assets/2ccb1782-1d85-499c-ba09-3be94c34a591)

## How to use?

1. You can use the container image provided:

    ```bash
    docker run --rm -v $(pwd):/work ghcr.io/hellt/markdown-footnote-sorter path/to/doc.md
    ```

1. Or download the script and put it in your `$PATH`:

    ```bash
    curl -sL \
    https://raw.githubusercontent.com/hellt/markdown-footnote-sorter/main/fnsort.py\
      > ~/.local/bin/fnsort.py

    fnsort.py path/to/doc.md
    ```

1. Or from the GitHub UI, run the container in a :sparkles:[Codespace](https://docs.github.com/en/codespaces/overview):

   * From this project's main page, click **Code**, then **Codespace**.
   * Choose **Create codespace on &lt;branch_name&gt;**

   This [creates a codespace](https://docs.github.com/en/codespaces/developing-in-a-codespace/creating-a-codespace-for-a-repository#creating-a-codespace-for-a-repository)
   with the default resources (currently 2 CPU, 8 GB RAM, 32 GB Storage).

   * :rocket: Run fnsort on your markdown file:

   ```bash
   /app/fnsort.py path/to/doc.md
   ```

> [!IMPORTANT]
> Keep in mind there are
> [monthly limits measured in core hours](https://docs.github.com/en/billing/managing-billing-for-your-products/managing-billing-for-github-codespaces/about-billing-for-github-codespaces#monthly-included-storage-and-core-hours-for-personal-accounts)
and to
[stop your codespace](https://docs.github.com/en/codespaces/developing-in-a-codespace/stopping-and-starting-a-codespace)
:stop_sign: when you're not using it to conserve your monthly core hours
allowance.

## Command Line Arguments

### --adjacent

Adjacent inline references that are not separated by other characters become
problematic (by default).
This option adds spacing between those inline references so they are properly
identified during sorting.

`fnsort.py path/to/doc.md --adjacent`

### --keepnames

Retain or keep inline reference and footnote names.
This prevents the default behavior of replacing the names with numbers.
Footnotes at the end of the markdown are **still sorted**.

`fnsort.py path/to/doc.md --keepnames`

## Contributing

For information about contributing to this project, see the
[contributing guidelines](CONTRIBUTING.md).
