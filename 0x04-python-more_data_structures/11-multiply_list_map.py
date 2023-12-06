#!/usr/bin/python3

def multiply_list_map(my_list, factor):
    """
    Multiply each element in the list by the given factor.

    Parameters:
    - my_list (list): The input list of numbers.
    - factor (int): The multiplication factor.

    Returns:
    - list: A new list with each element multiplied by the factor.
    """
    return list(map(lambda x: x * factor, my_list))

#
