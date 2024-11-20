#!/usr/bin/python3
"""Module to draw a square - Step 3"""


class Square:
    """Square class"""

    def __init__(self, size=0):
        """initialization method"""
        self._Square__size = size
        if not type(size) is int:
            raise TypeError("size must be an integer")
        if size < 0:
            raise ValueError("size must be >= 0")

    def area(self):
        """area method"""
        return self._Square__size**2
