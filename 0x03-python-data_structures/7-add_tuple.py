#!/usr/bin/python3
# addTuple

def add_tuple(tuple_a=(), tuple_b=()):
    """Tuples Addition"""
    a = len(tuple_a)
    b = len(tuple_b)
    return ((tuple_a[0] if a > 0 else 0) + (tuple_b[0] if b > 0 else 0),
            (tuple_a[1] if a > 1 else 0) + (tuple_b[1] if b > 1 else 0))
