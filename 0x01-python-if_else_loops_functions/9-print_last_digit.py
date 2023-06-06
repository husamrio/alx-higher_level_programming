#!/usr/bin/python3
def print_last_digit(number):
    print(f"{(abs(number) % 10):d}", end="")
    return abs(number) % 10

#    if num < 0:
#        num = num * -1
#    print("{}".format(num % 10), end='')
#    return (num % 10)
