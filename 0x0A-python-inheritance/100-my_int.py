#!/usr/bin/python3
"""
Module defining MyInt class inheriting from int.
"""

class MyInt(int):
    """
    MyInt class inheriting from int.
    """

    def __eq__(self, other):
        """
        Overrides the equality operator.

        Args:
        - other: The other object to compare.

        Returns:
        - True if not equal, False otherwise.
        """
        return super().__ne__(other)

    def __ne__(self, other):
        """
        Overrides the not equal operator.

        Args:
        - other: The other object to compare.

        Returns:
        - True if equal, False otherwise.
        """
        return super().__eq__(other)

# Example usage
if __name__ == "__main__":
    my_i = MyInt(3)
    print(my_i)
    print(my_i == 3)
    print(my_i != 3)

