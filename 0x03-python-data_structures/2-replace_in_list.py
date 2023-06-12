#!/usr/bin/python3
#replaceInList

def replace_in_list(my_list, idx, element):
    """Replaces an element of a list withian a specific location"""
    if idx < len(my_list) and idx > -1:
        my_list[idx] = element
        return my_list
    return my_list
