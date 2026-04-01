import pygame
import settings
import random as rand
class Enemy(pygame.sprite.Sprite):
    def __init__(self, x,y):
        super().__init__()
        self.image = pygame.image.load(settings.ENEMY_IMAGE_PATH.format(rand.randint(1,5 (constant) ENEMY_SCALE: float = 0.75)))
        