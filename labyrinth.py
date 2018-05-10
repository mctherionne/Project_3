#!/usr/bin/python3
# -*- coding: Utf-8 -*

"""
classes to create the game maze
"""

import pygame
import constant


class Labyrinth:
    """class to create a level"""

    def __init__(self, file):
        self.file = file
        self.structure = 0
        self.free_box = []
        self.item_lab = []
        
    def generate(self):
        """Method to generate the level according to the file.
         We create a general list, containing a list by line to display"""
        # Open the file
        with open(self.file, 'r') as file:
            structure_level = []
            # We go through the lines of the file
            for line in file:
                line_level = []
                # we go through the sprite contained in the file
                for sprite in line:
                    # We ignore the end of line "\ n"
                    if sprite != '\n':
                        # We add the sprite to the list of the sprite
                        line_level.append(sprite)
                # We add the line to the list of the level
                structure_level.append(line_level)
            # We saved this structure
            self.structure = structure_level

    def display(self, window):
        """Method to display the level according to the structure list returned by generate ()"""
        # loading images
        wall = pygame.image.load(constant.image_wall).convert()
        end_of_level = pygame.image.load(constant.image_guard).convert_alpha()
        end_of_level = pygame.transform.scale(end_of_level, (30, 30))
        background = pygame.image.load(constant.image_background).convert()
        # We go through the level line
        num_line = 0
        for line in self.structure:
            # We go through the lists of the line
            num_case = 0
            for sprite in line:
                # The actual position in pixels is calculated
                x = num_case * constant.size_sprite
                y = num_line * constant.size_sprite
                if sprite == 'm':  # m = wall
                    window.blit(wall, (x, y))
                elif sprite == 'a':  # a = end of level
                    window.blit(background, (x, y))
                    window.blit(end_of_level, (x, y))
                elif sprite == '0':  # 0 = path of Macgyver
                    self.free_box.append((x, y))
                    window.blit(background, (x, y))
                num_case += 1
            num_line += 1
