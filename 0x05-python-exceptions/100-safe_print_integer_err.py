#!/usr/bin/python3

import sys


def safe_print_integer_err(value):
    """Prints an integer using the format method.

    If a ValueError or TypeError occurs during the printing,
    an error message is displayed on the standard error stream.

    Args:
        value (int): The integer to print.

    Returns:
        If the printing is successful - True.
        Otherwise - False.
    """
    try:
        print("{:d}".format(value))
        return True
    except (TypeError, ValueError):
        print("Exception: {}".format(sys.exc_info()[1]), file=sys.stderr)
        return False
