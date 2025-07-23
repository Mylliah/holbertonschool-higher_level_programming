### Task 0 : 

What function would you use to print the type of an object?
Write the name of the function in the file, without ().

program [0-answer.txt](https://github.com/Mylliah/holbertonschool-higher_level_programming/blob/main/python-everything_is_object/0-answer.txt)


### Task 1 :

How do you get the variable identifier (which is the memory address in the CPython implementation)?
Write the name of the function in the file, without ().

program [1-answer.txt](https://github.com/Mylliah/holbertonschool-higher_level_programming/blob/main/python-everything_is_object/1-answer.txt)

### Task 2 :

In the following code, do a and b point to the same object? Answer with Yes or No.
```
>>> a = 89
>>> b = 100
```
program [2-answer.txt](https://github.com/Mylliah/holbertonschool-higher_level_programming/blob/main/python-everything_is_object/2-answer.txt)


### Task 3 :

In the following code, do a and b point to the same object? Answer with Yes or No.
```
>>> a = 89
>>> b = 89
```
programme [3-answer.txt](https://github.com/Mylliah/holbertonschool-higher_level_programming/blob/main/python-everything_is_object/3-answer.txt)


### Task 4 :

In the following code, do a and b point to the same object? Answer with Yes or No.
```
>>> a = 89
>>> b = a
```
program [4-answer.txt](https://github.com/Mylliah/holbertonschool-higher_level_programming/blob/main/python-everything_is_object/4-answer.txt)


### Task 5 :

In the following code, do a and b point to the same object? Answer with Yes or No.
```
>>> a = 89
>>> b = a + 1
```

program [5-answer.txt](https://github.com/Mylliah/holbertonschool-higher_level_programming/blob/main/python-everything_is_object/5-answer.txt)


### Task 6 :

What do these 3 lines print?
```
>>> s1 = "Best School"
>>> s2 = s1
>>> print(s1 == s2)
```

program [6-answer.txt](https://github.com/Mylliah/holbertonschool-higher_level_programming/blob/main/python-everything_is_object/6-answer.txt)


### Task 7 :

What do these 3 lines print?
```
>>> s1 = "Best"
>>> s2 = s1
>>> print(s1 is s2)
```

program [7-answer.txt](https://github.com/Mylliah/holbertonschool-higher_level_programming/blob/main/python-everything_is_object/7-answer.txt)


### Task 8 :

What do these 3 lines print?
```
>>> s1 = "Best School"
>>> s2 = "Best School"
>>> print(s1 == s2)
```

program [8-answer.txt](https://github.com/Mylliah/holbertonschool-higher_level_programming/blob/main/python-everything_is_object/8-answer.txt)


### Task 9 :

What do these 3 lines print?
```
>>> s1 = "Best School"
>>> s2 = "Best School"
>>> print(s1 is s2)
```

program [9-answer.txt](https://github.com/Mylliah/holbertonschool-higher_level_programming/blob/main/python-everything_is_object/9-answer.txt)


### Task 10 :

What do these 3 lines print?
```
>>> l1 = [1, 2, 3]
>>> l2 = [1, 2, 3] 
>>> print(l1 == l2)
```

program [10-answer.txt](https://github.com/Mylliah/holbertonschool-higher_level_programming/blob/main/python-everything_is_object/10-answer.txt)


### Task 11 :

What do these 3 lines print?
```
>>> l1 = [1, 2, 3]
>>> l2 = [1, 2, 3] 
>>> print(l1 is l2)
```

program [11-answer.txt](https://github.com/Mylliah/holbertonschool-higher_level_programming/blob/main/python-everything_is_object/11-answer.txt)


### Task 12 :

What do these 3 lines print?
```
>>> l1 = [1, 2, 3]
>>> l2 = l1
>>> print(l1 == l2)
```

program [12-answer.txt](https://github.com/Mylliah/holbertonschool-higher_level_programming/blob/main/python-everything_is_object/12-answer.txt)


### Task 13 :

What do these 3 lines print?
```
>>> l1 = [1, 2, 3]
>>> l2 = l1
>>> print(l1 is l2)
```

program [13-answer.txt](https://github.com/Mylliah/holbertonschool-higher_level_programming/blob/main/python-everything_is_object/13-answer.txt)


### Task 14 :

What does this script print?
```
l1 = [1, 2, 3]
l2 = l1
l1.append(4)
print(l2)         
```

program [14-answer.txt](https://github.com/Mylliah/holbertonschool-higher_level_programming/blob/main/python-everything_is_object/14-answer.txt)


### Task 15 :

What does this script print?
```
l1 = [1, 2, 3]
l2 = l1
l1 = l1 + [4]
print(l2)
```

program [15-answer.txt](https://github.com/Mylliah/holbertonschool-higher_level_programming/blob/main/python-everything_is_object/15-answer.txt)


### Task 16 :

What does this script print?
```
def increment(n):
    n += 1

a = 1
increment(a)
print(a)
```

program [16-answer.txt](https://github.com/Mylliah/holbertonschool-higher_level_programming/blob/main/python-everything_is_object/16-answer.txt)


### Task 17 :

What does this script print?
```
def increment(n):
    n.append(4)

l = [1, 2, 3]
increment(l)
print(l)
```

program [17-answer.txt](https://github.com/Mylliah/holbertonschool-higher_level_programming/blob/main/python-everything_is_object/17-answer.txt)


### Task 18 :

What does this script print?
```
def assign_value(n, v):
    n = v

l1 = [1, 2, 3]
l2 = [4, 5, 6]
assign_value(l1, l2)
print(l1)
```

program [18-answer.txt](https://github.com/Mylliah/holbertonschool-higher_level_programming/blob/main/python-everything_is_object/18-answer.txt)


### Task 19 :

Write a function def copy_list(a_list): that returns a copy of a list.
- The input list can contain any type of objects
- Your file should be maximum 3-line long (no documentation needed)
- You are not allowed to import any module
```
guillaume@ubuntu:~/$ ./19-main.py
[1, 2, 3]
[1, 2, 3]
[1, 2, 3]
True
False
guillaume@ubuntu:~/$ wc -l 19-copy_list.py 
3 19-copy_list.py
guillaume@ubuntu:~/$ 
```

program [19-copy_list.py](https://github.com/Mylliah/holbertonschool-higher_level_programming/blob/main/python-everything_is_object/19-copy_list.py)


### Task 20 :

```
a = ()
```
Is a a tuple? Answer with Yes or No.

program [20-answer.txt](https://github.com/Mylliah/holbertonschool-higher_level_programming/blob/main/python-everything_is_object/20-answer.txt)


### Task 21 :

```
a = (1, 2)
```
Is a a tuple? Answer with Yes or No.

program [21-answer.txt](https://github.com/Mylliah/holbertonschool-higher_level_programming/blob/main/python-everything_is_object/21-answer.txt)


### Task 22 :

```
a = (1)
```
Is a a tuple? Answer with Yes or No.

program [22-answer.txt](https://github.com/Mylliah/holbertonschool-higher_level_programming/blob/main/python-everything_is_object/22-answer.txt)


### Task 23 :

```
a = (1, )
```
Is a a tuple? Answer with Yes or No.

program [23-answer.txt](https://github.com/Mylliah/holbertonschool-higher_level_programming/blob/main/python-everything_is_object/23-answer.txt)


### Task 24 :

What does this script print?
```
a = (1)
b = (1)
a is b
```

program [24-answer.txt](https://github.com/Mylliah/holbertonschool-higher_level_programming/blob/main/python-everything_is_object/24-answer.txt)


### Task 25 :

What does this script print?
```
a = (1, 2)
b = (1, 2)
a is b
```

program [25-answer.txt](https://github.com/Mylliah/holbertonschool-higher_level_programming/blob/main/python-everything_is_object/25-answer.txt)


### Task 26 :

What does this script print?
```
a = ()
b = ()
a is b
```

program [26-answer.txt](https://github.com/Mylliah/holbertonschool-higher_level_programming/blob/main/python-everything_is_object/26-answer.txt)


### Task 27 :

```
>>> id(a)
139926795932424
>>> a
[1, 2, 3, 4]
>>> a = a + [5]
>>> id(a)
```
Will the last line of this script print 139926795932424? Answer with Yes or No.

program [27-answer.txt](https://github.com/Mylliah/holbertonschool-higher_level_programming/blob/main/python-everything_is_object/27-answer.txt)


### Task 28 :

```
>>> a
[1, 2, 3]
>>> id (a)
139926795932424
>>> a += [4]
>>> id(a)
```
Will the last line of this script print 139926795932424? Answer with Yes or No.

program [28-answer.txt](https://github.com/Mylliah/holbertonschool-higher_level_programming/blob/main/python-everything_is_object/28-answer.txt)
