#!/usr/bin/python3
def print_sorted_dictionary(a_dictionary):
    keys = sorted(list(a_dictionary.keys()))
    i = 0
    while i < len(keys):
        print(f"{keys[i]}: {a_dictionary[keys[i]]}")
        i += 1
