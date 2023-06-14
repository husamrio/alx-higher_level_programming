#!/usr/bin/python3
def uniq_add(my_list=[]):
    total = 0
    i = 0
    unique_list = list(set(my_list))
    while i < len(unique_list):
        total += unique_list[i]
        i += 1
    return total
