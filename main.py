# main.py

from objecten import maak_scherm, maak_middenlijn, maak_batje, maak_bal, maak_pen
from spel import PongSpel
import instellingen


def main():
    screen = maak_scherm()
    maak_middenlijn()

    batje_a = maak_batje(instellingen.BATJE_A_X)
    batje_b = maak_batje(instellingen.BATJE_B_X)
    ball = maak_bal()
    pen = maak_pen()

    spel = PongSpel(screen, batje_a, batje_b, ball, pen)
    spel.koppel_toetsen()

    while True:
        spel.update()


if __name__ == "__main__":
    main()