#!/usr/bin/python3
"""Module for reading and printing the contents of a text file."""


def read_file(filename=""):
    """Reads a text file (UTF8) and prints its content to stdout."""
    with open(filename, "r", encoding='utf-8') as f:
        print(f.read(), end="")
