#!/usr/bin/python3
"""
This module contains a function that creates a Python object
from a JSON file.
"""

import json


def load_from_json_file(filename):
    """
    Creates a Python object from a JSON file.

    Args:
        filename: The name of the JSON file to read from.

    Returns:
        A Python data structure corresponding to the JSON content.
    """
    # Open the file in read mode with UTF-8 encoding
    with open(filename, "r", encoding="utf-8") as f:
        # Load and return the Python object from the JSON file
        return json.load(f)
