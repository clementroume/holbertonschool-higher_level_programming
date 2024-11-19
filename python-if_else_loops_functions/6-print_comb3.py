#!/usr/bin/python3
a = 0
while a <= 8:
    b = a + 1
    while b <= 9:
        if a < 8:
            print("{}{}".format(a, b), end=", ")
        else:
            print("{}{}".format(a, b), end="\n")
        b += 1
    a += 1
