import pygame

from src.game_object import GameObject


class Player(GameObject):
    def boundary_bounce(self, game_window):
        if self.rect.top <= 0:
            self.rect.top = 0
        if self.rect.bottom >= game_window.get_height():
            self.rect.bottom = game_window.get_height()

    def move(self):
        self.rect.y += self.speed_y

    def animation(self, game_window):
        self.move()
        self.boundary_bounce(game_window)
        pygame.draw.rect(game_window.screen, self.color, self.rect)
