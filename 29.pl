% Forward chaining example
:- dynamic fact/1.

fact(sun_is_hot).

rule(day_is_bright) :-
    fact(sun_is_hot).

apply_rules :-
    rule(X),
    \+ fact(X),
    assert(fact(X)),
    fail.
apply_rules.
