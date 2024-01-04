#!/usr/bin/python3
import sys


def is_safe(board, row, col, N):
    """
    Check if it's safe to place a queen at a given position on the board.

    Args:
    - board: The chessboard representation.
    - row: The row index to check.
    - col: The column index to check.
    - N: The size of the chessboard.

    Returns:
    - True if it's safe to place a queen, False otherwise.
    """
    # Check this row on the left side
    for i in range(col):
        if board[row][i] == 1:
            return False

    # Check upper diagonal on the left side
    for i, j in zip(range(row, -1, -1), range(col, -1, -1)):
        if board[i][j] == 1:
            return False

    # Check lower diagonal on the left side
    for i, j in zip(range(row, N, 1), range(col, -1, -1)):
        if board[i][j] == 1:
            return False

    return True


def solve_nqueens_util(board, col, N, solutions):
    """
    Recursive utility function to solve the N Queens problem.

    Args:
    - board: The chessboard representation.
    - col: The current column to consider.
    - N: The size of the chessboard.
    - solutions: A list to store the solutions.

    Returns:
    - None
    """
    if col == N:
        solutions.append([[i, board[i].index(1)] for i in range(N)])
        return

    for i in range(N):
        if is_safe(board, i, col, N):
            board[i][col] = 1
            solve_nqueens_util(board, col + 1, N, solutions)
            board[i][col] = 0


def solve_nqueens(N):
    """
    Solve the N Queens problem and print all solutions.

    Args:
    - N: The size of the chessboard.

    Returns:
    - None
    """
    if not isinstance(N, int):
        print("N must be a number")
        sys.exit(1)

    if N < 4:
        print("N must be at least 4")
        sys.exit(1)

    board = [[0] * N for _ in range(N)]
    solutions = []
    solve_nqueens_util(board, 0, N, solutions)

    for solution in solutions:
        print(solution)


if __name__ == "__main__":
    if len(sys.argv) != 2:
        print("Usage: {} N".format(sys.argv[0]))
        sys.exit(1)

    try:
        N = int(sys.argv[1])
        solve_nqueens(N)
    except ValueError:
        print("N must be a number")
        sys.exit(1)
###
