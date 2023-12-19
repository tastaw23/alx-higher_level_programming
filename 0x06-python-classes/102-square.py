#!/usr/bin/python3
"""Define a class Square."""


class Square:
    """Represent a square."""

    def __init__(self, size=0):
        """Initialize a new square.
        Args:
            size (float or int): The size of the new square.
        """
        self.size = size

    @property
    def size(self):
        """Get/set the current size of the square."""
        return self.__size

    @size.setter
    def size(self, value):
        if not isinstance(value, (float, int)):
            raise TypeError("size must be a number")
        elif value < 0:
            raise ValueError("size must be >= 0")
        self.__size = value

    def area(self):
        """Return the current area of the square."""
        return self.__size * self.__size

    def __eq__(self, other):
        """Equality comparison."""
        return self.area() == other.area()

    def __ne__(self, other):
        """Inequality comparison."""
        return self.area() != other.area()

    def __lt__(self, other):
        """Less than comparison."""
        return self.area() < other.area()

    def __le__(self, other):
        """Less than or equal to comparison."""
        return self.area() <= other.area()

    def __gt__(self, other):
        """Greater than comparison."""
        return self.area() > other.area()

    def __ge__(self, other):
        """Greater than or equal to comparison."""
        return self.area() >= other.area()
###
