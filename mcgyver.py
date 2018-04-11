import pygame
from pygame.locals import *
from constant import *
from labyrinth import *
class mcgyver:
    def __init__(self, move, level):
        self.move = pygame.image.load(image_macgyver).convert_alpha()
        self.case_x = 0
        self.case_y = 0
        self.x = 0
        self.y = 0
        self.level = level


    def move(self, direction):
        if direction =='right':
            if self.case_x < (number_sprite_side - 1):
                if self.level.structure [self.case_y][self.case_x + 1] != "w":
                    self.case_x += 1
                    self.x = self.case_x * size_sprite

        if direction == 'left':
            if self.case_x > 0:
                if self.level.structure [self.case_y] [self.case_x - 1] !='w':
                    self.case_x -= 1
                    self.x = self.case_x * size_sprite

        if direction == 'up':
            if self.case_y > 0
                if self.level.structure [self.case_x] [self.case_y - 1] !='w':
                    self.case_y -= 1
                    self.y = self.case_y *size_sprite

        if direction == 'down':
            if self.case_y < (number_sprite_side - 1):
                if self.level.structure [self.case_x] [self.case_y + 1] != 'w':
                    self.case_y += 1
                    self.y = self.case_y * size_sprite
