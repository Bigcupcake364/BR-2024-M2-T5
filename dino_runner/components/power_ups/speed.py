import random

from dino_runner.utils.constants import SPEED, SPEED_TYPE
from dino_runner.components.power_ups.power_up import PowerUp


class Speed(PowerUp):
    def __init__(self):
        self.image = SPEED
        self.type = SPEED_TYPE
        self.life = 0
        self.duration = 5
        super().__init__(self.image, self.type, self.duration, self.life)