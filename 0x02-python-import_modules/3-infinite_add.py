#!/usr/bin/python3

if __name__ == "__main__":
    """Print to the diplay the addition of all arguments."""
    import sys

    total = 0
    if len(sys.argv) > 1:
        for arg in sys.argv[1:]:
            total += int(arg)
    print(f"{total}")
