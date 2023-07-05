import sys


def init_board(n):
    """Initialize an `n`x`n` sized chessboard with empty cells."""
    return [[' ' for _ in range(n)] for _ in range(n)]


def get_solution(board):
    """Return the list of lists representation of a solved chessboard."""
    return [[r, c] for r, row in enumerate(board) for c, cell in
            enumerate(row) if cell == 'Q']


def xout(board, row, col):
    """Mark spots on a chessboard where non-attacking
    queens can no longer be placed."""
    n = len(board)
    for r in range(n):
        if board[r][col] == ' ':
            board[r][col] = 'x'
    for i in range(1, n - max(row, col)):
        if board[row + i][col + i] == ' ':
            board[row + i][col + i] = 'x'
    for i in range(1, min(row, col) + 1):
        if board[row - i][col - i] == ' ':
            board[row - i][col - i] = 'x'
    for i in range(1, min(row + 1, n - col)):
        if board[row - i][col + i] == ' ':
            board[row - i][col + i] = 'x'
    for i in range(1, min(n - row, col + 1)):
        if board[row + i][col - i] == ' ':
            board[row + i][col - i] = 'x'


def recursive_solve(board, row, queens, solutions):
    """Recursively solve an N-queens puzzle.

    Args:
        board (list): The current working chessboard.
        row (int): The current working row.
        queens (int): The current number of placed queens.
        solutions (list): A list of lists of solutions.
    Returns:
        solutions
    """
    n = len(board)
    if queens == n:
        solutions.append(get_solution(board))
        return solutions

    for col in range(n):
        if board[row][col] == ' ':
            tmp_board = [row[:] for row in board]
            tmp_board[row][col] = 'Q'
            xout(tmp_board, row, col)
            solutions = recursive_solve(tmp_board, row + 1,
                                        queens + 1, solutions)

    return solutions


if __name__ == "__main__":
    if len(sys.argv) != 2:
        print("Usage: nqueens.py N")
        sys.exit(1)
    if not sys.argv[1].isdigit():
        print("N must be a number")
        sys.exit(1)
    n = int(sys.argv[1])
    if n < 4:
        print("N must be at least 4")
        sys.exit(1)

    board = init_board(n)
    solutions = recursive_solve(board, 0, 0, [])
    for sol in solutions:
        print(sol)
