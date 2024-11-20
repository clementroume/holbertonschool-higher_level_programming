#!/usr/bin/python3
"""Module to draw a square - Step 4"""


class Square:
    """Square class"""

    def __init__(self, size=0, position=(0, 0)):
        """initialization method"""
        self._Square__size = size
        self._Square__position = position

    @property
    def size(self):
        """size getter method"""
        return self._Square__size

    @size.setter
    def size(self, value):
        """size setter method"""
        if not type(value) is int:
            raise TypeError("size must be an integer")
        if value < 0:
            raise ValueError("size must be >= 0")
        self._Square__size = value

    @property
    def position(self):
        """position getter method"""
        return self._Square__position

    @position.setter
    def position(self, value):
        if not (
            isinstance(value, tuple)
            and len(value) == 2
            and isinstance(value[0], int)
            and value[0] >= 0
            and isinstance(value[1], int)
            and value[1] >= 0
        ):
            raise TypeError("position must be a tuple of 2 positive integers")
        self._Square__position = value

    def area(self):
        """area method"""
        return self._Square__size**2

    def my_print(self):
        """printing method"""
        if self._Square__size == 0:
            print()
        else:
            a, b = self._Square__position
            for i in range(b):
                print("")
            for j in range(self._Square__size):
                print(" " * a, end="")
                print("#" * self._Square__size)
