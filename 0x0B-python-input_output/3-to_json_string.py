#!/usr/bin/python3
"""

Returns a string containing the JSON representation
of the given object.”
"""


def to_json_string(my_obj):
    """Returns a string containing the JSON representation
      of the given Python object. The function takes one
      argument, my_obj, which is the Python object to be converted.
      The function returns the JSON string representation of the object.
    """
    import json

    return json.dumps(my_obj)
