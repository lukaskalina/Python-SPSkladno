import pygame
import random
from settings import *
class Asteroid(pygame.sprite.Sprite):
    def __init__(self):
        super().__init__()
        x = random.randrange(0+ (BLOCK_WIDTH // 2) , WIDTH - (BLOCK_WIDTH // 2))
        y = 0
        self.image = pygame.image.load(BLOCK_IMAGE_PATH).convert_alpha()
        self.image = pygame.transform.scale(self.image, (BLOCK_WIDTH,BLOCK_HEIGHT))
        self.rect = self.image.get_rect(bottom=y,centerx = x)
        self.speed = BLOCK_SPEED
    def update(self):
        self.rect.y += self.speed
        if self.rect.top > HEIGHT:
            self.rect.bottom  = 0
            x = random.randrange(0+ (BLOCK_WIDTH // 2) , WIDTH - (BLOCK_WIDTH // 2))
            self.rect.centerx = x
if __name__ == "__main__":
    import main
        

        