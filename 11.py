def is_valid(assignment, var, value, neighbors):
    return all(assignment.get(neighbor) != value for neighbor in neighbors[var])
def backtrack(assignment, variables, domain, neighbors):
    if len(assignment) == len(variables):
        return assignment
    var = next(v for v in variables if v not in assignment)
    for value in domain:
        if is_valid(assignment, var, value, neighbors):
            assignment[var] = value
            result = backtrack(assignment, variables, domain, neighbors)
            if result:
                return result
            del assignment[var]
    return None
def map_coloring(variables, domain, neighbors):
    return backtrack({}, variables, domain, neighbors)
variables = ['WA', 'NT', 'SA', 'Q', 'NSW', 'V', 'T']
domain = ['Red', 'Green', 'Blue']
neighbors = {
    'WA': ['NT', 'SA'],
    'NT': ['WA', 'SA', 'Q'],
    'SA': ['WA', 'NT', 'Q', 'NSW', 'V'],
    'Q': ['NT', 'SA', 'NSW'],
    'NSW': ['Q', 'SA', 'V'],
    'V': ['SA', 'NSW'],
    'T': []
}
solution = map_coloring(variables, domain, neighbors)
print("Solution:", solution)
