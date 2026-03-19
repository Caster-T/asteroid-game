from shot import Shot
from constants import *
import pygame

class NormalWeapon:
    def __init__(self):
        self.cooldown = PLAYER_SHOOT_COOLDOWN_SECONDS 

    def shoot(self, player):
        direction = player.get_direction() * PLAYER_SHOT_SPEED
        shot = Shot(player.position.x, player.position.y)
        shot.velocity = direction



class ShotgunWeapon:
    def __init__(self):
        self.cooldown = PLAYER_SHOOT_COOLDOWN_SECONDS * 2
        
    def shoot(self, player):
        base_direction = player.get_direction()

        angles = [-15, 0, 15]

        for angle in angles:
            direction = base_direction.rotate(angle) * PLAYER_SHOT_SPEED
            shot = Shot(player.position.x, player.position.y)
            shot.velocity = direction