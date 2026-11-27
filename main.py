#!/usr/bin/env python3
"""Entry point for the make.fun news-image-20261127 entry.

The front page itself is pre-rendered and shipped in this repository as
entry.png (1024x1024, 226,210 bytes). This program only copies that file
to the output directory the grader provides, then proves the copy is
intact: PNG magic bytes and dimensions first, then a byte-for-byte
SHA-256 match against the source. Any problem fails loudly (exit 1)
instead of leaving a partial or wrong entry behind.

Why a copy program and no drawing code: the grader runs
``python3 -P -s main.py`` in a stdlib-only sandbox, and under ``-P`` the
script's own directory is not on sys.path, so a sibling import such as
``from fontdata import FONTS`` crashes with ModuleNotFoundError before
anything is drawn. This program therefore has no sibling imports at
all — no fontdata, no Pillow, no drawing code — only the standard
library (hashlib, os, struct, sys). No network, no environment
secrets, no writes outside the output directory.
"""
import hashlib
import os
import struct
import sys

SOURCE_NAME = "entry.png"
OUTPUT_NAME = "entry.png"
PNG_MAGIC = b"\x89PNG\r\n\x1a\n"
MAX_BYTES = 1048576  # 1 MiB, the competition's size cap
MAX_DIMENSION = 1024  # the page is 1024x1024; nothing larger is valid


def sha256_of(path):
    """SHA-256 hex digest of a file, read in chunks."""
    digest = hashlib.sha256()
    with open(path, "rb") as handle:
        for chunk in iter(lambda: handle.read(65536), b""):
            digest.update(chunk)
    return digest.hexdigest()


def png_dimensions(data):
    """Return (width, height) from a PNG's IHDR chunk, or None if malformed.

    The IHDR chunk starts at byte 8 (length), 12 (type "IHDR"), then
    width and height as big-endian 32-bit integers at bytes 16 and 20.
    """
    if len(data) < 33 or data[12:16] != b"IHDR":
        return None
    width, height = struct.unpack(">II", data[16:24])
    return width, height


def fail(message):
    """Report an error on stderr and return the failure exit code."""
    print("error: %s" % message, file=sys.stderr)
    return 1


def main():
    # Locate the pre-rendered page next to this script, never via the
    # working directory, so the program works from any cwd.
    here = os.path.dirname(os.path.abspath(__file__))
    source = os.path.join(here, SOURCE_NAME)
    out_dir = os.environ.get("MAKEFUN_OUTPUT_DIR", "/output")
    target = os.path.join(out_dir, OUTPUT_NAME)

    if not os.path.isfile(source):
        return fail("%s not found next to main.py (%s)" % (SOURCE_NAME, source))

    try:
        with open(source, "rb") as handle:
            data = handle.read()
    except OSError as exc:
        return fail("cannot read %s: %s" % (source, exc))

    # Validate the source before writing anything.
    if data[:8] != PNG_MAGIC:
        return fail("%s is not a PNG (bad magic bytes)" % source)
    if len(data) > MAX_BYTES:
        return fail("%s is %d bytes, over the 1 MiB cap" % (source, len(data)))
    dims = png_dimensions(data)
    if dims is None:
        return fail("%s has no valid IHDR chunk" % source)
    if dims[0] > MAX_DIMENSION or dims[1] > MAX_DIMENSION:
        return fail("%s is %dx%d, over the 1024x1024 cap" % (source, dims[0], dims[1]))

    try:
        os.makedirs(out_dir, exist_ok=True)
        with open(target, "wb") as handle:
            handle.write(data)
    except OSError as exc:
        return fail("cannot write %s: %s" % (target, exc))

    # Re-read the copy and prove it is byte-for-byte identical to the
    # source before reporting success; a mismatch means the entry on
    # disk cannot be trusted, so fail instead of shipping it.
    try:
        with open(target, "rb") as handle:
            copied = handle.read()
    except OSError as exc:
        return fail("cannot re-read %s: %s" % (target, exc))
    if copied[:8] != PNG_MAGIC:
        return fail("copied file is not a PNG (bad magic bytes)")
    source_hash = hashlib.sha256(data).hexdigest()
    if hashlib.sha256(copied).hexdigest() != source_hash:
        return fail("copied file differs from source (SHA-256 mismatch)")

    print("wrote %s (%d bytes, sha256 %s)"
          % (target, len(copied), source_hash))
    return 0


if __name__ == "__main__":
    sys.exit(main())
