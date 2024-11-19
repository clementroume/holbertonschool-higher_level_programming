#!/usr/bin/python3
def uppercase(str):
    i = 0
    while i < len(str):
        char = str[i]
        print(chr(ord(char) - 32) if "a" <= char <= "z" else char, end="")
        i += 1
    print()


uppercase("best")
uppercase("Best School 98 Battery street")
