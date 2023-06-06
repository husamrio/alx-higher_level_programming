#!/usr/bin/python3
for ascii_value in range(ord('a'), ord('z') + 1):
    if ascii_value != ord('q') and ascii_value != ord('e'):
        print('{}'.format(chr(ascii_value)), end='')
