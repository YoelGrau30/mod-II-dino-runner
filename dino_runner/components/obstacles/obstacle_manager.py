import pygame
from dino_runner.components.obstacles.bird import Bird 
from dino_runner.components.obstacles.cactus import Cactus
from dino_runner.components.obstacles.cactus_large import CactusLarge
from dino_runner.utils.constants import SMALL_CACTUS, LARGE_CACTUS, BIRD
import random

class ObstacleManager:

    def __init__(self):
        self.obstacles = []

    def update(self, game):
        if len(self.obstacles) == 0:
            types = [
                Cactus(SMALL_CACTUS[0]), 
                Cactus(SMALL_CACTUS[1]), 
                Cactus(SMALL_CACTUS[2]), 
                CactusLarge(LARGE_CACTUS[0]),
                CactusLarge(LARGE_CACTUS[1]),
                CactusLarge(LARGE_CACTUS[2]),
                Bird(BIRD[0])
                ]
            self.obstacles.append(types[random.randint(0, 6)])

        for obstacle in self.obstacles:
            obstacle.update(game.game_speed, self.obstacles)
            if game.player.dino_rect.colliderect(obstacle.rect):
                game.player.dead()
                #pygame.time.delay(500)
                game.playing = False
                break 

    def draw(self, screen):
        for obstacle in self.obstacles:
            obstacle.draw(screen)

    def remove_obstacles(self):
        self.obstacles = []