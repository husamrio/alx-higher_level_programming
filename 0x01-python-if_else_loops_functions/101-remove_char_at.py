#!/usr/bin/python3
def remove_char_at(str, n):
    if n >= 0:
        return str[:n] + str[n+1:]
    else:
        return str
 # Remove a character from a string at a given index.
    #    Args:
    #        str (str): The string to remove the character from.
    #        n (int): The index of the character to remove.
    #    Returns:
    #        str: The resulting string after removing the character.
