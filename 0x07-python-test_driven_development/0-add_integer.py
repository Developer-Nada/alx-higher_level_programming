def add_integer(a, b=98):
    """Returns the integer addition of a and b.
    
    Args:
    a (int): The first number.
    b (int, optional): The second number. Defaults to 98.
    
    Returns:
    int: The sum of a and b.
    
    Raises:
    TypeError: If either a or b is not a number.
    """
    if not isinstance(a, (int, float)):
        raise TypeError("a must be a number")
    if not isinstance(b, (int, float)):
        raise TypeError("b must be a number")
    
    return int(a) + int(b)
