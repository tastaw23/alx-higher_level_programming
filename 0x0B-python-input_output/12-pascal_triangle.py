#!/usr/bin/python3

def pascal_triangle(n):
    """
    Generate Pascal's Triangle up to the nth row.

    Args:
        n (int): Number of rows to generate.

    Returns:
        list of lists: Pascal's Triangle up to the nth row.
    """
    if n <= 0:
        return []

    triangle = [[1]]

    for i in range(1, n):
        row = [1]
        for j in range(1, i):
            row.append(triangle[i-1][j-1] + triangle[i-1][j])
        row.append(1)
        triangle.append(row)

    return triangle

if __name__ == "__main__":
    # Test the pascal_triangle function
    def print_triangle(triangle):
        """
        Print the triangle.
        """
        for row in triangle:
            print("[{}]".format(",".join([str(x) for x in row])))

    print_triangle(pascal_triangle(5))

