#!/usr/bin/python3
def only_diff_elements(set_1, set_2):
    diff = set()
    for elem in set_1:
        if elem not in set_2:
            diff.add(elem)
    for elem in set_2:
        if elem not in set_1:
            diff.add(elem)
    return diff
