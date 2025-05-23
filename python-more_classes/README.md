### Task 0 : 
        Write an empty class `Rectangle` that defines a rectangle:   
        - You are not allowed to import any module
program [0-rectangle.py]()

### Task 1 :
        Write a class `Rectangle` that defines a rectangle by: (based on `0-rectangle.py`)
        - Private instance attribute: `width`:
            - property `def width(self):` to retrieve it
            - property setter `def width(self, value):` to set it:
                - `width` must be an integer, otherwise raise a `TypeError` exception with the message `width must be an integer`
                - if `width` is less than `0`, raise a `ValueError` exception with the message `width must be >= 0`
        - Private instance attribute: `height`:
            - property `def height(self):` to retrieve it
            - property setter `def height(self, value):` to set it:
                - `height` must be an integer, otherwise raise a `TypeError` exception with the message `height must be an integer`
                - if `height` is less than `0`, raise a `ValueError` exception with the message `height must be >= 0`
        - Instantiation with optional `width` and `height`: `def __init__(self, width=0, height=0):`
        - You are not allowed to import any module
program [1-rectangle.py]()

### Task 2 :
        Preview + :
        - Public instance method: `def area(self):` that returns the rectangle area
        - Public instance method: `def perimeter(self):` that returns the rectangle perimeter:
                - if `width` or `height` is equal to `0`, perimeter is equal to `0`
program [2-rectangle.py](https://github.com/Mylliah/holbertonschool-higher_level_programming/blob/main/python-more_classes/2-rectangle.py)

### Task 3 :
        Preview + :
        - `print()` and `str()` should print the rectangle with the character `#`:
program [3-rectangle.py](https://github.com/Mylliah/holbertonschool-higher_level_programming/blob/main/python-more_classes/3-rectangle.py)

### Task 4 :
        Preview + :
        - `repr()` should return a string representation of the rectangle to be able to recreate a new instance by using `eval()`
program [4-rectangle.py](https://github.com/Mylliah/holbertonschool-higher_level_programming/blob/main/python-more_classes/4-rectangle.py)

### Task 5 :
        Preview + :
        - Print the message `Bye rectangle...` (`...` being 3 dots not ellipsis) when an instance of `Rectangle` is deleted
program [5-rectangle.py](https://github.com/Mylliah/holbertonschool-higher_level_programming/blob/main/python-more_classes/5-rectangle.py)

### Task 6 :
        Preview + :
        - Public class attribute `number_of_instances:`
                - Initialized to `0`
                - Incremented during each new instance instantiation
                - Decremented during each instance deletion
program [6-rectangle.py](https://github.com/Mylliah/holbertonschool-higher_level_programming/blob/main/python-more_classes/6-rectangle.py)

### Task 7 :
        Preview + :
        Public class attribute `print_symbol:`
                - Initialized to `#`
                - Used as symbol for string representation
                - Can be any type
program [7-rectangle.py](https://github.com/Mylliah/holbertonschool-higher_level_programming/blob/main/python-more_classes/7-rectangle.py)

### Task 8 :
        Preview + :
        Static method `def bigger_or_equal(rect_1, rect_2)`: that returns the biggest rectangle based on the area
                -`rect_1` must be an instance of `Rectangle`, otherwise raise a `TypeError` exception with the message `rect_1 must be an instance of Rectangle`
                -`rect_2` must be an instance of `Rectangle`, otherwise raise a `TypeError` exception with the message `rect_2 must be an instance of Rectangle`
                - Returns `rect_1` if both have the same area value
program [8-rectangle.py](https://github.com/Mylliah/holbertonschool-higher_level_programming/blob/main/python-more_classes/8-rectangle.py)

### Task 9 :
        Preview + :
        - Class method `def square(cls, size=0):` that returns a new Rectangle instance with `width == height == size`
program [9-rectangle.py](https://github.com/Mylliah/holbertonschool-higher_level_programming/blob/main/python-more_classes/9-rectangle.py)
