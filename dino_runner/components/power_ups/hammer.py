import random 

from dino_runner.utils.constants import HAMMER, HAMMER_TYPE
from dino_runner.components.power_ups.power_up import PowerUp


class Hammer(PowerUp):
    def __init__(self):
        self.image = HAMMER
        self.life = 0
        self.type = HAMMER_TYPE
        self.duration = random.randint(8, 10)
        super().__init__(self.image, self.type, self.duration, self.life)