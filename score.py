import pygame

class Score(pygame.sprite.Sprite):
    def __init__(self):
        super().__init__()
        self.score = 0
        self.score_increment = 100
        self.timer_increment = 1
        self.font = pygame.font.Font(None, 36)

    def add_points(self):
        self.score += self.score_increment

    def update(self, dt):
        self.score += self.timer_increment * dt

    def draw(self, screen):
        text = self.font.render(f"Score:{int(self.score)}", True, (255,255,255))
        screen.blit(text,(10,10))