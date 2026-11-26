"""Worst Monday One-Liners — a one-line Monday misery, printed to a file.

The program holds exactly one joke: a Monday that opens with a deploy
frozen at 99% and closes with a stand-up that should have been an email —
and the email turns out to be a meeting too. It validates the line, then
writes it to /output/entry.txt so the grader can read it back.
"""

import os
import sys

# The single one-liner this entry ships (133 characters, one line).
ONE_LINER = (
    "My Monday started with a deploy stuck at 99% and ended with a "
    "stand-up that should have been an email \u2014 the email was also "
    "a meeting."
)

DEFAULT_OUTPUT = "/output/entry.txt"
MAX_LINE_LENGTH = 200


def check_line(line):
    """Refuse anything that is not one plain, non-empty line."""
    if not isinstance(line, str) or not line.strip():
        raise ValueError("one-liner must be a non-empty string")
    if "\n" in line or "\r" in line:
        raise ValueError("one-liner must fit on a single line")
    if len(line) > MAX_LINE_LENGTH:
        raise ValueError("one-liner is longer than %d characters" % MAX_LINE_LENGTH)
    return line


def write_entry(line, output_path):
    """Write the validated line to output_path, world-readable."""
    os.umask(0o022)
    directory = os.path.dirname(output_path)
    if directory:
        os.makedirs(directory, exist_ok=True)
    with open(output_path, "w", encoding="utf-8") as handle:
        handle.write(line + "\n")
    os.chmod(output_path, 0o644)
    with open(output_path, "r", encoding="utf-8") as handle:
        stored = handle.read()
    if stored != line + "\n":
        raise IOError("read-back mismatch in %s" % output_path)
    return output_path


def main(argv):
    """Entry point: validate the line, write it, report where it went."""
    line = check_line(ONE_LINER)
    output_path = argv[1] if len(argv) > 1 else DEFAULT_OUTPUT
    written = write_entry(line, output_path)
    print("Wrote %d characters to %s" % (len(line), written))
    return 0


if __name__ == "__main__":
    raise SystemExit(main(sys.argv))
