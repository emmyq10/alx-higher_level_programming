#!/usr/bin/python3

"""
is_kind_of_class
"""

def is_kind_of_class(obj, a_class):
    """
    This checks if an object is an instance of
    a class that inherited from, the specified class

    Args:
        obj (any): object to be checked
        a_class (any): class to be checked against

    Returns:
        bool: True if an object is an instance of
        instance of a class that inherited from, the specified class
    """
    if isinstance(obj, a_class):
        return True
    return False
