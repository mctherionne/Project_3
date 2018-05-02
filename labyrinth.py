import pygame
import constant


class Labyrinth:

    def __init__(self, file):
        self.file = file
        self.structure = 0
        self.free_box = []

    def generate(self):
        with open(self.file, 'r') as file:
            structure_level = []
            for line in file:
                line_level = []
                for sprite in line:
                    if sprite != '\n':
                        line_level.append(sprite)
                structure_level.append(line_level)
            self.structure = structure_level

    def display(self, window):
        wall = pygame.image.load(constant.image_wall).convert()
        end_of_level = pygame.image.load(constant.image_guard).convert_alpha()
        end_of_level = pygame.transform.scale(end_of_level, (30, 30))
        background = pygame.image.load(constant.image_background).convert()
        num_line = 0
        for line in self.structure:
            num_case = 0
            for sprite in line:
                x = num_case * constant.size_sprite
                y = num_line * constant.size_sprite
                if sprite == 'm':
                    window.blit(wall, (x, y))
                elif sprite == 'a':
                    window.blit(background, (x, y))
                    window.blit(end_of_level, (x, y))
                elif sprite == '0':
                    self.free_box.append((x, y))
                    window.blit(background, (x, y))
                num_case += 1
            num_line += 1
