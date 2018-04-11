#!/usr/bin/python3
# -*- coding: Utf-8 -*

from labyrinth import *

pygame.init()

window = pygame.display.set_mode((window_rating, window_rating))
icon = pygame.image.load(image_icon)
pygame.display.set_icon(icon)
pygame.display.set_caption(window_title)

continuer = 1
while continuer:
    home = pygame.image.load(image_home).convert()
    window.blit(home, (0, 0))

    pygame.display.flip()
    continuer_home = 1
    continuer_game = 1

    while continuer_home:
        pygame.time.clock().tick(30)

        for event in pygame.event.get():
            if event.type == QUIT or event.type == KEYDOWN and event.key == K_ESCAPE:
                continuer_home = 0
                continuer_game = 0
                continuer = 0
                choice = 0

            elif event.type == KEYDOWN:
                if event.key == K_F1:
                    continuer_home = 0
                    choice = 'n1'

    if choice != 0:
        background = pygame.image.load (image_background).convert()

        level = level(choice)
        level.generate()
        level.display

        mac = perso
