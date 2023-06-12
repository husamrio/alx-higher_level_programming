#!/usr/bin/python3
# multipleReturns

def multiple_returns(sentence):
    """Returns length of string and 1st char"""
    return (len(sentence), sentence[0] if sentence else None)
