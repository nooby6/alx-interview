#!/usr/bin/python3
import sys

def print_solution(board):
    """
    Prints the solution as a list of lists, where each list contains the row and column index
    of a queen in the solution.
    """
    solution = []
    for row in range(len(board)):
        solution.append([row, board[row]])
    print(solution)

def is_safe(board, row, col):
    """
    Checks if placing a queen on board[row][col] is safe from attacks by other queens.
    """
    for i in range(row):
        # Check if there’s a queen in the same column or diagonals
        if board[i] == col or \
           board[i] - i == col - row or \
           board[i] + i == col + row:
            return False
    return True

def solve_nqueens(board, row, N):
    """
    Uses backtracking to place queens on the board and print all possible solutions.
    """
    if row == N:
        print_solution(board)
        return

    for col in range(N):
        if is_safe(board, row, col):
            board[row] = col
            solve_nqueens(board, row + 1, N)
            # Backtrack: reset the position
            board[row] = -1

def main():
    # Validate the number of command-line arguments
    if len(sys.argv) != 2:
        print("Usage: nqueens N")
        sys.exit(1)

    try:
        N = int(sys.argv[1])
    except ValueError:
        print("N must be a number")
        sys.exit(1)

    # Validate that N is at least 4
    if N < 4:
        print("N must be at least 4")
        sys.exit(1)

    # Initialize the board with -1 (indicating no queen in any row initially)
    board = [-1] * N
    solve_nqueens(board, 0, N)

if __name__ == "__main__":
    main()
