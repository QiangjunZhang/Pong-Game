import random
import pygame
from src.game_object import GameObject


class Ball(GameObject):
    def reverse(self, direction):
        if direction == 'x':
            self.speed_x *= -1
        elif direction == 'y':
            self.speed_y *= -1

    def reset(self):
        self.rect.center = (self.x, self.y)
        self.speed_x *= random.choice((1, -1))
        self.speed_x *= random.choice((1, -1))

    def boundary_bounce(self, game_window):
        if self.rect.top <= 0 or self.rect.bottom >= game_window.get_height():
            self.reverse('y')
        if self.rect.left <= 0 or self.rect.right >= game_window.get_width():
            self.reset()

    def move(self):
        self.rect.x += self.speed_x
        self.rect.y += self.speed_y

    def animation(self, game_window):
        self.move()
        self.boundary_bounce(game_window)
        pygame.draw.ellipse(game_window.screen, self.color, self.rect)
