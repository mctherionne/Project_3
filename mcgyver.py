from pygame import sprite
import labyrinth
import constant


class Mcgyver:
    def __init__(self, level):
        self.direction = labyrinth.pygame.image.load(constant.image_macgyver).convert_alpha()
        self.direction = labyrinth.pygame.transform.scale(self.direction, (30, 30))
        self.case_x = 0
        self.case_y = 0
        self.x = 0
        self.y = 0
        self.level = level

    def move(self, direction):
        if direction == 'right':
            if self.case_x < (constant.number_sprite_side - 1):
                if self.level.structure[self.case_y][self.case_x + 1] != "m":
                    self.case_x += 1
                    self.x = self.case_x * constant.size_sprite

        if direction == 'left':
            if self.case_x > 0:
                if self.level.structure[self.case_y][self.case_x - 1] != 'm':
                    self.case_x -= 1
                    self.x = self.case_x * constant.size_sprite

        if direction == 'up':
            if self.case_y > 0:
                if self.level.structure[self.case_y - 1][self.case_x] != 'm':
                    self.case_y -= 1
                    self.y = self.case_y * constant.size_sprite

        if direction == 'down':
            if self.case_y < (constant.number_sprite_side - 1):
                if self.level.structure[self.case_y + 1][self.case_x] != 'm':
                    self.case_y += 1
                    self.y = self.case_y * constant.size_sprite

        if sprite != 'a':
            pass
