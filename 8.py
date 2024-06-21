def dfs(graph, start):
    visited = set()
    traversal_order = []
    def dfs_recursive(node):
        visited.add(node)
        traversal_order.append(node)
        for neighbor in graph[node]:
            if neighbor not in visited:
                dfs_recursive(neighbor)
    dfs_recursive(start)
    return traversal_order
graph = {
    'A': ['B', 'C'],
    'B': ['A', 'D', 'E'],
    'C': ['A', 'F'],
    'D': ['B'],
    'E': ['B', 'F'],
    'F': ['C', 'E']
}
start_node = 'A'
result = dfs(graph, start_node)
print("DFS Traversal Order:", result)
