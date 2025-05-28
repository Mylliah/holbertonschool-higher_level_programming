### Task 0 :
    Background:
    In object-oriented programming, Abstract Base Classes (ABCs) ensure that derived classes implement specific methods from the base class. This provides a blueprint for creating and structuring derived classes. Python’s `ABC` package facilitates the creation of abstract base classes.

    Objective:
    1. Create an abstract class named `Animal` using the `ABC` package. This class should have an abstract method called `sound`.
    2. Create two subclasses of `Animal`: `Dog` and `Cat`. Implement the `sound` method in each subclass to return the strings “Bark” and “Meow” respectively.

    Instructions:
    1. Setting up the Abstract Class:
        - Import the necessary components from the `abc` module.
        - Define the `Animal` class, ensuring it inherits from `ABC` to mark it as abstract.
        - Inside the `Animal` class, declare an abstract method named `sound` using the `@abstractmethod` decorator.
    2. Implementing the Subclasses:
        - Create a subclass named `Dog` that inherits from the `Animal` class.
            Implement the `sound` method in the `Dog` class to return the string “Bark”.
        - Similarly, create a subclass named `Cat` that also inherits from the `Animal` class.
            Implement the `sound` method in the `Cat` class to return the string “Meow”.
 
    Hints:
    * The abstract method in the base class doesn’t have a body. You need to provide the implementation in the subclasses.
    * If you try to instantiate a class that hasn’t implemented all of its abstract methods, Python will raise a `TypeError`.
program [task_00_abc.py]()

