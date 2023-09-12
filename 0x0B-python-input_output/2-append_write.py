#!/usr/bin/python3


"""
append_write function is define
"""


def append_write(filename="", text=""):
    """
    This appends a string at the end of a text file (UTF8) and returns the
    number of characters added

    Arguments:
        filename {str} -- [The name of the file]
        text {str} -- [The text to append]
    """
    with open(filename, "a", encoding="utf-8") as f:
        return f.write(text)
