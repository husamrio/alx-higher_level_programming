#!/usr/bin/python3


def islower(c):
    """Check if a character is lowercase.

    Args:
        char (str): The character to check.

    Returns:
        bool: True if the character is lowercase, False otherwise.
    """
    return ord('a') <= ord(c) <= ord('z')
