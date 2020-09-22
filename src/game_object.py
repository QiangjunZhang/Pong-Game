import pygame


class Point:
    def __init__(self, x, y):
        self.x = x
        self.y = y


class Speed(Point):
    pass


class Shape:
    def __init__(self, width, length):
        self.width = width
        self.length = length


class GameObject:
    def __init__(self, point, speed, shape):
        self.x = point.x
        self.y = point.y
        self.speed_x = speed.x
        self.speed_y = speed.y
        self.rect = pygame.Rect(self.x, self.y, shape.width, shape.length)
        self.color = (27, 235, 60)

    def set_color(self, color):
        self.color = color
