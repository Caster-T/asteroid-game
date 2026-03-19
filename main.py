import pygame
from constants import *
from logger import log_state, log_event
from circleshape import CircleShape
from player import Player
from asteroid import Asteroid
from asteroidfield import AsteroidField
import sys
from shot import Shot
from score import Score
from screens import draw_game_over

def main():
    pygame.init()
    

    print(f"Starting Asteroids with pygame version: {pygame.version.ver}")
    print(f"Screen width: {SCREEN_WIDTH}\nScreen height: {SCREEN_HEIGHT}")

    screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
    clock = pygame.time.Clock()
    dt = 0
    
    game_state = "playing"

    updatable = pygame.sprite.Group()
    drawable = pygame.sprite.Group()
    Player.containers = (updatable, drawable)

    player = Player(SCREEN_WIDTH/2, SCREEN_HEIGHT/2)

    asteroids = pygame.sprite.Group()
    Asteroid.containers = (asteroids, updatable, drawable)

    asteroidfield = pygame.sprite.Group()
    AsteroidField.containers = (updatable,)
    field = AsteroidField()

    shots = pygame.sprite.Group()
    Shot.containers = (shots, updatable, drawable)
    
    
    score = Score()
    updatable.add(score)
    drawable.add(score)

    keys = pygame.key.get_pressed()

    high_score = score.get_high_score()

    while True:
        log_state()
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                return
            if game_state == "game_over":
                if event.type == pygame.KEYDOWN and event.key == pygame.K_r:
                    for asteroid in asteroids:
                        asteroid.kill()
                    shots.empty()
                    score.score = 0
                    player.position = pygame.Vector2(SCREEN_WIDTH/2, SCREEN_HEIGHT/2)
                    new_field = AsteroidField()
                    game_state = "playing"

        if game_state == "playing":
            updatable.update(dt)
            for asteroid in asteroids:
                distance_vector = player.position - asteroid.position
                distance = distance_vector.length()
                if distance <= player.radius + asteroid.radius:
                    log_event("player_hit")
                    print("Game over!")
                    game_state = "game_over"
                    if score.score > high_score:
                        high_score = score.score
                        score.save_high_score()
                    break

        for asteroid in asteroids:
            for shot in shots:
                distance_vector = shot.position - asteroid.position
                distance = distance_vector.length()
                if distance <= shot.radius + asteroid.radius:
                    log_event("asteroid_shot")
                    score.add_points()
                    pygame.sprite.Sprite.kill(shot)
                    asteroid.split()
            

        

        screen.fill("black")
        
        for obj in drawable:
            obj.draw(screen)

        if game_state == "game_over":
            draw_game_over(screen, score.score , high_score, SCREEN_WIDTH, SCREEN_HEIGHT)

        pygame.display.flip()
        
        dt = clock.tick(60)/1000



if __name__ == "__main__":
    main()
