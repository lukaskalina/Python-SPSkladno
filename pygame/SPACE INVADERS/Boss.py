import pygame
import settings
from Enemy import Enemy
import random as rand

class Boss(Enemy):
    def __init__(self,y,x):
        super().__init__(x,y)
        self.image = pygame.transform.scale(self.image, (self.image.get_width()*settings.BOSS_SCALE, self.image.get_height()*settings.))
        self.hp = 20
 