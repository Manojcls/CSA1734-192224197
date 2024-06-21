import heapq
def manhattan(board, goal):
    return sum(abs(r - gr) + abs(c - gc)
               for r, row in enumerate(board)
               for c, val in enumerate(row) if val
               for gr, grow in enumerate(goal)
               for gc, gval in enumerate(grow) if gval == val)
def neighbors(board):
    r, c = next((r, c) for r, row in enumerate(board) for c, val in enumerate(row) if not val)
    swaps = [(-1, 0), (1, 0), (0, -1), (0, 1)]
    for dr, dc in swaps:
        nr, nc = r + dr, c + dc
        if 0 <= nr < len(board) and 0 <= nc < len(board[0]):
            new_board = [row[:] for row in board]
            new_board[r][c], new_board[nr][nc] = new_board[nr][nc], new_board[r][c]
            yield new_board
def a_star(start, goal):
    start_heuristic = manhattan(start, goal)
    heap = [(start_heuristic, start)]
    costs = {str(start): 0}
    parents = {str(start): None}   
    while heap:
        _, current = heapq.heappop(heap)
        if current == goal:
            path = []
            while current:
                path.append(current)
                current = parents[str(current)]
            return path[::-1]
        for neighbor in neighbors(current):
            new_cost = costs[str(current)] + 1
            if str(neighbor) not in costs or new_cost < costs[str(neighbor)]:
                costs[str(neighbor)] = new_cost
                priority = new_cost + manhattan(neighbor, goal)
                heapq.heappush(heap, (priority, neighbor))
                parents[str(neighbor)] = current
start_board = [
    [3, 5, 1],
    [4, 0, 2],
    [7, 8, 6]
]
goal_board = [
    [1, 2, 3],
    [4, 5, 6],
    [7, 8, 0]
]
path = a_star(start_board, goal_board)
for step in path:
    for row in step:
        print(row)
    print()
