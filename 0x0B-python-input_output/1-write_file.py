#!/usr/bin/python3
"""file-writing function is define."""


def write_file(filename="", text=""):
    """Write a string to a UTF8 text file.

    Args:
        filename (str): The file to write.
        text (str): Text to write to the file.
    Returns:
        The number of characters written to the file.
    """
    with open(filename, "w", encoding="utf-8") as f:
        return f.write(text)
