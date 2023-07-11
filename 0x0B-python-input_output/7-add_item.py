#!/usr/bin/python3
"""
Module 7-save_to_json_file includes a function that saves a
Python object to a file in JSON format
"""


from sys import argv
save_to_json_file = __import__('5-save_to_json_file').save_to_json_file
load_from_json_file = __import__('6-load_from_json_file').load_from_json_file

filename = "add_item.json"

"""Saves a Python object to a file in JSON format. The
    function takes two arguments: my_obj, the Python object
    to be saved, and filename, the name of the file to save to
"""

try:
    existing_content = load_from_json_file(filename)
except FileNotFoundError:
    existing_content = []

save_to_json_file(existing_content + argv[1:], filename)
