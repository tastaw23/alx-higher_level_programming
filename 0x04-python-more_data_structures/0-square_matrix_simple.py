#!/usr/bin/python3

def square_matrix_simple(matrix=[]):
    """Computes the square value of all integers in a matrix."""
    result_matrix = [list(map(lambda x: x**2, row)) for row in matrix]
    return result_matrix
#######

