#!/usr/bin/python3
def uppercase(str):
    for j in str:
        if (ord(j) >= ord('a')) and (ord(j) <= ord('z')):
            j = chr(ord(j)-ord('a')+ord('A'))
        print("{}".format(j), end="")
    print()
