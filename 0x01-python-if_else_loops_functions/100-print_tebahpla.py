#!/usr/bin/python3
for ascii_value in range(122, 96, -2):
    cs = f"{chr(ascii_value):s}{chr(ascii_value + ord('A') - ord('a') - 1):s}"
    print("{:s}".format(cs), end="")

# alternative method:
# for i in range(ord('z'), ord('a')-1, -1):
#    print('{:c}'.format(i) if i % 2 == 0 else chr(i-32), end='')
# Another alternative method:
# for i in range(0, 26):
#    c = ord('z') - i
#    if i % 2 == 1:
#        c = (chr(c - ord('a') + ord('A')))
#    else:
#        c = chr(c)
#    print("{}".format(c), end='')
