#!/usr/bin/python3
"""Finds all solutions to the N-Queens puzzle.

Calculates every possible way to place N non-attacking
queens on an NxN chessboard.

Usage:
    $ ./101-nqueens.py N

N must be an integer of at least 4.

Variables:
    board (list): A list of lists representing the chessboard.
    solutions (list): A list of lists with solutions.

Solutions are in the format [[r, c], [r, c], [r, c], [r, c]], where `r`
and `c` are the row and column where a queen is placed on the chessboard.
"""
import sys


def init_board(n):

    """Set up a chessboard of size `n`x`n`, filled with 0's."""
    board = []
    [board.append([]) for j in range(n)]
    [row.append(' ') for j in range(n) for row in board]
    return (board)


def copy_board(board):
    """Create a deep copy of a chessboard."""
    if isinstance(board, list):
        return [copy_board(item) for item in board]
    return board


def find_solution(board):
    """Get the list of lists representation of a solved chessboard."""
    solution = []
    for row in range(len(board)):
        for col in range(len(board)):
            if board[row][col] == "Q":
                solution.append([row, col])
                break
    return solution


def mark_invalid_positions(board, row, col):
    """Mark invalid positions on a chessboard.

    All positions where non-attacking queens can no longer be placed
    are marked.

    Args:
        board (list): The current chessboard.
        row (int): The row where a queen was last placed.
        col (int): The column where a queen was last placed.
    """
    # Mark all forward positions as invalid
    for c in range(col + 1, len(board)):
        board[row][c] = "x"
    # Mark all backward positions as invalid
    for c in range(col - 1, -1, -1):
        board[row][c] = "x"
    # Marks all spots below
    for r in range(row + 1, len(board)):
        board[r][col] = "x"
    # Mark all spots above
    for r in range(row - 1, -1, -1):
        board[r][col] = "x"
    # Mark all out spots diagonally down to the right
    c = col + 1
    for r in range(row + 1, len(board)):
        if c >= len(board):
            break
        board[r][c] = "x"
        c += 1
    # Marks spot al diagonally up to the left
    c = col - 1
    for r in range(row - 1, -1, -1):
        if c < 0:
            break
        board[r][c]
        c -= 1
    # Marks out all the spots diagonally up to the right
    c = col + 1
    for r in range(row - 1, -1, -1):
        if c >= len(board):
            break
        board[r][c] = "x"
        c += 1
    # Marks out all the down to the left
    c = col - 1
    for r in range(row + 1, len(board)):
        if c < 0:
            break
        board[r][c] = "x"
        c -= 1


def solve_recursively(board, row, queens, solutions):
    """Solve the N-Queens puzzle recursively.

    Args:
        board (list): The current chessboard.
        row (int): The current row being worked on.
        queens (int): The current number of queens placed.
        solutions (list): A list of lists containing solutions.
    Returns:
        solutions
    """
    if queens == len(board):
        solutions.append(find_solution(board))
        return (solutions)

    for c in range(len(board)):
        if board[row][c] == " ":
            tmp_board = copy_board(board)
            tmp_board[row][c] = "Q"
            mark_invalid_positions(tmp_board, row, c)
            solutions = solve_recursively(tmp_board, row + 1,
                                          queens + 1, solutions)

    return (solutions)


if __name__ == "__main__":
    if len(sys.argv) != 2:
        print("Usage: nqueens N")
        sys.exit(1)
    if sys.argv[1].isdigit() is False:
        print("N must be a number")
        sys.exit(1)
    if int(sys.argv[1]) < 4:
        print("N must be at least 4")
        sys.exit(1)

    board = init_board(int(sys.argv[1]))
    solutions = solve_recursively(board, 0, 0, [])
    for sol in solutions:
        print(sol)
