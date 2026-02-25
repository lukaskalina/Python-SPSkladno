import pygame
from settings import *
class Asteroid(pygame.sprite.Sprite):
    def __init__(self,x,y):
        super().__init__()
        self.x = x
        self.y = y
        self.image = pygame.image.load("obrazky/asteroid.png")
        self.image = pygame.transform.scale(self.image, (BLOCK_WIDTH,BLOCK_HEIGHT))
        self.rect = self.image.get_rect(bottom=y,centerx = x)
        self.speed = BLOCK_SPEED
    def update(self):
        self.rect.y += self.speed

if __name__ == "__main__":
    import main
        