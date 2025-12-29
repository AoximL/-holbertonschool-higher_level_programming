#!/usr/bin/python3
"""
This module contains a function that writes a Python object
to a text file using its JSON representation.
"""

import json


def save_to_json_file(my_obj, filename):
    """
    Writes a Python object to a text file using JSON format.

    Args:
        my_obj: The Python object to serialize.
        filename: The name of the file to write to.
    """
    # Open the file in write mode with UTF-8 encoding
    with open(filename, "w", encoding="utf-8") as f:
        # Serialize the object to JSON and write it to the file
        json.dump(my_obj, f)
