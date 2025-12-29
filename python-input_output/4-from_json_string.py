#!/usr/bin/python3
"""
This module contains a function that converts a JSON
string into a Python data structure.
"""

import json


def from_json_string(my_str):
    """
    Returns a Python object represented by a JSON string.

    Args:
        my_str: A string containing a JSON representation.

    Returns:
        A Python data structure corresponding to the JSON string.
    """
    # Parse the JSON string and return the corresponding Python object
    return json.loads(my_str)
