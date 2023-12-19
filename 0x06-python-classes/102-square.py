#!/usr/bin/python3


class Square:
    """Class that defines a square.

    Attributes:
        __size (number): The size of the square.
    """
    def __init__(self, size=0):
        """Initialization method for the Square class.

        Args:
            size (number, optional): The size of the square. Defaults to 0.
        """
        self.size = size

    @property
    def size(self):
        """Getter method for the size attribute."""
        return self.__size

    @size.setter
    def size(self, value):
        """Setter method for the size attribute.

        Args:
            value (number): The size value to set.

        Raises:
            TypeError: If value is not a number.
            ValueError: If value is less than 0.
        """
        if not isinstance(value, (int, float)):
            raise TypeError("size must be a number")
        elif value < 0:
            raise ValueError("size must be >= 0")
        else:
            self.__size = value

    def area(self):
        """Method to calculate and return the current square area."""
        return self.__size ** 2

    def __eq__(self, other):
        """Method to compare if two squares are equal in terms of area."""
        return self.area() == other.area()

    def __ne__(self, other):
        """Method compare if 2squares are not equal in terms of area."""
        return self.area() != other.area()

    def __lt__(self, other):
        """Method compare if area of 1square is less area of other."""
        return self.area() < other.area()

    def __le__(self, other):
        """Method compare ifarea of 1square is less/equal to area other."""
        return self.area() <= other.area()

    def __gt__(self, other):
        """Method compare if area of 1square is greater to area other."""
        return self.area() > other.area()

    def __ge__(self, other):
        """Method compare if area of 1square is greater/equal to area other."""
        return self.area() >= other.area()


if __name__ == "__main__":
    s_5 = Square(5)
    s_6 = Square(6)

    if s_5 < s_6:
        print("Square 5 < Square 6")
    if s_5 <= s_6:
        print("Square 5 <= Square 6")
    if s_5 == s_6:
        print("Square 5 == Square 6")
    if s_5 != s_6:
        print("Square 5 != Square 6")
    if s_5 > s_6:
        print("Square 5 > Square 6")
    if s_5 >= s_6:
        print("Square 5 >= Square 6")
##
