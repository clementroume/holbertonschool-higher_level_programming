#!/usr/bin/python3
"""0. Integers addition"""


def add_integer(a, b=98):
    """add integer function"""
    if not (isinstance(a, int) or isinstance(a, float)):
        raise TypeError("a must be an integer")
    elif not (isinstance(b, int) or isinstance(b, float)):
        raise TypeError("b must be an integer")
    else:
        return a + b


if __name__ == "__main__":
    import doctest

    doctest.testmod()
