#!/usr/bin/python3
# -*- coding: Utf-8 -*

"""
files for class to create items
"""
import random

import pygame

import constant





class Item:
    """class to create Item"""

    def __init__(self, name, free_box):
        self.name = name
        self.position = ()
        self.dropped_item = False
        self.item_location(free_box)


    def item_location(self, free_box):
        """Method for placing an object randomly"""
        self.position = random.choice(free_box)




    def item_display(self, window):
        """Method for display picture in my labyrinth"""
        # Loading image
        loot = pygame.image.load(constant.image_loot).convert()
        loot = pygame.transform.scale(loot, (30, 30))
        window.blit(loot, self.position)




