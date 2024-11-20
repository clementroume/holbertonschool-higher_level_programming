#!/usr/bin/python3
"""Module to draw a square - Step 4"""


class Square:
    """Square class"""

    def __init__(self, size=0):
        """initialization method"""
        self._Square__size = size

    @property
    def size(self):
        """getter method"""
        return self._Square__size

    @size.setter
    def size(self, value):
        """setter method"""
        if not type(value) is int:
            raise TypeError("size must be an integer")
        if value < 0:
            raise ValueError("size must be >= 0")
        self._Square__size = value

    def area(self):
        """area method"""
        return self._Square__size**2

    def my_print(self):
        """printing method"""
        if self._Square__size == 0:
            print()
        else:
            for i in range(self._Square__size):
                print("#" * self._Square__size)
