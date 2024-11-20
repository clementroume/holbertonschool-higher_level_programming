#!/usr/bin/python3
"""Module to draw a square - Step 4"""


class Square:
    """Square class"""

    def __init__(self, size=0, position=(0, 0)):
        """initialization method"""
        self.size = size
        self.position = position

    @property
    def size(self):
        """size getter method"""
        return self.__size

    @size.setter
    def size(self, value):
        """size setter method"""
        if not type(value) is int:
            raise TypeError("size must be an integer")
        if value < 0:
            raise ValueError("size must be >= 0")
        self.__size = value

    @property
    def position(self):
        """position getter method"""
        return self.__position

    @position.setter
    def position(self, value):
        if not isinstance(value, tuple):
            raise TypeError("position must be a tuple of 2 positive integers")
        if len(value) != 2:
            raise TypeError("position must be a tuple of 2 positive integers")
        if not all(isinstance(x, int) and x >= 0 for x in value):
            raise TypeError("position must be a tuple of 2 positive integers")
        self.__position = value

    def area(self):
        """area method"""
        return self.__size**2

    def my_print(self):
        """printing method"""
        if self.size == 0:
            print()
        else:
            a, b = self.position
            for i in range(b):
                print("")
            for j in range(self.size):
                print(" " * a, end="")
                print("#" * self.size)


my_square_3 = Square(3, (0, 1))
my_square_3.my_print()
