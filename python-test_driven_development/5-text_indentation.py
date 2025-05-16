#!/usr/bin/python3
"""
This module provides a function to print a text with 2 new lines after
each of these characters: ., ? and :.
"""


def text_indentation(txt):
    """
    Prints a text with 2 new lines after each of these characters: ., ? and :

    Args:
        txt (str): The text to print.

    Raises:
        TypeError: If txt is not a string.
    """
    if type(txt) is not str:
        raise TypeError("text must be a string")

    segment = ""
    for char in txt:
        if char in ('.', '?', ':'):
            segment += char
            print(segment.strip())
            print()
            segment = ""
        elif char == '\n':
            if segment.strip():
                print(segment.strip())
            print()
            segment = ""
        else:
            segment += char

    if segment.strip():
        print(segment.strip(), end="")
