#!/usr/bin/python3

"""JSON-to-object function is define."""
import json


def from_json_string(my_str):
    """This return Python object representation of a JSON string."""
    return json.loads(my_str)
