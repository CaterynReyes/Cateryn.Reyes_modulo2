from dino_runner.components.obstacles.obstacle import Obstacle
import random
import pygame
from pygame.sprite import Sprite


class Bird(Obstacle):
     BIRD_HEIGHTS = [250, 290, 320]
     def __init__(self, image, description):
        self.image = image
        self.type = 0
        self.description = description
        super().__init__(self.image, self.type, self.description)
        self.rect.y = random.choice(self.BIRD_HEIGHTS)
        self.index = 0
