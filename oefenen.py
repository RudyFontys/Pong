from turtle import *
# forward(100)
# left(120)
# color('pink')
# forward(100)
# home()
# wait = input("Press Enter to continue.")
# clearscreen()
# Algoritmische patronen met loops:
# for steps in range(100):
#     for c in ('red', 'green', 'blue', 'brown', 'yellow'):
#         color(c)
#         forward(steps)
#         right(30)
# wait = input("Press Enter to continue.")
color('red')
fillcolor('yellow')
begin_fill()
while True:
    forward(200)
    left(170)
    if abs(pos()) < 1:
        break
end_fill()
wait = input("Press Enter to continue.")