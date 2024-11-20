#!/usr/bin/python3
"""0. Integers addition"""


def add_integer(a, b=98):
    """add integer function"""
    if not isinstance(a, (int, float)):
        raise TypeError("a must be an integer")
    if not isinstance(b, (int, float)):
        raise TypeError("b must be an integer")
    return int(a + b)
