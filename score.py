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
    
    def get_high_score(self):
        try:
            with open("highscore.txt", "r") as file:
                return int(file.read())
        except:
            with open("highscore.txt", "w") as file:
                file.write("0")
            return 0
        
    def save_high_score(self):
        with open("highscore.txt", "w") as file:
            file.write(str(int(self.score)))

 