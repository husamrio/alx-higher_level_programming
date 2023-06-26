#!/usr/bin/python3
from sys import stderr


def safe_function(fct, *args):
    """
    Safely executes a given function with the provided arguments.
    :param fct: The function to be executed.
    :param args: Arguments for the function.
    :return: The result of the function call if successful, otherwise None.
    """
    try:
        return fct(*args)
    except Exception as e:
        stderr.write("Exception: {}\n".format(e))
        return None
