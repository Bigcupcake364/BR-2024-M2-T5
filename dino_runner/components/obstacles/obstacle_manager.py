import pygame
import random

from dino_runner.components.obstacles.cactus import Cactus
from dino_runner.components.obstacles.bird import Bird
from dino_runner.utils.constants import SHIELD_TYPE, HAMMER_TYPE, DEFAULT_TYPE, SPEED_TYPE, RUNNING_SHIELD_ACT, JUMPING_SHIELD_ACT, DUCKING_SHIELD_ACT, DINO_DAMAGE, CACTUS_DEATH, BIRD_DEATH

X_POS = 80
Y_POS = 310
Y_POS_DUCK = 340

SHA_IMG = {0: RUNNING_SHIELD_ACT,
           1: JUMPING_SHIELD_ACT,
           2: DUCKING_SHIELD_ACT
           }


class ObstacleManager:
    def __init__(self):
        self.obstacles = []
        self.step_index = 0
    def update(self, game):
        obstacle_type = [
            Cactus(),
            Bird(),
        ]

        if len(self.obstacles) == 0:
            self.obstacles.append(obstacle_type[random.randint(0, 1)])

        for obstacle in self.obstacles:
            obstacle.update(game.game_speed, self.obstacles)
            if game.player.dino_rect.colliderect(obstacle.rect):
                if not game.player.has_power_up and game.player.life == 0:
                    pygame.time.delay(500)
                    game.player.type = DEFAULT_TYPE
                    game.player.power_up_time = 0
                    game.playing = False
                    game.death_count += 1
                    if isinstance(obstacle, Cactus):
                        game.death_message = CACTUS_DEATH[random.randint(0, 2)]
                    elif isinstance(obstacle, Bird):
                        game.death_message = BIRD_DEATH[random.randint(0, 2)]
                    break
                elif game.player.has_power_up and game.player.type == HAMMER_TYPE:
                    self.obstacles.pop()
                    game.player.type = DEFAULT_TYPE
                    game.player.power_up_time = 0
                elif game.player.has_power_up and game.player.type == SPEED_TYPE:
                    self.obstacles.pop()
                elif game.player.has_power_up and game.player.type == SHIELD_TYPE:   
                    game.player.image = SHA_IMG[game.player.index][game.player.step_index // 5]
                elif game.player.life > 0:
                    self.obstacles.pop()
                    game.player.image = DINO_DAMAGE
                    game.player.life -= 1

    def reset_obstacles(self):
        self.obstacles = []

    def draw(self, screen):
        for obstacle in self.obstacles:
            obstacle.draw(screen)
         
