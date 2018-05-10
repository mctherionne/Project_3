#!/usr/bin/python3
# -*- coding: Utf-8 -*

"""
files for class to create items
"""
import random
import pygame
import constant
import labyrinth as lab


class Item:
    """class to create Item"""

    def __init__(self, name, free_box):
        self.name = name
        self.position = []
        self.free_box = free_box
        self.item_location()

    def item_location(self):
        """Method for placing an object randomly"""
        self.position.append(random.choice(self.free_box))

    def item_display(self, window):
        # Loading image
        item = pygame.image.load(constant.image_loot).convert
        num_line = 0
        for line in lab.Labyrinth.self.structure:
            num_case = 0
            for sprite in line:
                x = num_case * constant.size_sprite
                y = num_line * constant.size_sprite
                if sprite == self.position:
                    window.blit(item, (x, y))



    def undisplay(self, window):
        pass


