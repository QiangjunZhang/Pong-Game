import pygame
import sys
from src.ball import Ball
from src.game_manager import Manager
from src.game_object import Speed, Point, Shape
from src.game_window import GameWindow
from src.player import Player


pygame.init()
clock = pygame.time.Clock()
pygame.display.set_caption('Ping Pong')

screen_width = 1280
screen_height = 960
bg_color = pygame.Color('grey20')
light_grey = pygame.Color('green')
game_window = GameWindow(screen_width, screen_height)

ball_point = Point(game_window.get_width() // 2 - 15, game_window.get_height() // 2 - 15)
ball_speed = Speed(7, 7)           # speed at x and y direction
ball_shape = Shape(30, 30)
ball = Ball(ball_point, ball_speed, ball_shape)
ball_color = pygame.Color('blue')
ball.set_color(ball_color)

player_point = Point(game_window.get_width() - 20, game_window.get_height() // 2 - 70)
player_speed = Speed(0, 0)         # speed at x and y direction
player_shape = Shape(10, 140)
player = Player(player_point, player_speed, player_shape)
player_color = pygame.Color('white')
player.set_color(player_color)

opponent_point = Point(10, screen_height // 2 - 70)
opponent_speed = Speed(0, 7)         # speed at x and y direction
opponent_shape = Shape(10, 140)
opponent = Player(opponent_point, opponent_speed, opponent_shape)
opponent_color = pygame.Color('green')
opponent.set_color(opponent_color)

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
