#!/usr/bin/python3

class Square:
    """Class that defines a square.

    Attributes:
        __size (int): The size of the square.
    """
    def __init__(self, size):
        """Initialization method for the Square class.

        Args:
            size (int): The size of the square.
        """
        self.__size = size
#!/usr/bin/python3
Square = __import__('1-square').Square

my_square = Square(3)
print(type(my_square))
print(my_square.__dict__)

try:
    print(my_square.size)
except Exception as e:
    print(e)

try:
    print(my_square.__size)
except Exception as e:
    print(e)
##
