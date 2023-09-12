#!/usr/bin/python3
"""string-to-JSON function is define."""
import json


def to_json_string(my_obj):
    """This returns the JSON representation of a string object."""
    return json.dumps(my_obj)
