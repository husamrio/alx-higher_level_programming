#!/usr/bin/python3
"""
This function adds a string after lines in a file that contain a
specified keyword.
"""


def append_after(filename="", search_string="", new_string=""):
    """
    This function adds a string after lines in a file that contain a
    specified keyword.

    Args:
        filename (str): The name of the file to modify.
        search_string (str): The keyword to search for in the file.
        new_string (str): The string to add after lines containing the
        keyword.
    """
    with open(filename, mode="r+", encoding="utf-8") as f:
        new_text = ""
        for line in f:
            new_text += line
            if search_string in line:
                new_text += new_string
        f.seek(0)
        f.write(new_text)
