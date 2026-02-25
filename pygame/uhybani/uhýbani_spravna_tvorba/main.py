import pygame
from Player import *
from settings import *
from Asteroid import *
pygame.init()
screen = pygame.display.set_mode((WIDTH,HEIGHT))
pygame.display.set_caption("Uhybani")
running = True
clock = pygame.time.Clock()

player = Player(WIDTH // 2,HEIGHT)
player_group = pygame.sprite.Group()
player_group.add(player)
asteroid = Asteroid(WIDTH // 2,0)
asteroid_group = pygame.sprite.Group()
asteroid_group.add(asteroid)
while running:
    screen.fill((255, 0, 0))
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    player_group.update()
    player_group.draw(screen)
    asteroid_group.update()
    asteroid_group.update(screen)

    clock.tick(60)
    pygame.display.update()



