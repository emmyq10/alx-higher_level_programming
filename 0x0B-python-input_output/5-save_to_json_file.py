#!/usr/bin/python3
"""JSON file-writing function is define."""
import json


def save_to_json_file(my_obj, filename):
    """This write an object to a text file, using a JSON representation."""
    with open(filename, "w") as f:
        json.dump(my_obj, f)
