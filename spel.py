# spel.py

import instellingen
from geluid import speel_pong_geluid


class PongSpel:
    def __init__(self, screen, batje_a, batje_b, ball, pen):
        self.screen = screen
        self.batje_a = batje_a
        self.batje_b = batje_b
        self.ball = ball
        self.pen = pen

        self.score_speler_a = 0
        self.score_speler_b = 0

        self.schrijf_score()

    def schrijf_score(self):
        self.pen.clear()
        self.pen.write(
            f"Speler A: {self.score_speler_a}  Speler B: {self.score_speler_b}",
            align="center",
            font=instellingen.LETTERTYPE
        )

    def batje_a_up(self):
        y = self.batje_a.ycor()
        y += instellingen.BATJE_STAP
        if y > 250:
            y = 250
        self.batje_a.sety(y)

    def batje_a_down(self):
        y = self.batje_a.ycor()
        y -= instellingen.BATJE_STAP
        if y < -250:
            y = -250
        self.batje_a.sety(y)

    def batje_b_up(self):
        y = self.batje_b.ycor()
        y += instellingen.BATJE_STAP
        if y > 250:
            y = 250
        self.batje_b.sety(y)

    def batje_b_down(self):
        y = self.batje_b.ycor()
        y -= instellingen.BATJE_STAP
        if y < -250:
            y = -250
        self.batje_b.sety(y)

    def koppel_toetsen(self):
        self.screen.listen()
        self.screen.onkeypress(self.batje_a_up, instellingen.TOETS_A_OMHOOG)
        self.screen.onkeypress(self.batje_a_down, instellingen.TOETS_A_OMLAAG)
        self.screen.onkeypress(self.batje_b_up, instellingen.TOETS_B_OMHOOG)
        self.screen.onkeypress(self.batje_b_down, instellingen.TOETS_B_OMLAAG)

    def reset_bal(self, richting):
        self.ball.goto(0, 0)
        self.ball.dx = instellingen.BAL_START_SNELHEID_X * richting
        self.ball.dy = instellingen.BAL_START_SNELHEID_Y

    def beweeg_bal(self):
        self.ball.setx(self.ball.xcor() + self.ball.dx)
        self.ball.sety(self.ball.ycor() + self.ball.dy)

    def controleer_boven_onderrand(self):
        if self.ball.ycor() > instellingen.BOVENRAND:
            self.ball.sety(instellingen.BOVENRAND)
            self.ball.dy *= -1
            speel_pong_geluid()

        if self.ball.ycor() < instellingen.ONDERRAND:
            self.ball.sety(instellingen.ONDERRAND)
            self.ball.dy *= -1
            speel_pong_geluid()

    def kaats_tegen_batje(self, batje, is_links):
        # Hoe ver van het midden van het batje zit de bal?
        verschil = self.ball.ycor() - batje.ycor()

        # Batje is ongeveer 100 pixels hoog (5 stretch_wid => ±50 boven/onder midden)
        relatieve_raakplek = verschil / 50

        # Begrenzen zodat extreme hoeken niet te gek worden
        if relatieve_raakplek > 1:
            relatieve_raakplek = 1
        if relatieve_raakplek < -1:
            relatieve_raakplek = -1

        huidige_snelheid_x = abs(self.ball.dx) * instellingen.BAL_VERSNELLING
        if huidige_snelheid_x > instellingen.BAL_MAX_SNELHEID:
            huidige_snelheid_x = instellingen.BAL_MAX_SNELHEID

        nieuwe_snelheid_y = relatieve_raakplek * huidige_snelheid_x

        if is_links:
            self.ball.setx(-340)
            self.ball.dx = huidige_snelheid_x
        else:
            self.ball.setx(340)
            self.ball.dx = -huidige_snelheid_x

        self.ball.dy = nieuwe_snelheid_y
        speel_pong_geluid()

    def controleer_batjes(self):
        # Botsing rechts
        if (
            340 < self.ball.xcor() < 350
            and self.batje_b.ycor() + 50 > self.ball.ycor() > self.batje_b.ycor() - 50
            and self.ball.dx > 0
        ):
            self.kaats_tegen_batje(self.batje_b, is_links=False)

        # Botsing links
        if (
            -350 < self.ball.xcor() < -340
            and self.batje_a.ycor() + 50 > self.ball.ycor() > self.batje_a.ycor() - 50
            and self.ball.dx < 0
        ):
            self.kaats_tegen_batje(self.batje_a, is_links=True)

    def controleer_score(self):
        if self.ball.xcor() > instellingen.RECHTS_UIT:
            self.score_speler_a += 1
            self.schrijf_score()
            self.reset_bal(richting=-1)

        if self.ball.xcor() < instellingen.LINKS_UIT:
            self.score_speler_b += 1
            self.schrijf_score()
            self.reset_bal(richting=1)

    def update(self):
        self.screen.update()
        self.beweeg_bal()
        self.controleer_boven_onderrand()
        self.controleer_batjes()
        self.controleer_score()