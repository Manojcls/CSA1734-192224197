from itertools import permutations
def is_solution(perm):
    s, e, n, d, m, o, r, y = perm
    send = 1000 * s + 100 * e + 10 * n + d
    more = 1000 * m + 100 * o + 10 * r + e
    money = 10000 * m + 1000 * o + 100 * n + 10 * e + y
    return send + more == money
def solve_cryptarithmetic():
    letters = 'SENDMORY'
    digits = range(10)
    
    for perm in permutations(digits, len(letters)):
        s, e, n, d, m, o, r, y = perm
        if s == 0 or m == 0: 
            continue
        if is_solution(perm):
            return {'S': s, 'E': e, 'N': n, 'D': d, 'M': m, 'O': o, 'R': r, 'Y': y}
solution = solve_cryptarithmetic()
if solution:
    print("Solution found:")
    print(solution)
else:
    print("No solution exists.")
