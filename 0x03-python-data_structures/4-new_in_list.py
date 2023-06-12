#!/usr/bin/python3
# new in list

def new_in_list(my_list, idx, element):
    """Supplant an element in a copied list at a specific pos."""
    new_list = my_list.copy()
    if idx >= 0 and idx < len(my_list):
        new_list[idx] = element
    return new_list
