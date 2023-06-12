#!/usr/bin/python3
# divisibleBy2

def divisible_by_2(my_list=[]):
    """Identify and find all multiples of 2 ina list"""
    result = []
    for i in my_list:
        result.append(i % 2 == 0)
    return result
