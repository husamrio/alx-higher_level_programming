#!/usr/bin/python3
# print_reversedListInteger

def print_reversed_list_integer(my_list=[]):
    """Print to the display all integers of a list in reverse order."""
    if my_list is not None and isinstance(my_list, list):
        for i in my_list[::-1]:
            print("{:d}".format(i))
