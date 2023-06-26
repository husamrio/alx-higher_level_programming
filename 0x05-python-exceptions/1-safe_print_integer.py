#!/usr/bin/python3

def safe_print_integer(value):
    """Prints an integer value using the '{:d}'.format() method.

    Args:
        value (int): The integer value to be printed.

    Returns:
        True if the integer value is successfully printed, False otherwise.
    """
    try:
        print("{:d}".format(value))
        return True
    except (TypeError, ValueError):
        return False
