#!/usr/bin/python3
"""
Defines a class MyList that inherits from list and
adds a print_sorted method.
"""


class MyList(list):
    """
    MyList class that inherits from list.
    Provides a method to print the list in sorted order.
    """

    def print_sorted(self):
        """Prints the list, but sorted in ascending order."""
        print(sorted(self))
