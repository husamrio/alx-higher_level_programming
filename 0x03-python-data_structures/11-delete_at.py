#!/usr/bin/python3
# deleteAt

def delete_at(my_list=[], idx=0):
    """Deletes item at specific position in a list"""
    if idx >= 0 and idx < len(my_list):
        my_list.pop(idx)
    return my_list
