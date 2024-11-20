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
    Size validation throught the two if conditions
    Area calculation throught area(self) function
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
