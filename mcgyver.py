#!/usr/bin/python3
# -*- coding: Utf-8 -*

"""
class to create Macgyver (character of the game)
"""
import pygame
import constant
import labyrinth


class Mcgyver:
    """class to create a character"""

    def __init__(self, level):
        # Sprite of the character
        self.direction = pygame.image.load(constant.image_macgyver).convert_alpha()
        self.direction = pygame.transform.scale(self.direction, (30, 30))
        # Character position in boxes and pixel
        self.case_x = 0
        self.case_y = 0
        self.case = ()
        self.x = 0
        self.y = 0
        # Level in which the character is located
        self.level = level
        self.old_case_x = 0
        self.old_case_y = 0
        # Tuple for inventory
        self.inventory = []
        self.nb_item = 0
        self.actually_x = 0
        self.actually_y = 0

    def move(self, direction):
        """Method for moving the character"""
        self.case = (self.x, self.y)
        self.old_case_x = self.x
        self.old_case_y = self.y
        print(self.x, self.y)



        # Move to right
        if direction == 'right':
            # Not to exceed the screen
            if self.case_x < (constant.number_sprite_side - 1):
                # We check that the destination box is not a wall
                if self.level.structure[self.case_y][self.case_x + 1] != "m":
                    # Moving a box
                    self.case_x += 1
                    # Calculation of the actual pixel positions
                    self.x = self.case_x * constant.size_sprite

        # Move to left
        if direction == 'left':
            if self.case_x > 0:
                if self.level.structure[self.case_y][self.case_x - 1] != 'm':
                    self.case_x -= 1
                    self.x = self.case_x * constant.size_sprite
        # Move to up
        if direction == 'up':
            if self.case_y > 0:
                if self.level.structure[self.case_y - 1][self.case_x] != 'm':
                    self.case_y -= 1
                    self.y = self.case_y * constant.size_sprite
        # Move to down

        if direction == 'down':
            if self.case_y < (constant.number_sprite_side - 1):
                if self.level.structure[self.case_y + 1][self.case_x] != 'm':
                    self.case_y += 1
                    self.y = self.case_y * constant.size_sprite

    def add_item(self, name_item):
        """appends item on the list, for create a inventory"""

        self.inventory.append(name_item)
        self.nb_item = len(self.inventory)

        print(self.inventory)
        print(self.nb_item)
