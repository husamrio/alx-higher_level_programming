#!/usr/bin/python3
# deleteAt

def delete_at(my_list=[], idx=0):
    """Deletes item at specific position in a list"""
    if idx >= 0 and idx < len(my_list):
        my_list[:] = my_list[:idx] + my_list[idx + 1:]
    return my_list
