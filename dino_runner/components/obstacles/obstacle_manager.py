import pygame
import random

from dino_runner.components.obstacles.cactus import Cactus
from dino_runner.components.obstacles.bird import Bird
from dino_runner.utils.constants import SMALL_CACTUS, LARGE_CACTUS, BIRD

BIRD_HEIGHT = 240


class ObstacleManager:
    def __init__(self):
        self.obstacles = []

    def update(self, game):
        obstacle_type = [
            Cactus(),
            Bird()
        ]
        if len(self.obstacles) == 0: 
            self.obstacles.append(obstacle_type[random.randint(0, 1)])

        for obstacle in self.obstacles:
            obstacle.update(game.game_speed, self.obstacles)
            if game.player.dino_rect.colliderect(obstacle.rect):
                pygame.time.delay(500)
                self.reset_obstacles(game)
                if game.score > game.record:
                    game.record = game.score
                game.playing = False
                game.last_score = game.score
                game.score = 0
                game.death_count += 1
                print(game.death_count)
                break

    def reset_obstacles(self, game):
        self.obstacles = []
        game.game_speed = 20

    def draw(self, screen):
        for obstacle in self.obstacles:
            obstacle.draw(screen)
         
