#!/usr/bin/env python3

"""Module defining the VerboseList class with verbose list operations."""


class VerboseList(list):
    """A list subclass that prints messages on operations."""

    def append(self, item):
        """Append item to the list and print a message."""
        super().append(item)
        print(f"Added [{item}] to the list.")

    def extend(self, item):
        """Extend list by appending elements from the iterable and
        print a message."""
        super().extend(item)
        print(f"Extended the list with [{len(item)}] items.")

    def remove(self, item):
        """Remove first occurrence of item and print a message."""
        print(f"Removed [{item}] from the list.")
        super().remove(item)

    def pop(self, item=-1):
        """Remove and return item at index (default last) and
        print a message."""
        print(f"Popped [{self[item]}] from the list.")
        return super().pop(item)
