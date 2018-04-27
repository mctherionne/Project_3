from random import random
import pygame
import constant
from labyrinth import Labyrinth
from mcgyver import Mcgyver


class Item(Labyrinth, Mcgyver):

    def __init__(self, position_x, position_y, name):
        self.name = name
        item = pygame.image.load(constant.image_loot).convert
        self.item = item
        self.position_x = position_x
        self.position_y = position_y
        Labyrinth.__init__(self.free_box)
        self.position = position_x * position_y

    def aleatory_position(self, position, name):
        if name == "needle":
            random(self.free_box)

            print(random, self.position)
