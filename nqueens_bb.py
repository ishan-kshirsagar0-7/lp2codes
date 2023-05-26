def is_safe(board, row, col):
    for i in range(row):
        if board[i] == col or board[i] - i == col - row or board[i] + i == col + row:
            return False
    return True

def solve_n_queens(n):
    def branch_and_bound(board, row, remaining_rows):
        if row == n:
            result.append(board[:])
            return

        for col in range(n):
            if is_safe(board, row, col):
                board[row] = col
                conflicts = sum(board[i] == board[row] or board[i] - i == board[row] - row or board[i] + i == board[row] + row for i in range(row))
                if conflicts < remaining_rows:
                    branch_and_bound(board, row + 1, remaining_rows - 1)

    result = []
    board = [-1] * n
    branch_and_bound(board, 0, n)
    return result

n = 4  # Number of queens
solutions = solve_n_queens(n)
for placement in solutions:
    for row in placement:
        for col in range(len(placement)):
            print('Q ' if row == col else '. ', end='')
        print()
    print()