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
program [task_00_abc.py](https://github.com/Mylliah/holbertonschool-higher_level_programming/blob/main/python-abc/task_00_abc.py)


### Task 1 :
    1. Create an abstract class named `Shape` with two abstract methods: `area` and `perimeter`.
    2. Implement two concrete classes: `Circle` and `Rectangle`, both inheriting from `Shape`. Each class should provide implementations for the `area` and `perimeter` methods.
    3. Write a standalone function named `shape_info` that accepts an object of type `Shape` (by duck typing) and prints its area and `perimeter`.
    4. Test the `shape_info` function with instances of both `Circle` and `Rectangle`.
    ---
    a. Shape Abstract Class:
        - Define an abstract class `Shape` using the `ABC` package.
        - Within `Shape`, declare two abstract methods: `area` and `perimeter`.
    b. Circle and Rectangle Classes:
        - Create a `Circle` class that inherits from `Shape`. The constructor `(__init__)` should accept a radius. Implement the `area` and `perimeter` methods.
        - Create a `Rectangle` class, also inheriting from `Shape`. Its constructor should accept the `width` and `height`. Implement the `area` and `perimeter` methods.
    c. shape_info Function:
        - Define a function named `shape_info` that takes a single argument.
        - Without explicitly checking the type of the argument, call its `area` and `perimeter` methods (relying on duck typing).
        - Print the `area` and `perimeter` of the shape passed to the function.
    d. Testing:
        - Instantiate a `Circle` and a `Rectangle`.
        - Pass each object to the `shape_info` function and observe the output.

Hints:
        While Python doesn’t enforce interfaces in the same way as statically-typed languages, abstract base classes provide a mechanism to ensure certain methods are implemented in subclasses.
        Duck typing in the `shape_info` function implies that you shouldn’t use `isinstance` checks. Instead, trust that the passed object adheres to the `Shape` interface.
program [task_01_duck_typing.py](https://github.com/Mylliah/holbertonschool-higher_level_programming/blob/main/python-abc/task_01_duck_typing.py)


### Task 2 :
        Create a class named `VerboseList` that extends the Python `list` class. This custom class should print a notification message every time an item is added (using the `append` or `extend` methods) or removed (using the `remove` or `pop` methods).
        1. Setting up the `VerboseList` Class:
            - Define a class `VerboseList` that inherits from the built-in `list` class.
            - Within `VerboseList`, override the methods that modify the list: `append`, `extend`, `remove`, and `pop`.
        2. Implementing Notifications:
            - For the `append` method: After adding the item to the list, print a message like “Added [item] to the list.”
            - For the `extend` method: After extending the list, print a message like “Extended the list with [x] items.” where [x] is the number of items added.
            - For the `remove` method: Before removing the item from the list, print a message like “Removed [item] from the list.”
            - For the `pop` method: Before popping the item from the list, print a message like “Popped [item] from the list.” If the index is not specified, default behavior is to pop the last item.
        3. Testing:
            - Instantiate a `VerboseList` object.
            - Test all the overridden methods (`append`, `extend`, `remove`, and `pop`) and ensure that the appropriate messages are printed for each operation.
Hints:
        Remember to call the original method of the `list` class using the `super()` function to ensure that the original functionality is retained. For example, for `append`: `super().append(item)`.
        Think about edge cases, such as trying to remove an item that doesn’t exist in the list.
program [task_02_verboselist.py](https://github.com/Mylliah/holbertonschool-higher_level_programming/blob/main/python-abc/task_02_verboselist.py)


### Task 3 :
        Create a class named `CountedIterator` that extends the built-in iterator obtained from the `iter` function. The `CountedIterator` should keep track of the number of items that have been iterated over. Specifically, you will need to override the `__next__` method to increment a counter each time an item is fetched.

        1. Setting up the `CountedIterator` Class:  
                - Define a class CountedIterator.
                - In the constructor (`__init__`), initialize two attributes: the iterator object (using the `iter` function) and a counter to track the number of items iterated.
                - Provide a method `get_count` to return the current value of the counter.
        2. Overriding the next Method:
                - Within the `CountedIterator` class, override the `__next__` method.
                - In this method, increment the counter each time the `__next__` method is called.
                - Fetch the next item from the original iterator and return it. If there are no items left to iterate, the method should raise the `StopIteration` exception.
        3. Testing:
                - Instantiate a `CountedIterator` object using a list or another iterable.
                - Iterate over items using a loop or manual calls to the `__next__` method.
                - Use the `get_count` method to retrieve and print the number of items that have been fetched.
Hints:
        Remember that the `__next__` method should raise a `StopIteration` exception when there are no more items to iterate, so ensure this behavior is retained in your overridden method.
        You can initialize the iterator object in the `CountedIterator` constructor using: `self.iterator = iter(some_iterable)`.
program [task_03_countediterator.py](https://github.com/Mylliah/holbertonschool-higher_level_programming/blob/main/python-abc/task_03_countediterator.py)


### Task 4 :
        Construct a `FlyingFish` class that inherits from both a `Fish` class and a `Bird` class. Within `FlyingFish`, override methods from both parents. The goal is to comprehend multiple inheritance and how Python determines method resolution order.
        1. Parent Classes Setup:
            - Create a `Fish` class with methods `swi` (which prints “The fish is swimming”) and `habitat` (which prints “The fish lives in water”).
            - Create a `Bird` class with methods `fly` (which prints “The bird is flying”) and `habitat` (which prints “The bird lives in the sky”).
        2. Implementing `FlyingFish`:
            - Construct a `FlyingFish` class that inherits from both Fish and `Bird`.
            - Override the `fly` method to print “The flying fish is soaring!”.
            - Override the `swim` method to print “The flying fish is swimming!”.
            - Override the `habitat` method to print “The flying fish lives both in water and the sky!”.
        3. Testing and MRO Exploration:
            - Instantiate an object of the `FlyingFish` class.
            - Call the `fly`, `swim`, and `habitat` methods and observe the outputs.
            - Use the `mro()` method or the `.__mro__` attribute on the `FlyingFish` class to investigate the method resolution order. For instance, `print(FlyingFish.mro())`.

Hints:
        Consider the order in which you list the parent classes when defining `FlyingFish`. It affects the method resolution order.
        While multiple inheritance can be a powerful tool, it should be used judiciously, as it can make the code more complex and harder to read.
program [task_04_flyingfish.py](https://github.com/Mylliah/holbertonschool-higher_level_programming/blob/main/python-abc/task_04_flyingfish.py)


### Task 5 :
        Design two mixin classes, `SwimMixin` and `FlyMixin`, each equipped with methods `swim` and `fly` respectively. Next, construct a class `Dragon` that inherits from both these mixins. Your aim is to show that a `Dragon` instance can both swim and fly.
        1. Creating Mixins:
            - Design a mixin called `SwimMixin` with a method `swim` that prints “The creature swims!”.
            - Design another mixin called `FlyMixin` with a method `fly` that prints “The creature flies!”.
        2. Implementing Dragon:
            - Construct a class named `Dragon` that inherits from both `SwimMixin` and `FlyMixin`.
            - Within the `Dragon` class, you can add additional methods or attributes if desired, such as `roar`, which could print “The dragon roars!”.
        3. Testing the Dragon’s Abilities:
            - Instantiate an object of the `Dragon` class named `draco`.
            - Demonstrate `draco`‘s abilities by calling the `swim`, `fly`, and (if implemented) `roar` methods.

Hints:
    While designing mixins, remember that they should be focused, providing a single piece of functionality. They shouldn’t be overly broad or try to manage too much behavior.
    Mixins allow for code reusability and can be combined in various ways to give objects different capabilities without setting up complex inheritance hierarchies.
program [task_05_dragon.py](https://github.com/Mylliah/holbertonschool-higher_level_programming/blob/main/python-abc/task_05_dragon.py)
