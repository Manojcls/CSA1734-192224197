from collections import deque
def water_jug_bfs(x, y, z):
    if z > max(x, y):
        return None
    visited = set()
    queue = deque([(0, 0)])  
    path = []
    while queue:
        a, b = queue.popleft()
        if (a, b) in visited:
            continue
        visited.add((a, b))
        path.append((a, b))
        if a == z or b == z or a + b == z:
            return path
        possible_moves = [
            (x, b),  
            (a, y),  
            (0, b),  
            (a, 0), 
            (a - min(a, y - b), b + min(a, y - b)),  
            (a + min(b, x - a), b - min(b, x - a))  
        ]
        for move in possible_moves:
            if move not in visited:
                queue.append(move)
    return None
x = 4  
y = 3
z = 2  
solution = water_jug_bfs(x, y, z)
if solution:
    print("Solution found:")
    for state in solution:
        print(state)
else:
    print("No solution exists.")
