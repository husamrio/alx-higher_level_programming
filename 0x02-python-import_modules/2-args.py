#!/usr/bin/python3
if __name__ == "__main__":
    """Outputs the no. of lists of arguments."""
    from sys import argv
    userin = argv[1:]
    size = len(userin)
    argument_string = "arguments" if size != 1 else "argument"
    punctuation = "." if size == 0 else ":"

    print(f"{size} {argument_string}{punctuation}")

    for idx, arg in enumerate(userin, start=0):
        print(f"{idx}: {arg}")
