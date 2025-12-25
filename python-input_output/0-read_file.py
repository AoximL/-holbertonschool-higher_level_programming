#!/usr/bin/python3
"""
This module contains a function that reads a text file and prints it.
It uses the UTF-8 encoding and the 'with' statement for safety.
"""


def read_file(filename=""):
    """
    Reads a text file (UTF8) and prints it to stdout.

    Args:
        filename (str): The name of the file to be read.
    """
    with open(filename, "r", encoding="utf-8") as f:
        print(f.read(), end="")
