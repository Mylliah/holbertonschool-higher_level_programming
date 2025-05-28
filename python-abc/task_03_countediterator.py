#!/usr/bin/env python3

"""Module providing the CountedIterator class."""


class CountedIterator:
    """Iterator that counts the number of items iterated."""

    def __init__(self, iterable):
        """Initialize with an iterable and set counter to zero."""
        self.iterator = iter(iterable)
        self.counter = 0

    def __iter__(self):
        """Return the iterator itself."""
        return self

    def __next__(self):
        """Return the next item and increment the counter."""
        item = next(self.iterator)
        self.counter += 1
        return item

    def get_count(self):
        """Return the number of items iterated so far."""
        return self.counter
