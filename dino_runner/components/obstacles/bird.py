from dino_runner.components.obstacles.obstacle import Obstacle
from dino_runner.components.dinossaur import Dinosaur
from dino_runner.utils.constants import BG, BIRD

dinosaur = Dinosaur()
step_index = dinosaur.step_index

class Bird(Obstacle):
    def __init__(self, image, heigth):
        self.type = 0 if step_index < 5 else 1
        super().__init__(image, self.type)

        self.heigth = heigth
        self.rect.y = BG.get_height() + self.heigth
  