#!/usr/bin/python3

"""
This module provides a function to create an object from a JSON file.
"""

import json


def load_from_json_file(filename):
    """Creates an object from a JSON file."""
    with open(filename, "r") as f:
        return json.load(f)
