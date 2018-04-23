#!/usr/bin/python3
# -*- coding: Utf-8 -*

from pygame.locals import *
from labyrinth import *
from mcgyver import Mcgyver
from constant import *

pygame.init()

window = pygame.display.set_mode((800, 600))
icon = pygame.image.load(image_icon)
pygame.display.set_icon(icon)
pygame.display.set_caption(window_title)

continuer = 1
choice = 0
continuer_game = 0

while continuer:
    home = pygame.image.load(image_home).convert()
    window.blit(home, (0, 0))

    pygame.display.flip()

    continuer_game = 1

    pygame.time.Clock().tick(30)

    for event in pygame.event.get():
        if event.type == QUIT or event.type == KEYDOWN and event.key == K_ESCAPE:
            continuer_game = 0
            continuer = 0


        elif event.type == KEYDOWN:
            if event.key == K_1:
                choice = 'n1'

    if choice != 0:
        background = pygame.image.load(image_background).convert()
        window.blit(background, (0, 0))
        level = Labyrinth(choice)
        level.generate()
        level.display(window)

        mcg = Mcgyver(image_macgyver, level)
        continuer_game = 1

        while continuer_game:

            pygame.time.Clock().tick(30)

            for event in pygame.event.get():

                if event.type == QUIT:
                    continuer_game = 0
                    continuer = 0

                elif event.type == KEYDOWN:
                    if event.key == K_ESCAPE:
                        continuer_game = 0

                    elif event.key == K_RIGHT:
                        mcg.move('right')
                    elif event.key == K_LEFT:
                        mcg.move('left')
                    elif event.key == K_UP:
                        mcg.move('up')
                    elif event.key == K_DOWN:
                        mcg.move('down')

            level.display(window)
            window.blit(mcg.direction, (0, 0))
            pygame.display.flip()

            if level.structure[mcg.case_y][mcg.case_x] == 'a':
                continuer_game = 0
