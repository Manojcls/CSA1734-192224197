% Backward chaining example
fact(sun_is_hot).

rule(day_is_bright) :-
    fact(sun_is_hot).

query(X) :-
    rule(X).
