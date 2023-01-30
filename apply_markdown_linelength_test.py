"""
This file contains the unit testing suite for the package to apply
the markdown line length to all *.md files in a given folder.
"""

import apply_markdown_linelengths as aml


# Using pytest's tmpdir fixture, which creates a temporary folder
# for test purposes
def test_apply_markdown_line_length(tmpdir):
    tmp_file = tmpdir.join("test.md")
    tmp_file.write("a"*60 + ". " + "b"*60)  # create line with length over limit

    line_lengths_applied = aml.apply_markdown_line_length(tmpdir)
    assert line_lengths_applied is True

    contents = tmp_file.read().split("\n")
    line_lengths = [len(line) for line in contents]

    assert max(line_lengths) < aml.LINE_LENGTH
