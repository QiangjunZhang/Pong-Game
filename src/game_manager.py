class Manager:
    def __init__(self, ball, player, opponent):
        self.ball = ball
        self.player = player
        self.opponent = opponent

    def run_game(self, game_window):
        if self.opponent.rect.top < self.ball.rect.y:
            self.opponent.speed_y = abs(self.opponent.speed_y)
        else:
            self.opponent.speed_y = -abs(self.opponent.speed_y)

        if self.ball.rect.colliderect(self.player.rect):
            self.ball.reverse('x')
            self.ball.rect.x = self.player.rect.x - 30
        elif self.ball.rect.colliderect(self.opponent.rect):
            self.ball.reverse('x')
            self.ball.rect.x = self.opponent.rect.x + 30

        self.ball.animation(game_window)
        self.player.animation(game_window)
        self.opponent.animation(game_window)
