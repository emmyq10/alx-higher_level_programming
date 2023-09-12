#!/usr/bin/python3
"""Python class-to-JSON function is define."""


def class_to_json(obj):
    """This return the dictionary description with simple data structure."""
    return obj.__dict__
