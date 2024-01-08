#!/usr/bin/python3
"""
Module defining Square class inheriting from Rectangle.
"""

Rectangle = __import__('9-rectangle').Rectangle

class Square(Rectangle):
    """
    Square class inheriting from Rectangle.
    """

    def __init__(self, size):
        """
        Initializes a Square instance.

        Args:
        - size: The size of the square.
        """
        self.integer_validator("size", size)
        self.__size = size
        super().__init__(size, size)

    def __str__(self):
        """
        Returns a string representation of the square.

        Returns:
        - A string in the format "[Square] <size>/<size>"
        """
        return "[Square] {}/{}".format(self.__size, self.__size)

# Example usage
if __name__ == "__main__":
    s = Square(13)

    print(s)
    print(s.area())

