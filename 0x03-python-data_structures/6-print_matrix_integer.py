#!/usr/bin/python3

def print_matrix_integer(matrix=[[]]):
    if not matrix:
        return

    for i, row in enumerate(matrix):
        for j, num in enumerate(row):
            print("{:d}".format(num), end=" ")
            if j < len(row) - 1:
                print(end=" ")
        if i < len(matrix) - 1:
            print()

