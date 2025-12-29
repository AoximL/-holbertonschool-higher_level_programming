#!/usr/bin/python3
"""
100-append_after.py
Insert a line of text after each line containing a specific string
"""


def append_after(filename="", search_string="", new_string=""):
    """Insert new_string after each line containing search_string
    in filename"""
    with open(filename, "r", encoding="utf-8") as f:
        lines = f.readlines()

    # Insert new_string after each line that contains search_string
    new_lines = []
    for line in lines:
        new_lines.append(line)
        if search_string in line:
            new_lines.append(new_string)

    with open(filename, "w", encoding="utf-8") as f:
        f.writelines(new_lines)
