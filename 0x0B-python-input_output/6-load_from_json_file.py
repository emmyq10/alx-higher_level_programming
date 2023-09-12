#!/usr/bin/python3
"""JSON file-reading function is define."""
import json


def load_from_json_file(filename):
    """This create a Python object from a JSON file."""
    with open(filename) as f:
        return json.load(f)
