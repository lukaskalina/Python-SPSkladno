import pygame
pygame.init()
screen = pygame.display.set_mode((700,550))
pygame.display.set_caption("Uhybani")
running = True
clock = pygame.time.Clock()
while running:
    screen.fill((255, 0, 0))
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    clock.tick(60)
    pygame.display.update()

pygame.quit