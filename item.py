import pygame
from labyrinth import Labyrinth
import constant


class Item(Labyrinth):

    def __init__(self, position_x, position_y):
        item = pygame.image.load(constant.image_loot).convert
        self.item = item
        self.position_x = position_x
        self.position_y = position_y
        Labyrinth.__init__(self.free_box)
        self.position = position_x * position_y


    def aleatory_position(self):
        self.position = Labyrinth.self.free_box.random.choice()
        print(Labyrinth.free_box)







