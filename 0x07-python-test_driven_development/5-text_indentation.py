#!/usr/bin/python3
"""
5-text_indentation module
prints text with 2 new lines after each ".", "?", and ":" i.e method in this
Input is a string
"""


def text_indentation(text):
    """
    Prints text with 2 new lines after each ".", "?", and ":"
    """
    if not isinstance(text, str):
        raise TypeError("text must be a string")

    text = text.replace('.', '.\n\n')
    text = text.replace('?', '?\n\n')
    text = text.replace(':', ':\n\n')

    print('\n'.join(line.strip() for line in text.split('\n')), end="")
