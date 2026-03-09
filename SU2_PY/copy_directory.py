#!/usr/bin/env python
# Copyright 2012-2026, SU2 Contributors (cf. AUTHORS.md)

import argparse
import os
import shutil


def parse_args():
    parser = argparse.ArgumentParser(
        description="Copy a directory recursively to a new destination."
    )
    parser.add_argument("source", help="Source directory to copy")
    parser.add_argument("destination", help="Destination directory (must not exist)")
    return parser.parse_args()


if __name__ == "__main__":
    args = parse_args()

    src = os.path.abspath(args.source)
    dst = os.path.abspath(args.destination)

    if not os.path.isdir(src):
        raise SystemExit("Source directory does not exist: %s" % src)
    if os.path.exists(dst):
        raise SystemExit("Destination already exists: %s" % dst)

    shutil.copytree(src, dst)
