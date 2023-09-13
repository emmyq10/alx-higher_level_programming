#!/usr/bin/python3


"""
This is a module for add_attribute method.
"""


def add_attribute(obj, name, value):
    """
    It Adds a new attribute to an object if it's possible.

    Args:
    - obj: Object to add the attribute to.
    - name (str): Name of attribute.
    - value: Value of the attribute.

    Raises:
    - TypeError: If attribute cannot be added.
    """

    if hasattr(obj, "__dict__"):
        setattr(obj, name, value)
    else:
        raise TypeError("can't add new attribute")
