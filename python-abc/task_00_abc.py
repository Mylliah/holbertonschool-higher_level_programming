#!/usr/bin/env python3

"""Module demonstrating abstract base classes with Animal, Dog, and Cat."""

from abc import ABC, abstractmethod


class Animal(ABC):
    """Abstract base class for animals."""
    @abstractmethod
    def sound(self):
        """Return the sound made by the animal."""
        pass


class Dog(Animal):
    """Dog class inheriting from Animal."""
    def sound(self):
        return "Bark"


class Cat(Animal):
    """Cat class inheriting from Animal."""
    def sound(self):
        """Return the sound made by a cat."""
        return "Meow"
