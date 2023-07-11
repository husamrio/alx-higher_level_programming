#!/usr/bin/python3
"""

Generates a Python object from the data contained in a JSON file.
"""


def load_from_json_file(filename):
    """Creates a Python object from a JSON file. The function
    takes one argument, filename, which is the name of the file
    containing the JSON data
    """
    import json

    with open(filename, mode="r", encoding="utf-8") as f:
        return json.load(f)
