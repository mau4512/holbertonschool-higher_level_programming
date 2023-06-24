#!/usr/bin/python3
"""Function that writes a string into a text file"""


def write_file(filename="", text=""):
    """Write a string into a text
    Args:
        filename: the name of the file to write
        text: The text to write to the file
    """
    with open(filename, "w", encoding="utf-8") as f:
        return f.write(text)
