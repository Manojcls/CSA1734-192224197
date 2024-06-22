import heapq
import math
def distance(c1, c2):
    return math.hypot(c1[0] - c2[0], c1[1] - c2[1])
def heuristic(cities, route):
    remaining = [distance(cities[route[-1]], cities[i]) for i in range(len(cities)) if i not in route]
    return min(remaining) if remaining else 0
def tsp_a_star(cities):
    n = len(cities)
    pq = [(heuristic(cities, [0]), 0, [0])]  
    while pq:
        estimated_cost, current_distance, route = heapq.heappop(pq)
        if len(route) == n:
            return route + [route[0]], current_distance + distance(cities[route[-1]], cities[route[0]])
        for next_city in range(n):
            if next_city not in route:
                next_route = route + [next_city]
                next_distance = current_distance + distance(cities[route[-1]], cities[next_city])
                heapq.heappush(pq, (next_distance + heuristic(cities, next_route), next_distance, next_route))
    return None, float('inf')
cities = [(0, 0), (1, 2), (3, 1), (6, 3)]
best_route, min_distance = tsp_a_star(cities)
print("Best route:", best_route)
print("Minimum distance:", min_distance)
