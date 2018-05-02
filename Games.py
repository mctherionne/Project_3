#!/usr/bin/python3
# -*- coding: Utf-8 -*
import pygame
from pygame.locals import *

import constant
import labyrinth
import mcgyver

labyrinth.pygame.init()

window = labyrinth.pygame.display.set_mode((800, 600))
icon = labyrinth.pygame.image.load(constant.image_icon)
labyrinth.pygame.display.set_icon(icon)
labyrinth.pygame.display.set_caption(constant.window_title)

continuer = 1
choice = 0
continuer_game = 0

while continuer:
    home = labyrinth.pygame.image.load(constant.image_home).convert()
    window.blit(home, (0, 0))

    labyrinth.pygame.display.flip()

    labyrinth.pygame.time.Clock().tick(30)

    for event in labyrinth.pygame.event.get():
        if event.type == QUIT or event.type == KEYDOWN and event.key == K_ESCAPE:
            continuer_game = 0
            continuer = 0


        elif event.type == KEYDOWN:
            if event.key == K_1:
                choice = 'n1'

    if choice != 0:

        background = labyrinth.pygame.Surface(window.get_size())
        background = labyrinth.pygame.image.load(constant.image_background).convert()
        window.blit(background, (0, 0))

        level = labyrinth.Labyrinth(choice)
        level.generate()
        level.display(window)

        labyrinth.pygame.display.flip()

        mcg = mcgyver.Mcgyver(level)
        level.display(window)

        continuer_game = 1
        while continuer_game:
            background_2 = pygame.draw.rect(window, (0, 0, 0), (0, 0, 800, 600))
            inventory = "vous avez obtenue"
            font = pygame.font.SysFont("broadway", 36, bold=False, italic=False)
            text = font.render(inventory, 1, (255, 255, 255))
            window.blit(text, (450, 0))
            labyrinth.pygame.time.Clock().tick(30)

            for event in labyrinth.pygame.event.get():

                if event.type == QUIT:
                    continuer_game = 0
                    continuer = 0

                elif event.type == KEYDOWN:
                    if event.key == K_ESCAPE:
                        continuer_game = 0
                        continuer = 1

                    elif event.key == K_RIGHT:
                        mcg.move('right')
                    elif event.key == K_LEFT:
                        mcg.move('left')
                    elif event.key == K_UP:
                        mcg.move('up')
                    elif event.key == K_DOWN:
                        mcg.move('down')

            window.blit(background, (0, 0))
            level.display(window)
            window.blit(mcg.direction, (mcg.x, mcg.y))
            labyrinth.pygame.display.flip()

            if level.structure[mcg.case_y][mcg.case_x] == 'a':
                continuer_game = 0
