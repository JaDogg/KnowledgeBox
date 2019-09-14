#!/usr/bin/env python3
"""
This program is used to convert markdown file's tab indentations to 2 spaces.
"""

import argparse
from pathlib import Path
import io
import itertools
from multiprocessing import Pool

_TAB_2_SPACE = "  "


def fix_indent(filename):
    with io.open(filename, mode="r", encoding="utf-8") as h:
        text = h.read()

    lines = text.splitlines(True)
    skip = False
    for index, line in enumerate(lines):
        if line.startswith("```"):
            skip = not skip
        elif not skip and line.startswith("\t"):
            lines[index] = line.replace("\t", _TAB_2_SPACE)

    with io.open(filename, mode="w", encoding="utf-8") as h:
        h.write("".join(lines))


def main():
    parser = argparse.ArgumentParser(description="Fix indent")
    parser.add_argument(
        "files", metavar="N", type=str, nargs="+", help="List of files to scan"
    )

    args = parser.parse_args()
    all_files = tuple(
        itertools.chain(
            *[
                (filename for filename in Path().glob("**/" + file_))
                for file_ in args.files
            ]
        )
    )

    with Pool(2) as process_pool:
        process_pool.map(fix_indent, all_files)


if __name__ == "__main__":
    main()
