#!/usr/bin/python3
# -*- coding: utf-8 -*-
"""
This module containt a single class named Square
"""


class Square:
    """
    This is the empty class named Square.
    The empy block is identified using the pass statement.
    The private instance atribute size is defined.
    Added size validaition throught the to if conditions
    """

    __size = 0

    def __init__(self, size=0):
        self._Square__size = size
        if not type(size) is int:
            raise TypeError("size must be an integer")
        if size < 0:
            raise ValueError("size must be >= 0")

    def area(self):
        return self._Square__size**2


my_square_1 = Square(3)
print("Area: {}".format(my_square_1.area()))

try:
    print(my_square_1.size)
except Exception as e:
    print(e)

try:
    print(my_square_1.__size)
except Exception as e:
    print(e)

my_square_2 = Square(5)
print("Area: {}".format(my_square_2.area()))
