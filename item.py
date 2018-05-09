#!/usr/bin/python3
# -*- coding: Utf-8 -*

"""
files for class to create items
"""

import pygame
import constant


class Item:
    """class to create Item"""
    def __init__(self, position_x, position_y, name):
        self.name = name
        item = pygame.image.load(constant.image_loot).convert
        self.item = item
        self.position_x = position_x
        self.position_y = position_y
        self.position = position_x * position_y

    def item_location(self):
        """Method for placing an object randomly"""
        pass
