#!/usr/bin/python3

"""Module for from_json_string function."""

import json


def from_json_string(my_str):
    """Return the Python object represented by a JSON string."""
    return json.loads(my_str)
