import random
import pygame

from src.Config import Config


class Apple:
    def __init__(self, display):
        self.x_pos = 0
        self.y_pos = 0

        self.display = display

        # Generates a random integer between
        # the minimum and maximum of both directions.
        self.randomize()

    def randomize(self):
        width = Config['game']['width']
        height = Config['game']['height']
        bumper = Config['game']['bumper_size']

        max_x = width - bumper - Config['apple']['width']
        max_y = height - bumper - Config['apple']['height']

        # max_x = (width - Config['apple']['width'])
        # max_y = (height - Config['apple']['height'])

        self.x_pos = random.randint(bumper, max_x)
        self.y_pos = random.randint(bumper, max_y)
        # self.x_pos = random.randint(0, max_x)
        # self.y_pos = random.randint(0, max_y)

    def draw(self):
        return pygame.draw.rect(
            self.display,
            Config['colors']['red'],
            [
                self.x_pos,
                self.y_pos,
                Config['apple']['height'],
                Config['apple']['width']
            ]
        )
