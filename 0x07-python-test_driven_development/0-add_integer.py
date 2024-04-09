#!/usr/bin/python3
def add_integer(a, b=98):
    """returns the integer addition of a and b.
    raises:
    TypeError: if either a not b is a number
    """
    if not (isinstance(a, int) and not isinstance(a, float)):
        TypeError("a must be an integer")
        if (not isinstance(b, int) and not isinstance(b, float)):
            TypeError("b must be an integer")
            return (int(a) + int(b))
