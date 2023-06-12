#!/usr/bin/python3
# deleteAt

def delete_at(my_list=[], idx=0):
    """Deletes item at specific position in a list"""
    result = []
    for i, item in enumerate(my_list):
        if i != idx:
            result.append(item)
    return result
