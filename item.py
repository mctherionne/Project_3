#!/usr/bin/python3
# -*- coding: Utf-8 -*

"""
files for class to create items
"""
import random
import pygame
import constant
import labyrinth as lab
import mcgyver as mcg


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
        """Method for display picture in my labyrinth"""
        # Loading image
        loot = pygame.transform.scale(constant.image_loot, (30, 30))

        for line in lab.Labyrinth.self.structure:
            for sprite in line:
                x = lab.Labyrinth.item_lab * constant.size_sprite
                y = lab.Labyrinth.item_lab * constant.size_sprite
                if sprite == self.position:
                    window.blit(loot, (x, y))
            pygame.display.flip()
