import pygame
from pygame.locals import *
from constant import *

class Labyrinth :
    def __init__(self, file):
        self.file = file
        self.structure = 0

    def generate(self):
        with open(self.file, 'r') as file :
            structure_level = []
            for line in file :
                line_level = []
                for sprite in line
                    if sprite != '\n'
                        line_level.append(sprite)
                structure_level.append(line_level)
            self.structure = structure_level

    def display(self, window):
