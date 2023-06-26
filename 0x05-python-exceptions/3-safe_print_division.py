#!/usr/bin/python3

def safe_print_division(a, b):
    """Calculates the division of a by b and displays the result."""
    quot = None
    try:
        quot = a / b
    except (ZeroDivisionError, TypeError):
        pass
    finally:
        print("The division result is: {}".format(quot))
        return quot
