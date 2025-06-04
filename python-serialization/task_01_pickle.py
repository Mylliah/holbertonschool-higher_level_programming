#!/usr/bin/env python3

"""Module for serializing and deserializing a custom object using pickle."""


import pickle


class CustomObject:
    """Custom object with name, age, and is_student attributes."""
    def __init__(self, name, age, is_student):
        """Initialize a CustomObject instance."""
        self.name = name
        self.age = age
        self.is_student = is_student

    def serialize(self, filename):
        """Serialize the object to a file using pickle."""
        try:
            with open(filename, "wb") as f:
                return pickle.dump(self, f)
        except Exception:
            return None

    @classmethod
    def deserialize(cls, filename):
        """Deserialize a CustomObject instance from a file."""
        try:
            with open(filename, "rb") as f:
                return pickle.load(f)
        except Exception:
            return None

    def display(self):
        """Display the object's attributes."""
        print(f"Name: {self.name}")
        print(f"Age: {self.age}")
        print(f"Is student: {self.is_student}")
