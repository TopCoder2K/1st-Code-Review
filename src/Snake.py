import pygame

from src.Config import Config


class Snake:
    # Snake body placement.
    def __init__(self, display):
        # self.x_pos = (Config['game']['width'] - Config['game']['bumper_size']) / 2
        # self.y_pos = (Config['game']['height'] - Config['game']['bumper_size']) / 2
        self.x_pos = Config['game']['width'] / 2
        self.y_pos = Config['game']['height'] / 2
        self.display = display
        self.body = [(self.x_pos, self.y_pos)]
        self.max_size = 1

    def eat(self, eat_apple):
        self.max_size += 1
        eat_apple.play()

    # Draws a snake body.
    def draw(self):
        for index in range(len(self.body)):
            tmp_rect = pygame.draw.rect(
                self.display,
                Config['colors']['green'],
                [
                    self.body[index][0],
                    self.body[index][1],
                    Config['snake']['width'],
                    Config['snake']['height']
                ]
            )
        return tmp_rect

    # Changes coordinates.
    def move(self, dx, dy):
        self.body.append((self.x_pos, self.y_pos))
        self.x_pos += dx
        self.y_pos += dy

        if self.x_pos + Config['snake']['width'] > Config['game']['width']:
            self.x_pos %= Config['game']['width']
        if self.y_pos + Config['snake']['height'] > Config['game']['height']:
            self.y_pos %= Config['game']['height']
        if self.x_pos < 0:
            self.x_pos += Config['game']['width']
        if self.y_pos < 0:
            self.y_pos += Config['game']['height']

        if len(self.body) > self.max_size:
            del(self.body[0])
