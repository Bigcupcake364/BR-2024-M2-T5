import random   

from dino_runner.components.obstacles.obstacle import Obstacle
from dino_runner.utils.constants import BG


class Cactus(Obstacle):
    def __init__(self, image, heigth):
        self.type = random.randint(0, 2)
        super().__init__(image, self.type)

        self.heigth = heigth
        self.rect.y = BG.get_height() + self.heigth