#!/usr/bin/python3
"""This module defines a text-indentation function."""


def text_indentation(text):
    """Print text with two new lines after each '.', '?', and ':'.

    Args:
        text (string): The text to print.
    Raises:
        TypeError: If text is not a string.
    """
    if not isinstance(text, str):
        raise TypeError("text must be a string")

    # Define characters that trigger a new line
    new_line_chars = ['.', '?', ':']

    # Iterate the text and print lines with 2 new lines
    current_line = ""
    for char in text:
        current_line += char
        if char in new_line_chars:
            # strip any tabs and spaces from the beggining to end
            print(current_line.strip())
            print()  # Print 2 new lines
            current_line = ""

    # Print the last line if there is any text remaining
    if current_line:
        print(current_line.strip())
