"""Counting grains on a chess board."""

def square(number):
    """Function that counts the number of grains on a square."""
    if number < 1 or number > 64:
        raise ValueError("square must be between 1 and 64")
    return 2**(number-1)

def total():
    """Function that returns total number of grains on a board."""
    counter = 0
    for num in range(1,65):
        counter += square(num)
    return counter
    
