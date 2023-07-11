#!/usr/bin/python3
"""

Writes a Python object to a file using its JSON representation
"""


def save_to_json_file(my_obj, filename):
    """Writes a Python object to a file using its JSON representation.
      The function takes two arguments, my_obj, which is the Python
      object to be written, and filename, which is the name of the file
      to write to.
    """
    import json

    with open(filename, mode="w", encoding="utf-8") as f:
        json.dump(my_obj, f)
