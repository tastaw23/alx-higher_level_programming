#!/usr/bin/python3

def divisible_by_2(my_list=[]):
    """Check if each element in the list is divisible by 2."""
    return [num % 2 == 0 for num in my_list]

