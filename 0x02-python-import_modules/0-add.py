#!/usr/bin/python3

if__name__ == "__main__":
    """Print the sum of 1 and 2."""
# import the add function from add_0.py file
from add_0 import add

# define variables a and b
a = 1
b = 2

# call the add function and print the result using string formatting
print("{} + {} = {}".format(a, b, add(a, b)))
