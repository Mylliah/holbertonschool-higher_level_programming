#!/usr/bin/env python3

def uppercase(str):
    alpha = ""
    for char in str:
        if 97 <= ord(char) <= 122:
            alpha += chr((ord(char)) - 32)
        else:
            alpha += char
    print(alpha, end="")
    print("")
