def is_safe(board, row, col):
    for i in range(row):
        if board[i] == col or board[i] - i == col - row or board[i] + i == col + row:
            return False
    return True

def solve_n_queens(n):
    def backtrack(board, row):
        if row == n:
            result.append(board[:])
            return

        for col in range(n):
            if is_safe(board, row, col):
                board[row] = col
                backtrack(board, row + 1)

    result = []
    board = [-1] * n
    backtrack(board, 0)
    return result

def print_solutions(solutions):
    for placement in solutions:
        for row in placement:
            for col in range(len(placement)):
                print('Q ' if row == col else '. ', end='')
            print()
        print()

n = 4  # Number of queens
solutions = solve_n_queens(n)
print_solutions(solutions)