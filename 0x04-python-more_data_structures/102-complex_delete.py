#!/usr/bin/python3
def complex_delete(a_dictionary, value):
    keys = list(a_dictionary.keys())
    i = 0
    while i < len(keys):
        if a_dictionary[keys[i]] == value:
            del a_dictionary[keys[i]]
        i += 1
    return a_dictionary
