#!/usr/bin/python3

def safe_print_list(my_list=[], x=0):
    """Print a specific number of elements from a list,
    handling index errors gracefully.

    Args:
        my_list (list): The list to print elements from.
        x (int): The number of elements to print.

    Returns:
        int: The actual number of elements successfully printed.
    """
    count = 0
    try:
        for element in my_list[:x]:
            print("{}".format(element), end="")
            count += 1
        print()
        return count
    except IndexError:
        print()
        return count
