#!/usr/bin/python3

if __name__ == "__main__":
    """Print to the display the number of and list of arguments."""
    from sys import argv

    count = len(argv) - 1
    argument_string = "arguments" if count != 1 else "argument"
    punctuation = "." if count == 0 else ":"

    print(f"{count} {argument_string}{punctuation}")

    for i, arg in enumerate(argv[1:], start=1):
        print(f"{i}: {arg}")
