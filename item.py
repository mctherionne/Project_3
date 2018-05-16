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
        self.free_box = free_box
        self.item_location()


    def item_location(self):
        """Method for placing an object randomly"""
        self.position = random.choice(self.free_box)




    def item_display(self, window):
        """Method for display picture in my labyrinth"""
        # Loading image
        loot = pygame.image.load(constant.image_loot).convert()
        loot = pygame.transform.scale(loot, (30, 30))
        window.blit(loot, self.position)

    def item_undisplay(self, window):
        unloot = pygame.image.load(constant.image_background).convert()
        unloot = pygame.transform.scale(unloot, (30, 30))
        window.blit(unloot, self.position)



