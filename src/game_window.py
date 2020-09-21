import pygame


class GameWindow:
    def __init__(self, width, height):
        self.__width = width
        self.__height = height
        self.screen = pygame.display.set_mode((self.__width, self.__height))

    def get_width(self):
        return self.__width

    def get_height(self):
        return self.__height
