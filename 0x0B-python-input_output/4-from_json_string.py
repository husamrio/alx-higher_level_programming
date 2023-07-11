#!/usr/bin/python3
"""

Returns a Python data structure from a given JSON string
"""


def from_json_string(my_str):
    """Returns a Python data structure from a given JSON string.
    The function takes one argument, my_str, which is the JSON
    string representation to be converted. The function returns
    the corresponding Python object
    """
    import json

    return json.loads(my_str)
