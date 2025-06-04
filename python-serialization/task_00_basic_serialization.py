#!/usr/bin/env python3

"""
Basic serialization module for saving and
loading Python dictionaries as JSON files.
"""


import json


def serialize_and_save_to_file(data, filename):
    """Serialize a dictionary and save it to a JSON file."""
    with open(filename, "w", encoding="utf-8") as file:
        return json.dump(data, file)


def load_and_deserialize(filename):
    """Load a dictionary from a JSON file."""
    with open(filename, "r", encoding="utf-8") as file:
        return json.load(file)
