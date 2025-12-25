#!/usr/bin/python3
"""This module defines a function."""
def write_file(filename ="", text=""):
    """Writes a string to a text file (UTF8)."""
    with open(filename, "w", encoding="utf-8")as f:
        return f.write(text)
