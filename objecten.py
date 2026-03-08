# objecten.py

from turtle import Screen, Turtle
import instellingen


def maak_scherm():
    screen = Screen()
    screen.title(instellingen.TITEL)
    screen.bgcolor(instellingen.ACHTERGROND_KLEUR)
    screen.setup(width=instellingen.SCHERM_BREEDTE, height=instellingen.SCHERM_HOOGTE)
    screen.tracer(0)
    return screen


def maak_middenlijn():
    middenlijn = Turtle()
    middenlijn.speed(0)
    middenlijn.color(instellingen.VOORGROND_KLEUR)
    middenlijn.penup()
    middenlijn.hideturtle()
    middenlijn.goto(0, instellingen.SCHERM_HOOGTE // 2)
    middenlijn.setheading(270)

    for _ in range(instellingen.MIDDENLIJN_AANTAL_STREPEN):
        middenlijn.pendown()
        middenlijn.forward(instellingen.MIDDENLIJN_STREEP_LENGTE)
        middenlijn.penup()
        middenlijn.forward(instellingen.MIDDENLIJN_TUSSENRUIMTE)

    return middenlijn


def maak_batje(x_positie):
    batje = Turtle()
    batje.speed(0)
    batje.shape("square")
    batje.color(instellingen.VOORGROND_KLEUR)
    batje.shapesize(
        stretch_wid=instellingen.BATJE_HOOGTE,
        stretch_len=instellingen.BATJE_BREEDTE
    )
    batje.penup()
    batje.goto(x_positie, 0)
    return batje


def maak_bal():
    ball = Turtle()
    ball.speed(0)
    ball.shape("circle")
    ball.color(instellingen.VOORGROND_KLEUR)
    ball.penup()
    ball.goto(0, 0)
    ball.dx = instellingen.BAL_START_SNELHEID_X
    ball.dy = instellingen.BAL_START_SNELHEID_Y
    return ball


def maak_pen():
    pen = Turtle()
    pen.speed(0)
    pen.color(instellingen.VOORGROND_KLEUR)
    pen.penup()
    pen.hideturtle()
    pen.goto(0, 260)
    return pen