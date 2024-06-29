% Best first search algorithm
% A simple example with nodes and edges
edge(a, b, 1).
edge(a, c, 3).
edge(b, d, 1).
edge(c, d, 1).
edge(d, goal, 2).

heuristic(goal, 0).
heuristic(a, 3).
heuristic(b, 2).
heuristic(c, 1).
heuristic(d, 0).

best_first_search(Start, Goal, Path) :-
    heuristic(Start, H),
    search([node(Start, [], H)], Goal, Path).

search([node(Goal, Path, _)|_], Goal, [Goal|Path]).
search([node(State, Path, _)|Rest], Goal, FinalPath) :-
    findall(node(NextState, [State|Path], NewH),
            (edge(State, NextState, _), heuristic(NextState, NewH)),
            Children),
    append(Rest, Children, NewNodes),
    sort(3, @=<, NewNodes, SortedNodes),
    search(SortedNodes, Goal, FinalPath).
