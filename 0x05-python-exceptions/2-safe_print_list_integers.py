#!/usr/bin/python3

def safe_print_list_integers(my_list=[], x=0):
    """
    This function prints the first x elements of a list that are integers.
    It iterates through the list and uses a try-except
    block to handle non-integer elements.
    The number of successfully printed elements is returned as the result.
    """

    num_printed = 0
    for i in range(x):
        try:
            print("{:d}".format(my_list[i]), end="")
            num_printed += 1
        except (TypeError, ValueError):
            pass
    print("")
    return num_printed
