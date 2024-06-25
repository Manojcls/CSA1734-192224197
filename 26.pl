% Fruit and its color
fruit(apple, red).
fruit(banana, yellow).
fruit(grape, purple).
fruit(orange, orange).

find_color(Fruit, Color) :-
    fruit(Fruit, Color).
