#!/usr/bin/python3

class MyList(list):
    """
    MyList class inherits from the list class and adds a print_sorted method.
    """

    def print_sorted(self):
        """
        Public instance method to print the list in sorted (ascending order).

        This method modifies the behavior of the built-in print function.

        Example:
        >>> my_list = MyList([1, 4, 2, 3, 5])
        >>> print(my_list)
        [1, 4, 2, 3, 5]
        >>> my_list.print_sorted()
        [1, 2, 3, 4, 5]
        """
        print(sorted(self))

# Example usage
if __name__ == "__main__":
    my_list = MyList()
    my_list.append(1)
    my_list.append(4)
    my_list.append(2)
    my_list.append(3)
    my_list.append(5)

    print(my_list)
    my_list.print_sorted()
    print(my_list)

