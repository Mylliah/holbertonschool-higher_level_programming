### Task 0 : 
        Write a function that reads a text file (`UTF8`) and prints it to stdout:
        - Prototype: `def read_file(filename="")`:
        - You must use the `with` statement
        - You don’t need to manage `file permission` or `file doesn't exist` exceptions.
        - You are not allowed to import any module
program [0-read_file.py](https://github.com/Mylliah/holbertonschool-higher_level_programming/blob/main/python-input_output/0-read_file.py)

### Task 1 :
        Write a function that writes a string to a text file (`UTF8`) and returns the number of characters written:
        - Prototype: `def write_file(filename="", text="")`:
        - You must use the `with` statement
        - You don’t need to manage file permission exceptions.
        - Your function should create the file if doesn’t exist.
        - Your function should overwrite the content of the file if it already exists.
        - You are not allowed to import any module
program [1-write_file.py](https://github.com/Mylliah/holbertonschool-higher_level_programming/blob/main/python-input_output/1-write_file.py)


### Task 2 :
        Write a function that appends a string at the end of a text file (`UTF8`) and returns the number of characters added:
        - Prototype: `def append_write(filename="", text=""):`
        - If the file doesn’t exist, it should be created
        - You must use the `with` statement
        - You don’t need to manage `file permission` or `file doesn't exist` exceptions.
        - You are not allowed to import any module
program [2-append_write.py](https://github.com/Mylliah/holbertonschool-higher_level_programming)


### Task 3 :
        Write a function that returns the JSON representation of an object (string):
        - Prototype: `def to_json_string(my_obj):`
        - You don’t need to manage exceptions if the object can’t be serialized.
program [3-to_json_string.py](https://github.com/Mylliah/holbertonschool-higher_level_programming/blob/main/python-input_output/3-to_json_string.py)


### Task 4 :
        Write a function that returns an object (Python data structure) represented by a JSON string:
        - Prototype: `def from_json_string(my_str):`
        - You don’t need to manage exceptions if the JSON string doesn’t represent an object.
program [4-from_json_string.py](https://github.com/Mylliah/holbertonschool-higher_level_programming/blob/main/python-input_output/4-from_json_string.py)


### Task 5 :
        Write a function that writes an Object to a text file, using a JSON representation:
        - Prototype: `def save_to_json_file(my_obj, filename):`
        - You must use the `with` statement
        - You don’t need to manage exceptions if the object can’t be serialized.
        - You don’t need to manage file permission exceptions.
program [5-save_to_json_file.py](https://github.com/Mylliah/holbertonschool-higher_level_programming/blob/main/python-input_output/5-save_to_json_file.py)


### Task 6 :
        Write a function that creates an Object from a “JSON file”:
        - Prototype: `def load_from_json_file(filename):`
        - You must use the `with` statement
        - You don’t need to manage exceptions if the JSON string doesn’t represent an object.
        - You don’t need to manage file permissions / exceptions.
program [6-load_from_json_file.py](https://github.com/Mylliah/holbertonschool-higher_level_programming/blob/main/python-input_output/6-load_from_json_file.py)


### Task 7 :
        Write a script that adds all arguments to a Python list, and then save them to a file:
        - You must use your function `save_to_json_file` from `5-save_to_json_file.py`
        - You must use your function `load_from_json_file` from `6-load_from_json_file.py`
        - The list must be saved as a JSON representation in a file named `add_item.json`
        - If the file doesn’t exist, it should be created
        - You don’t need to manage file permissions / exceptions.
program [7-add_item.py](https://github.com/Mylliah/holbertonschool-higher_level_programming/blob/main/python-input_output/7-add_item.py)


### Task 8 :
        Write a function that returns the dictionary description with simple data structure (list, dictionary, string, integer and boolean) for JSON serialization of an object:
        - Prototype: `def class_to_json(obj):`
        - `obj` is an instance of a Class
        - All attributes of the `obj` Class are serializable: list, dictionary, string, integer and boolean
        - You are not allowed to import any module
program [8-class_to_json.py](https://github.com/Mylliah/holbertonschool-higher_level_programming/blob/main/python-input_output/8-class_to_json.py)


### Task 9 :
        Write a class `Student` that defines a student by:        
        - Public instance attributes:
                - `first_name`
                - `last_name`
                - `age`
        - Instantiation with `first_name`, `last_name` and `age`: `def __init__(self, first_name, last_name, age):`
        - Public method `def to_json(self):` that retrieves a dictionary representation of a `Student` instance (same as `8-class_to_json.py`)
        - You are not allowed to import any module
program [9-student.py](https://github.com/Mylliah/holbertonschool-higher_level_programming/blob/main/python-input_output/9-student.py)


### Task 10 :
        Write a class `Student` that defines a student by: (based on `9-student.py`)
        - Public instance attributes:
                - `first_name`
                - `last_name`
                - `age`
        - Instantiation with `first_name`, `last_name` and `age`: `def __init__(self, first_name, last_name, age):`
        - Public method `def to_json(self, attrs=None):` that retrieves a dictionary representation of a `Student` instance (same as `8-class_to_json.py`):
        - If `attrs` is a list of strings, only attribute names contained in this list must be retrieved.
        - Otherwise, all attributes must be retrieved
        - You are not allowed to import any module
program [10-student.py](https://github.com/Mylliah/holbertonschool-higher_level_programming/blob/main/python-input_output/10-student.py)


### Task 11 :
        prev + :
        - Public method `def reload_from_json(self, json):` that replaces all attributes of the `Student` instance:
                - You can assume `json` will always be a dictionary
                - A dictionary key will be the public attribute name
                - A dictionary value will be the value of the public attribute
program [11-student.py] (https://github.com/Mylliah/holbertonschool-higher_level_programming/blob/main/python-input_output/11-student.py)


### Task 12 :
        Technical interview preparation:
        - You are not allowed to google anything
        - Whiteboard first
        Create a function def pascal_triangle(n): that returns a list of lists of integers representing the Pascal’s triangle of n:
        - Returns an empty list if n <= 0
        - You can assume n will be always an integer
        - You are not allowed to import any module
program [12-pascal_triangle.py](https://github.com/Mylliah/holbertonschool-higher_level_programming/blob/main/python-input_output/12-pascal_triangle.py)
