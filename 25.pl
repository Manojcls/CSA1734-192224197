% Monkey and banana problem
state(monkey, on_floor, at_door, has_not).
state(monkey, on_box, at_banana, has).

move(state(middle, on_box, middle, has_not), grab, state(middle, on_box, middle, has)).
move(state(X, on_floor, X, H), climb, state(X, on_box, X, H)).
move(state(X1, on_floor, X1, H), push(X1, X2), state(X2, on_floor, X2, H)).
move(state(X1, on_floor, B, H), walk(X1, X2), state(X2, on_floor, B, H)).

canget(state(_, _, _, has)).
canget(State1) :-
    move(State1, _, State2),
    canget(State2).
