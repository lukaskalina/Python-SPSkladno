import pygame
import settings
from Enemy import Enemy
import random as rand

class Boss(Enemy):
    def __init__(self,y,x):
        super().__init__(x,y)
        self.image = pygame.transform.scale(self.image, (self.image.get_width()*settings.BOSS_SCALE, self.image.get_height()*settings.BOSS_SCALE))
        self.hp = 20
    
    def update(self):
        if self.direction == 1:
            self.rect.move_ip(self.speed,0)
            self.counter_for_direction += 1 
        else:
            self.rect.move_ip(-self.speed,0)
            self.counter_for_direction -= 1 
        if self.counter_for_direction %100 == 0 and self.counter_for_direction != 0:
           self.direction *= -1
           self.rect.move_ip(0, settings.ENEMY_DROP_SPEED)
        self._check_borders()
 