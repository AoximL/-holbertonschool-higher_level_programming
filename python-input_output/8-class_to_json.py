#!/usr/bin/python3
"""
This module contains a function that returns the dictionary
description of an object for JSON serialization.
"""


def class_to_json(obj):
    """
    Returns the dictionary description of an object
    with simple data structures for JSON serialization.

    Args:
        obj: An instance of a Class.

    Returns:
        A dictionary containing all serializable attributes of obj.
    """
    # Return the object's attribute dictionary
    return obj.__dict__
