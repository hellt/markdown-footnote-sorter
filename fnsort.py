#!/usr/bin/python3

"""
Read a Markdown file passed as a first argument and sort footnotes.
The reference links will be numbered in
the order they appear in the text and placed at the bottom
of the file.

Based on https://github.com/derdennis/sort-markdown-footnotes which is
based on "Tidying Markdown reference links" by Dr. Drang available at:

http://www.leancrew.com/all-this/2012/09/tidying-markdown-reference-links/

Do *not* place footnote reference links at the start of a line, bad things will
happen, your footnotes will be eaten by a grue.
"""

import argparse
import re


def parse_arguments():
    parser = argparse.ArgumentParser(description="Tidy Markdown footnotes")
    parser.add_argument(
        "file",
        nargs="?",
        type=str,
        default="-",
        help="Input file to process (use - for stdin)",
    )
    return parser.parse_args()


# The regex for finding footnote reference links in the text.
# https://regex101.com/r/BZTNKG/2
# matches ([^2], 2) in Text[^2]
link = re.compile(r"[^\n](\[\^(\w+)\])")
# link = re.compile(r"[^(?<=\n)](\[\^fn([\d]+)\])")

# The regex for finding the footnote labels with the text.
# https://regex101.com/r/hNcv3X/1
label = re.compile(r"^\[\^([^\]]+)\]:\s*((?:(?!\n\[)[\s\S])*)", re.MULTILINE)


def refrepl(m, order):
    # Rewrite reference links with the reordered link numbers. Insert the first
    # character from the footnote reference link right before the new link.
    return "%s[^%s]" % (m.group(0)[:1], order.index(m.group(2)) + 1)


def sort_footnotes(text):
    # removes the last newline from EOF so there is no EOL on the last line
    text = text.rstrip()

    links = link.findall(text)
    # print(f"links: {links}")

    labels = dict(label.findall(text))
    # print(f"labels: {labels}")

    # Determine the order of the footnote-links in the text. If a link is used
    # more than once, its order is its first position.
    order = []
    [order.append(i[1]) for i in links if i[1] not in order]

    # print(f"order: {order}")

    # Make a list of the footnote-references in order of appearance the original footnotes in text.
    # this is not the order of the footnote contents, but the order of the footnote references in the text.
    newlabels = ["[^%s]: %s" % (i + 1, labels[j]) for (i, j) in enumerate(order)]
    # print(f"newlabels: {newlabels}")

    # Remove the old footnote-references and put the new ones at the end of the text.
    text = label.sub("", text).strip() + "\n" * 2 + "\n".join(newlabels)
    # print(f"text: {text}")

    # Rewrite the footnote-links with the new footnote-reference numbers.
    text = link.sub(lambda m: refrepl(m, order), text)

    return text


def main():
    args = parse_arguments()
    with open(args.file, "r+") as file:
        text = file.read()
        processed_text = sort_footnotes(text)
        file.seek(0)
        file.write(processed_text)
        file.truncate()


if __name__ == "__main__":
    main()
