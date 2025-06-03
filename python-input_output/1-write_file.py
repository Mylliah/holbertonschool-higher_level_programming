#!/usr/bin/python3
"""
This module provides a function to write a string to a text file
and return the number of characters written.
"""


def write_file(filename="", text=""):
    """
    Write a string to a text file and return the number of characters written.
    """
    with open(filename, "w", encoding="utf-8") as f:
        return f.write(text)
