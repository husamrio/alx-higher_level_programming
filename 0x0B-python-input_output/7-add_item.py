#!/usr/bin/python3
"""
Module 7-save_to_json_file includes a function that saves a
Python object to a file in JSON format
"""


def save_to_json_file(my_obj, filename):
    """Saves a Python object to a file in JSON format. The
    function takes two arguments: my_obj, the Python object
    to be saved, and filename, the name of the file to save to
    """
    import json

    with open(filename, mode="w", encoding="utf-8") as f:
        json.dump(my_obj, f)
