#!/usr/bin/python3
"""Defines a file-appending function"""


def append_write(filename="", text=""):
    """Appends a string to the end of a filetext
    Args:
        filename: The name of the file to append to
        text: the string to append
    """
    with open(filename, "a", encoding="utf-8") as f:
        return f.write(text)
