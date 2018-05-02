import random

import pygame

import constant
import labyrinth


class Item():

    def __init__(self, position_x, position_y, name):
        self.name = name
        item = pygame.image.load(constant.image_loot).convert
        self.item = item
        self.position_x = position_x
        self.position_y = position_y
        self.position = position_x * position_y
        position_r = random.random(labyrinth.free_box)
        self.position_r = position_r

    def needle(self, position):
        pass

