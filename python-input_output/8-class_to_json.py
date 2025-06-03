#!/usr/bin/python3

"""
Function to get the dictionary description of an object for JSON serialization.
"""


def class_to_json(obj):
    """
    Return the dictionary description of an object.
    """
    return obj.__dict__
