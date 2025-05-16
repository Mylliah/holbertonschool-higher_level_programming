#!/usr/bin/python3
"""
This module provides a function to print a text with 2 new lines after
each of these characters: ., ? and :.
"""


def text_indentation(text):
    """
    Prints a text with 2 new lines after each of these characters: ., ? and :

    Args:
        text (str): The text to print.

    Raises:
        TypeError: If text is not a string.
    """
    if not isinstance(text, str):
        raise TypeError("text must be a string")

    start = 0
    length = len(text)
    i = 0
    while i < length:
        while start < length and text[start] == " ":
            start += 1
        i = start
        while i < length and text[i] not in ".:?":
            i += 1
        if start < length:
            if i < length:
                print(text[start:i + 1].strip())
                print()
                start = i + 1
                i = start
            else:
                if text[start:].strip():
                    print(text[start:].strip())
                break
