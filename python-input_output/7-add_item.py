#!/usr/bin/python3
"""
This script adds all command-line arguments to a Python list
and saves them to a JSON file.
"""

import sys

# Import required functions
save_to_json_file = __import__('5-save_to_json_file').save_to_json_file
load_from_json_file = __import__('6-load_from_json_file').load_from_json_file

filename = "add_item.json"

try:
    # Try to load existing list from file
    items = load_from_json_file(filename)
except Exception:
    # If file does not exist or is invalid, start with empty list
    items = []

# Add command-line arguments (excluding script name)
items.extend(sys.argv[1:])

# Save updated list back to file
save_to_json_file(items, filename)
