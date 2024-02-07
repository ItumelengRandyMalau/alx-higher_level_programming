#!/usr/bin/python3
""" Defines a function that appends a string
    at the end a file (UTF8)"""


def append_write(filename="", text=""):
    """appends a string to a text file.
        Args:
            filename(str): The name of the file
            text(str): The text to append.
        Returns:
            The lenth of characters added.
    """
    with open(filename, 'a', encoding='utf-8') as f:
        f.write(text)
        return len(text)
