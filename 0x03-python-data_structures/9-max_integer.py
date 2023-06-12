#!/usr/bin/python3
# max Integer

def max_integer(my_list=[]):
    """Find the biggest int of a list"""
    if not my_list:
        return None
    big = my_list[0]
    i = 1
    while i < len(my_list):
        if my_list[i] > big:
            big = my_list[i]
        i += 1
    return big
