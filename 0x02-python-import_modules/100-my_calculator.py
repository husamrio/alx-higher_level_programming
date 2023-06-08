#!/usr/bin/python3
from calculator_1 import add, sub, mul, div
import sys

if __name__ == "__main__":
    """Handle basic arithmetic operations."""
    if len(sys.argv) != 4:
        print("Usage:", sys.argv[0], "<a> <operator> <b>")
        sys.exit(1)

    ops = {"+": add, "-": sub, "*": mul, "/": div}
    op = sys.argv[2]
    if op not in ops:
        print("Unknown operator. Available operators: +, -, * and /")
        sys.exit(1)

    a = int(sys.argv[1])
    b = int(sys.argv[3])
    print("{:d} {:s} {:d} = {:d}".format(a, op, b, ops[op](a, b)))
