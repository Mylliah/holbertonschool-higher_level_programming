### Task 0 :
        Write a function that adds 2 integers.
        - Prototype: 'def add_integer(a, b=98):'
        - 'a' and 'b' must be integers or floats, otherwise raise a 'TypeError' exception with the message 'a must be an integer' or 'b must be an integer'
        - 'a' and 'b' must be first casted to integers if they are float
        - Returns an integer: the addition of 'a' and 'b'
        - You are not allowed to import any module
program [0-add_integer.py](https://github.com/Mylliah/holbertonschool-higher_level_programming/blob/main/python-test_driven_development/0-add_integer.py)
program [tests/0-add_integer.txt](https://github.com/Mylliah/holbertonschool-higher_level_programming/blob/main/python-test_driven_development/tests/0-add_integer.txt)

### Task 1 : 
        Write a function that divides all elements of a matrix.
        - Prototype: 'def matrix_divided(matrix, div):'
        - 'matrix' must be a list of lists of integers or floats, otherwise raise a 'TypeError' exception with the message matrix must be a 'matrix (list of lists) of integers/floats'
        - Each row of the 'matrix' must be of the same size, otherwise raise a 'TypeError' exception with the message 'Each row of the matrix must have the same size'
        - 'div' must be a number (integer or float), otherwise raise a 'TypeError' exception with the message 'div must be a number'
        - 'div' can’t be equal to '0', otherwise raise a 'ZeroDivisionError' exception with the message 'division by zero'
        - All elements of the matrix should be divided by 'div', rounded to 2 decimal places
        - Returns a new matrix
        - You are not allowed to import any module
program [2-matrix_divided.py](https://github.com/Mylliah/holbertonschool-higher_level_programming/blob/main/python-test_driven_development/2-matrix_divided.py)
program [2-matrix_divided.py](https://github.com/Mylliah/holbertonschool-higher_level_programming/blob/main/python-test_driven_development/tests/2-matrix_divided.txt)

### Task 2 :
        Write a function that prints 'My name is <first name> <last name>'
        - Prototype: 'def say_my_name(first_name, last_name=""):'
        - 'first_name' and 'last_name' must be strings otherwise, raise a 'TypeError' exception with the message 'first_name must be a string' or 'last_name must be a string'
        - You are not allowed to import any module
program [3-say_my_name.py](https://github.com/Mylliah/holbertonschool-higher_level_programming/blob/main/python-test_driven_development/3-say_my_name.py)
program [tests/3-say_my_name.txt](https://github.com/Mylliah/holbertonschool-higher_level_programming/blob/main/python-test_driven_development/tests/3-say_my_name.txt)

### Task 3 : 
        Write a function that prints a square with the character '#'.
        - Prototype: 'def print_square(size):'
        - 'size' is the size length of the square
        - 'size' must be an integer, otherwise raise a 'TypeError' exception with the message 'size must be an integer'
        - if 'size' is less than '0', raise a 'ValueError' exception with the message 'size must be >= 0'
        - if 'size' is a float and is less than 0, raise a 'TypeError' exception with the message 'size must be an integer'
        - You are not allowed to import any module
program [4-print_square.py](https://github.com/Mylliah/holbertonschool-higher_level_programming/blob/main/python-test_driven_development/4-print_square.py)
program [tests/4-print_square.txt](https://github.com/Mylliah/holbertonschool-higher_level_programming/blob/main/python-test_driven_development/tests/4-print_square.txt)

### Task 4 :
        Write a function that prints a text with 2 new lines after each of these characters: ., ? and :
        - Prototype: 'def text_indentation(text):'
        - 'text' must be a string, otherwise raise a 'TypeError' exception with the message 'text must be a string'
        - There should be no space at the beginning or at the end of each printed line
        - You are not allowed to import any module
program [5-text_indentation.py](https://github.com/Mylliah/holbertonschool-higher_level_programming/blob/main/python-test_driven_development/5-text_indentation.py)
program [tests/5-text_indentation.txt](https://github.com/Mylliah/holbertonschool-higher_level_programming/blob/main/python-test_driven_development/tests/5-text_indentation.txt)

### Task 5 :
        Since the beginning you have been creating “Interactive tests”. For this exercise, you will add Unittests.
        In this task, you will write unittests for the function 'def max_integer(list=[]):'.
        - Your test file should be inside a folder 'tests'
        - You have to use the 'unittest module'
        - Your test file should be python files (extension: '.py')
        - Your test file should be executed by using this command: 
        'python3 -m unittest tests.6-max_integer_test'
        - All tests you make must be passable by the function below
        - We strongly encourage you to work together on test cases, so that you don’t miss any edge case
program [tests/6-max_integer_test.py](https://github.com/Mylliah/holbertonschool-higher_level_programming/blob/main/python-test_driven_development/tests/6-max_integer_test.py)
