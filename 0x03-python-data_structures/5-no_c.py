#!/usr/bin/python3
def no_c(my_string):
    """Remove all characters c and C from a string."""
    return "".join(c for c in my_string if c not in "Cc")
