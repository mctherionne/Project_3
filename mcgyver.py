import pygame
from pygame.locals import *
from constant import *
from labyrinth import *
class mcgyver:
    def __init__(self, moove, level):
        self.move = pygame.image.load(character).convert_alpha()
        self.case_x = 0
        self.case_y = 0
        self.x = 0
        self.y = 0
        self.level = level


    def move(self, direction):
        if direction =='right':
            if self.case_x < (number_sprite_side - 1):
                if self.level.structure [self.case_y][self.case_x + 1] != "w"
                    self.case_x += 1
                    self.x = self.case_x * size_sprite

