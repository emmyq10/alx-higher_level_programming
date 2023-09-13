#!/usr/bin/python3

"""
is_same_class
"""

def is_same_class(obj, a_class):
    """
    This checks if an object is exactly an instance of the specified class

    Args:
        obj (any): object to be checked
        a_class (any): class to be checked against

    Returns:
        bool: True if object is exactly an instance of the specified class
    """
    if type(obj) == a_class:
        return True
    return False
