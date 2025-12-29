#!/usr/bin/python3
"""
This module contains a function that appends a string
to the end of a UTF-8 text file and returns the number
of characters added.
"""


def append_write(filename="", text=""):
    """
    Appends a string to the end of a text file (UTF-8)
    and returns the number of characters added.

    If the file does not exist, it will be created.
    """
    # Open the file in append mode with UTF-8 encoding
    with open(filename, "a", encoding="utf-8") as f:
        # Write the text to the file and return number of characters written
        return f.write(text)
