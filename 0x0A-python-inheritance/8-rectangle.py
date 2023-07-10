#!/usr/bin/python3
Rectangle = __import__('8-rectangle').Rectangle

# Create a new Rectangle object with width 3 and height 5
r = Rectangle(3, 5)

# Print the string representation of the Rectangle object
print(r)
# Print the list of available attributes and methods of the Rectangle object
print(dir(r))

# Attempt to print the width and height of the Rectangle object
try:
    print("Rectangle: {} - {}".format(r.width, r.height))
except Exception as e:
    # If an exception occurs, print the exception class name and message
    print("[{}] {}".format(e.__class__.__name__, e))

# Attempt to create a new Rectangle object with invalid arguments
try:
    r2 = Rectangle(4, True)
except Exception as e:
    # If an exception occurs, print the exception class name and message
    print("[{}] {}".format(e.__class__.__name__, e))
