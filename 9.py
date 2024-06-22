import itertools
def distance(c1, c2):
    return ((c1[0] - c2[0]) ** 2 + (c1[1] - c2[1]) ** 2) ** 0.5
def total_distance(route, cities):
    return sum(distance(cities[route[i]], cities[route[i+1]]) for i in range(len(route)-1)) + distance(cities[route[-1]], cities[route[0]])
def tsp(cities):
    n = len(cities)
    routes = itertools.permutations(range(n))
    best_route = min(routes, key=lambda route: total_distance(route, cities))
    return best_route, total_distance(best_route, cities)
cities = [(0, 0), (1, 2), (3, 1), (6, 3)]
best_route, min_distance = tsp(cities)
print("Best route:", best_route)
print("Minimum distance:", min_distance)
