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
import item
import labyrinth
import mcgyver

pygame.init()
# Opening the Pygame window (square: width = height)
window = pygame.display.set_mode((800, 600))
# Icon
icon = pygame.image.load(constant.image_icon)
pygame.display.set_icon(icon)
# Title
pygame.display.set_caption(constant.window_title)

# Home loop
continuer = 1
choice = 0
continuer_game = 0

while continuer:
    # Loading and viewing the home screen
    home = pygame.image.load(constant.image_home).convert()
    window.blit(home, (0, 0))

    # Refresh
    pygame.display.flip()

    # Speed limitation of the loop
    pygame.time.Clock().tick(30)

    for event in pygame.event.get():

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
        background_2 = pygame.draw.rect(window, (0, 0, 0), (0, 0, 800, 600))
        background = pygame.Surface(window.get_size())
        background = pygame.image.load(constant.image_background).convert()
        window.blit(background, (0, 0))
        # Generating a level from a file
        level = labyrinth.Labyrinth(choice)
        level.generate()
        level.display(window)

        pygame.display.flip()

        # Creation of macgyver
        mcg = mcgyver.Mcgyver(level)
        level.display(window)

        # creation items
        name_item = ("needle", "small plastic tube", "ether")
        item.Item.name = name_item
        image_loot = pygame.image.load(constant.image_loot).convert()
        for i in range(0, 3):
            level.item_lab.append(item.Item(name_item[i], level.free_box))
            level.item_lab[i].item_display(window)

            print(level.item_lab[i].name, level.item_lab[i].position)

        # game loop
        continuer_game = 1
        while continuer_game:

            # Background for write item, inventory
            font = pygame.font.SysFont("broadway", 36)
            text = font.render("you got : ", 1, (255, 255, 255))
            window.blit(text, (450, 0))

            # when mcgyver go in case with a item
            if mcg.case == level.item_lab[0].position:
                window.blit(background, (mcg.x, mcg.y))
                text_1 = font.render(level.item_lab[0].name, 1, (255, 255, 255))
                window.blit(text_1, (450, 40))
                pygame.display.flip()
                item.Item.inventory(level.item_lab.name)
            elif mcg.case == level.item_lab[1].position:
                window.blit(background, (mcg.x, mcg.y))
                text_2 = font.render(level.item_lab[1].name, 1, (255, 255, 255))
                window.blit(text_2, (450, 90))
                pygame.display.flip()
            elif mcg.case == level.item_lab[2].position:
                window.blit(background, (mcg.case_x, mcg.case_y))
                text_3 = font.render(level.item_lab[2].name, 1, (255, 255, 255))
                window.blit(text_3, (450, 150))
                pygame.display.flip()


            pygame.time.Clock().tick(30)

            for event in pygame.event.get():

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
            window.blit(background, (mcg.old_case_x, mcg.old_case_y))
            window.blit(mcg.direction, (mcg.x, mcg.y))
            pygame.display.flip()

            # when Mcgyver finished level
            # if mcgyver had all item
            if level.structure[mcg.case_y][mcg.case_x] == 'a':
                continuer = 1
                background_3 = pygame.draw.rect(window, (255, 255, 255), (0, 0, 800, 600))
                finished_game = "congratulation you have down the guard"
                font = pygame.font.SysFont("broadway", 58, bold=False, italic=False)
                text_4 = font.render(finished_game, 1, (0, 0, 0))
                window.blit(text_4, (5, 300))
            # if Mcgyver had no item
