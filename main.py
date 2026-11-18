#!/usr/bin/env python3
"""Entrypoint for the 18 November 2026 poster.

The picture is committed as entry.png beside this file, so the graded run only
checks it against the competition's caps and copies the bytes to
/output/entry.png. render.py is what draws it.
"""
import os
import shutil
import struct
import sys

HERE = os.path.dirname(os.path.abspath(__file__))
SOURCE = os.path.join(HERE, "entry.png")
MAX_BYTES = 1024 * 1024
MAX_SIDE = 1024
PNG_MAGIC = b"\x89PNG\r\n\x1a\n"


def output_dir():
    """MAKEFUN_OUTPUT_DIR on a local run, /output in the sandbox."""
    return os.environ.get("MAKEFUN_OUTPUT_DIR") or "/output"


def png_size(path):
    """Width and height, read from the IHDR chunk."""
    with open(path, "rb") as fh:
        head = fh.read(24)
    if head[:8] != PNG_MAGIC:
        raise SystemExit("entry.png is not a PNG: %r" % head[:8])
    return struct.unpack(">II", head[16:24])


def main():
    """Refuse an image the gate would score invalid, then write it out."""
    size = os.path.getsize(SOURCE)
    width, height = png_size(SOURCE)
    if size > MAX_BYTES:
        raise SystemExit("entry.png is %d bytes, over the 1 MiB cap" % size)
    if max(width, height) > MAX_SIDE:
        raise SystemExit("entry.png is %dx%d, over the 1024 cap" % (width, height))
    out = output_dir()
    os.makedirs(out, exist_ok=True)
    target = os.path.join(out, "entry.png")
    shutil.copyfile(SOURCE, target)
    print("entry.png %dx%d, %d bytes -> %s" % (width, height, size, target))
    return 0


if __name__ == "__main__":
    sys.exit(main())
