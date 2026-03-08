from turtle import *

# Variabelen

# Variabelen voor beide spelers op 0
score_speler_a = 0
score_speler_b = 0
a_up = "w"
a_down = "s"
b_up = "Up"
b_down = "Down"

# Objecten

# Scherminstellingen: titel - achtergrondkleur - afmeting
screen = Screen() # Maar een nieuw turtle screen
screen.title("Pong")
screen.bgcolor("black") # Uiteraard, wit is geen gezicht voor retro
screen.setup(width=800, height=600)
screen.tracer(0) # turtle commando: Update het scherm niet automatisch
# anders is het te traag, handmatig schermupdates zijn nu wel nodig
# https://docs.python.org/3/library/turtle.html#turtle.tracer

# Gestippelde middenlijn 
# Middenlijn tekenen
midline = Turtle()
midline.speed(0)
midline.color("orange")
midline.penup()
midline.hideturtle()
midline.goto(0, 300)      # start boven in het midden
midline.setheading(270)   # naar beneden kijken
# gestippelde lijn
for i in range(30):
    midline.pendown()
    midline.forward(10)
    midline.penup()
    midline.forward(10)

# batje A snelheid - vorm - kleur - grootte - pen-up (geen lijn tekenen) - pen locatie
batje_a = Turtle()
batje_a.speed(0)
batje_a.shape("square")
batje_a.color("orange")
batje_a.shapesize(stretch_wid=5, stretch_len=1)
batje_a.penup() # De tekenpen optillen, dus geen lijn trekken
batje_a.goto(-350, 0) # (x, y) coordinaten van de pen (-350 links van het midden)

# batje B
batje_b = Turtle()
batje_b.speed(0)
batje_b.shape("square")
batje_b.color("orange")
batje_b.shapesize(stretch_wid=5, stretch_len=1)
batje_b.penup()
batje_b.goto(350, 0)

# de bal snelheid - vorm - kleur - start locatie - richting van de beweging
ball = Turtle()
ball.speed(0)
ball.shape("circle")
ball.color("orange")
ball.penup()
ball.goto(0, 0)
ball.dx = 0.1 # beweeg 0,1 per update naar rechts (-0,1 is naar links)
ball.dy = -0.1 # beweeg 0,1 per update naar beneden

# de pen van turtle, Deze code schrijft de turtle tekst boven in het scherm
# Deze turtle wordt niet gebruikt om te bewegen of vormen te maken, 
# maar om tekst op het scherm te schrijven.
pen = Turtle() # maak een nieuwe turtle aan met de naam "pen"
pen.speed(0) # snelste vorm van turtle
pen.color("orange")
pen.penup() # teken geen lijnen als je beweegt (we willen tekst, geen lijnen)
pen.hideturtle() # De turtle-cursor (het pijltje) wordt onzichtbaar.
pen.goto(0, 260) # positie bijna bovenaan
pen.write("Speler A: 0  Speler B: 0", align="center", font=("Press Start 2P", 20, "normal"))

# Functies

def batje_a_up():
    y = batje_a.ycor()
    y += 25
    batje_a.sety(y)


def batje_a_down():
    y = batje_a.ycor()
    y -= 25
    batje_a.sety(y)


def batje_b_up():
    y = batje_b.ycor()
    y += 25
    batje_b.sety(y)


def batje_b_down():
    y = batje_b.ycor()
    y -= 25
    batje_b.sety(y)


screen.listen()
screen.onkeypress(batje_a_up, a_up)
screen.onkeypress(batje_a_down, a_down)
screen.onkeypress(batje_b_up, b_up)
screen.onkeypress(batje_b_down, b_down)


# Workflow

while True:
    screen.update()

    # Beweeg de bal
    ball.setx(ball.xcor() + ball.dx)
    ball.sety(ball.ycor() + ball.dy)

    # randen controleren
    if ball.ycor() > 280:
        ball.sety(280)
        ball.dy *= -1

    if ball.ycor() < -280:
        ball.sety(-280)
        ball.dy *= -1

    # naar links en rechts
    if (ball.xcor() < -340 and ball.xcor() > -350) and (batje_a.ycor() + 50 > ball.ycor() > batje_a.ycor() - 50):
        score_speler_a += 1
        pen.clear()
        pen.write("Speler A: {} Speler B: {}".format(score_speler_a, score_speler_b), align="center", font=("Press Start 2P", 20, "normal"))
    if ball.xcor() > 380:
        score_speler_a = 0
        pen.clear()
        pen.write("Speler A: {} Speler B: {}".format(score_speler_a, score_speler_b), align="center", font=("Press Start 2P", 20, "normal"))
        ball.goto(0, 0)
        ball.dx *= -1


    if (ball.xcor() > 340 and ball.xcor() < 350) and (batje_b.ycor() + 50 > ball.ycor() > batje_b.ycor() - 50):
        score_speler_b += 1
        pen.clear()
        pen.write("Speler A: {} Speler B: {}".format(score_speler_a, score_speler_b), align="center", font=("Press Start 2P", 20, "normal"))
    if ball.xcor() < -380:
        score_speler_b = 0
        pen.clear()
        pen.write("Speler A: {} Speler B: {}".format(score_speler_a, score_speler_b), align="center", font=("Press Start 2P", 20, "normal"))
        ball.goto(0, 0)
        ball.dx *= -1


    # als de bal het batje raakt
    if (ball.xcor() > 340 and ball.xcor() < 350) and (batje_b.ycor() + 50 > ball.ycor() > batje_b.ycor() - 50):
        ball.setx(340)
        ball.dx *= -1

    if (ball.xcor() < -340 and ball.xcor() > -350) and (batje_a.ycor() + 50 > ball.ycor() > batje_a.ycor() - 50):
        ball.setx(-340)
        ball.dx *= -1
