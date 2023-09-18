import random 

from dino_runner.utils.constants import HEART, HEART_TYPE
from dino_runner.components.power_ups.power_up import PowerUp


class Heart(PowerUp):
    def __init__(self):
        self.image = HEART
        self.life = 1
        self.type = HEART_TYPE
        self.duration = 0
        super().__init__(self.image, self.type, self.duration, self.life)