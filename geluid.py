# geluid.py

import pygame

pygame.mixer.init()

pong_geluid = pygame.mixer.Sound("assets/pong.mp3")


def speel_pong_geluid():
    pong_geluid.play()