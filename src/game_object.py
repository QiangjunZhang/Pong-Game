import pygame


class GameObject:
    def __init__(self, x, y, speed_x, speed_y, width, length):
        self.x = x
        self.y = y
        self.speed_x = speed_x
        self.speed_y = speed_y
        self.rect = pygame.Rect(x, y, width, length)
        self.color = (27, 235, 60)

    def set_color(self, color):
        self.color = color
