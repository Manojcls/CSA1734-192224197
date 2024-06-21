def solve_n_queens(n):
    solutions = []
    board = [-1] * n
    def is_valid(row, col):
        for r in range(row):
            if board[r] == col or \
               board[r] - r == col - row or \
               board[r] + r == col + row:
                return False
        return True
    def solve(row):
        if row == n:
            solutions.append(board[:])
        else:
            for col in range(n):
                if is_valid(row, col):
                    board[row] = col
                    solve(row + 1)
    solve(0)
    return solutions

def print_solutions(solutions):
    for solution in solutions:
        for row in solution:
            print(' '.join('Q' if i == row else '.' for i in range(len(solution))))
        print()
        break;
solutions = solve_n_queens(8)
print_solutions(solutions)
