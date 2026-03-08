from turtle import *
forward(100)
left(120)
color('pink')
forward(100)
home()
wait = input("Press Enter to continue.")
clearscreen()
# Algoritmische patronen met loops:
for steps in range(100):
    for c in ('red', 'green', 'blue'):
        color(c)
        forward(steps)
        right(30)
wait = input("Press Enter to continue.")