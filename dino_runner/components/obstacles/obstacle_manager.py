import pygame
import random

from dino_runner.components.obstacles.cactus import Cactus
from dino_runner.components.obstacles.bird import Bird
from dino_runner.utils.constants import SMALL_CACTUS, LARGE_CACTUS, BIRD

SMALL_CACTUS_HEIGHT = 295
LARGE_CACTUS_HEIGHT = 270
BIRD_HEIGHT = 240


class ObstacleManager:
    def __init__(self):
        self.obstacles = []

    def update(self, game):
        if len(self.obstacles) == 0: 
            random_obstacle = random.choice([SMALL_CACTUS, LARGE_CACTUS, BIRD])

            if random_obstacle == SMALL_CACTUS:
                self.obstacles.append(Cactus(random_obstacle, SMALL_CACTUS_HEIGHT))
            elif random_obstacle == LARGE_CACTUS:
                self.obstacles.append(Cactus(random_obstacle, LARGE_CACTUS_HEIGHT))
            elif random_obstacle == BIRD:
                self.obstacles.append(Bird(random_obstacle, BIRD_HEIGHT))
    
        for obstacle in self.obstacles:
            obstacle.update(game.game_speed, self.obstacles)
            if game.player.dino_rect.colliderect(obstacle.rect):
                pygame.time.delay(500)
                game.playing = False
                break

    def draw(self, screen):
        for obstacle in self.obstacles:
            obstacle.draw(screen)
         
