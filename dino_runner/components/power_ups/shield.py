import random

from dino_runner.utils.constants import SHIELD, SHIELD_TYPE
from dino_runner.components.power_ups.power_up import PowerUp


class Shield(PowerUp):
    def __init__(self):
        self.image = SHIELD
        self.type = SHIELD_TYPE
        self.life = 0
        self.duration = random.randint(8, 10)
        super().__init__(self.image, self.type, self.duration, self.life)