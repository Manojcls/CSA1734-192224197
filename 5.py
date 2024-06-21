from collections import deque
def is_valid_state(state):
    m_left, c_left, m_right, c_right, boat = state
    if (m_left >= 0 and m_right >= 0 and c_left >= 0 and c_right >= 0 and 
        (m_left == 0 or m_left >= c_left) and (m_right == 0 or m_right >= c_right)):
        return True
    return False
def get_successors(state):
    m_left, c_left, m_right, c_right, boat = state
    successors = []
    if boat == 'left':
        moves = [(1, 0), (2, 0), (0, 1), (0, 2), (1, 1)]
        for m, c in moves:
            new_state = (m_left - m, c_left - c, m_right + m, c_right + c, 'right')
            if is_valid_state(new_state):
                successors.append(new_state)
    else:
        moves = [(1, 0), (2, 0), (0, 1), (0, 2), (1, 1)]
        for m, c in moves:
            new_state = (m_left + m, c_left + c, m_right - m, c_right - c, 'left')
            if is_valid_state(new_state):
                successors.append(new_state)
    return successors
def bfs(initial_state):
    queue = deque([(initial_state, [])])
    visited = set()
    visited.add(initial_state)
    
    while queue:
        (state, path) = queue.popleft()
        if state == (0, 0, 3, 3, 'right'):
            return path + [state]
        
        for successor in get_successors(state):
            if successor not in visited:
                visited.add(successor)
                queue.append((successor, path + [state]))
    return None
def print_solution(solution):
    if solution:
        for state in solution:
            print(state)
    else:
        print("No solution found.")
initial_state = (3, 3, 0, 0, 'left')
solution = bfs(initial_state)
print_solution(solution)
