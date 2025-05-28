#!/usr/bin/python3
"""
Provides a function to check if an object is an instance of a class
or an instance of a class that inherited from the specified class.
"""


def is_kind_of_class(obj, a_class):
    """Check if obj is an instance of a_class or a subclass thereof."""
    if isinstance(obj, a_class):
        return True
    else:
        return False
