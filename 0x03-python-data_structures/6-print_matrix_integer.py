#!/usr/bin/python3

def print_matrix_integer(matrix=[[]]):
    if not matrix:
        print()
        return

    for row in matrix:
        for num in row:
            print("{:d}".format(num), end=" ")
            if num != row[-1]:
                print(end=" ")
        print()

# Example usage
if __name__ == "__main__":
    matrix = [
        [1, 2, 3],
        [4, 5, 6],
        [7, 8, 9]
    ]
    print_matrix_integer(matrix)
    print("--")
    print_matrix_integer()

