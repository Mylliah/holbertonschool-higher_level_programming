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

    text = text.strip()
    
    i = 0
    length = len(text)
    while i < length:

        start = i

        while i < length and text[i] not in ['.', '?', ':']:
            i += 1

        line = text[start:i].strip()
        if line:
            print(line)

        if i == length:
            break
        
        print(text[i])
        print()
        
        i += 1
        while i < length and text[i] == ' ':
            i += 1
