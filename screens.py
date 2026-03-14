import pygame
from constants import *

def draw_game_over(screen, score, screen_width, screen_height):
    font = pygame.font.Font(None, 72)
    text = font.render("GAME OVER", True, (255,255,255))
    rect = text.get_rect(center=(screen_width/2, screen_height/2 - 50))
    screen.blit(text, rect)

    score_font = pygame.font.Font(None, 48)
    score_text = score_font.render(f"Final Score: {int(score)}", True, (255,255,255))
    score_rect = score_text.get_rect(center=(screen_width/2, screen_height/2 + 20))
    screen.blit(score_text, score_rect)

    reset_font = pygame.font.Font(None, 72)
    reset_text = reset_font.render("Press R to restart", True, (255,255,255))
    reset_rect = reset_text.get_rect(center=(screen_width/2,screen_height/2 + 100))
    screen.blit(reset_text, reset_rect)


    