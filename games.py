#!/usr/bin/python3
# -*- coding: Utf-8 -*

"""
Macgyver labyrinth game
games in which macgyver must move, pick up objects and get to the guards, through a labyrinth

Script Python
Files : games.py, mcgyver.py, labyrinth.py, item.py, constant.py, n1 + images
"""

import pygame
from pygame.locals import *
import constant
import labyrinth
import mcgyver
import item

labyrinth.pygame.init()
# Opening the Pygame window (square: width = height)
window = labyrinth.pygame.display.set_mode((800, 600))
# Icon
icon = labyrinth.pygame.image.load(constant.image_icon)
labyrinth.pygame.display.set_icon(icon)
# Title
labyrinth.pygame.display.set_caption(constant.window_title)

# Home loop
continuer = 1
choice = 0
continuer_game = 0

while continuer:
    # Loading and viewing the home screen
    home = labyrinth.pygame.image.load(constant.image_home).convert()
    window.blit(home, (0, 0))

    # Refresh
    labyrinth.pygame.display.flip()

    # Speed limitation of the loop
    labyrinth.pygame.time.Clock().tick(30)

    for event in labyrinth.pygame.event.get():

        # If the user leaves, we put the loop variables
        # at 0 to not browse any and close
        if event.type == QUIT or event.type == KEYDOWN and event.key == K_ESCAPE:
            continuer_game = 0
            continuer = 0
            # Variable of choice of the level
            choice = 0

        elif event.type == KEYDOWN:
            # Launch of level
            if event.key == K_1:
                continuer = 0  # we quit home
                choice = 'n1'  # We define the level to load
    # We check that the player has made a choice of level
    # to not load if he leaves
    if choice != 0:
        # load background
        background = labyrinth.pygame.Surface(window.get_size())
        background = labyrinth.pygame.image.load(constant.image_background).convert()
        window.blit(background, (0, 0))
        # Generating a level from a file
        level = labyrinth.Labyrinth(choice)
        level.generate()
        level.display(window)

        labyrinth.pygame.display.flip()

        # Creation of macgyver
        mcg = mcgyver.Mcgyver(level)
        level.display(window)

        # creation items
        name_item = ("needle", "small plastic tube", "ether")
        item.Item.name = name_item
        for i in range(0, 3):
            level.item_lab.append(item.Item(name_item[i], level.free_box))

            print(level.item_lab[i].name, level.item_lab[i].position)

        # game loop
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

                    # Movement keys
                    elif event.key == K_RIGHT:
                        mcg.move('right')
                    elif event.key == K_LEFT:
                        mcg.move('left')
                    elif event.key == K_UP:
                        mcg.move('up')
                    elif event.key == K_DOWN:
                        mcg.move('down')

            # Display on the news positions
            window.blit(background, (0, 0))
            level.display(window)
            window.blit(mcg.direction, (mcg.x, mcg.y))
            labyrinth.pygame.display.flip()

            # Victory -> back to the home
            if level.structure[mcg.case_y][mcg.case_x] == 'a':
                continuer_game = 0
