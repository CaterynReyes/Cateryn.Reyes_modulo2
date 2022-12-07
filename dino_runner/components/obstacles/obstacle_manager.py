import random

import pygame
from dino_runner.components.obstacles.cactus import  LargeCactus, SmallCactus
from dino_runner.utils.constants import (
    SMALL_CACTUS,LARGE_CACTUS
)
class ObstacleManager:

    def __init__(self):
        self.obstacles=[]

    def update(self,game):
        if len(self.obstacles)==0:
            cactus_size=random.randint(0,2)
            if cactus_size==0:
                self.obstacles.append(SmallCactus(SMALL_CACTUS))
            else:
                self.obstacles.append(LargeCactus(LARGE_CACTUS))

        for obstacle in self.obstacles:
            obstacle.update(game.game_speed,self.obstacles)
            if game.player.dino_rect.colliderect(obstacle.rect):
                game.playing = False
                pygame.time.delay(1000)
                break
                

                          
    def draw(self,screen):
        for obstacle in self.obstacles:
            obstacle.draw(screen)

    def reset_obstacles(self,self1):
        self.obstacles=[]
        