% Bird can fly or not
bird(sparrow).
bird(eagle).
bird(penguin).

can_fly(Bird) :-
    bird(Bird),
    Bird \= penguin.
