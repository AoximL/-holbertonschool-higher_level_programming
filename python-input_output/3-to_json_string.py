#!/usr/bin/python3
"""
This module contains a function that returns the JSON
representation of a Python object as a string.
"""

import json


def to_json_string(my_obj):
    """
    Returns the JSON representation of an object (string).

    Args:
        my_obj: The Python object to convert to JSON.

    Returns:
        A string containing the JSON representation of my_obj.
    """
    # Convert the Python object to a JSON string and return it
    return json.dumps(my_obj)
