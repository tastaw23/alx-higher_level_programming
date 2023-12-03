#!/usr/bin/python3

def add_tuple(tuple_a=(), tuple_b=()):
    # Use the first two elements of each tuple, filling with 0 if needed
    a = tuple_a + (0, 0)
    b = tuple_b + (0, 0)

    # Perform addition for each corresponding element
    result = (a[0] + b[0], a[1] + b[1])
    return result
######
