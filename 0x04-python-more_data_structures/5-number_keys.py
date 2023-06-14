#!/usr/bin/python3
def number_keys(a_dictionary):
    count = 0
    keys = list(a_dictionary.keys())
    i = 0
    while i < len(keys):
        count += 1
        i += 1
    return count
