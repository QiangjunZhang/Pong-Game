import pygame
import sys
from src.ball import Ball
from src.game_manager import Manager
from src.game_window import GameWindow
from src.player import Player


pygame.init()
clock = pygame.time.Clock()
pygame.display.set_caption('Ping Pong')

screen_width = 1280
screen_height = 960
bg_color = pygame.Color('grey12')
light_grey = (27, 235, 60)
game_window = GameWindow(screen_width, screen_height)

ball = Ball(game_window.get_width() // 2 - 15, game_window.get_height() // 2 - 15, 7, 7, 30, 30)
ball.set_color((200, 10, 10))
player = Player(game_window.get_width() - 20, game_window.get_height() // 2 - 70, 0, 0, 10, 500)
player.set_color((20, 210, 210))
opponent = Player(10, screen_height // 2 - 70, 0, 7, 10, 140)
game_manager = Manager(ball, player, opponent)


while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_DOWN:
                player.speed_y += 7
            if event.key == pygame.K_UP:
                player.speed_y -= 7
        if event.type == pygame.KEYUP:
            if event.key == pygame.K_DOWN:
                player.speed_y -= 7
            if event.key == pygame.K_UP:
                player.speed_y += 7

    game_window.screen.fill(bg_color)
    pygame.draw.aaline(game_window.screen, light_grey,
                       (game_window.get_width() / 2, 0),
                       (game_window.get_width() / 2,
                        game_window.get_height()))
    game_manager.run_game(game_window)
    pygame.display.flip()
    clock.tick(60)
