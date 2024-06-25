% Family tree
parent(john, mary).
parent(mary, susan).
parent(mary, james).
parent(susan, kate).

ancestor(X, Y) :- parent(X, Y).
ancestor(X, Y) :-
    parent(X, Z),
    ancestor(Z, Y).
