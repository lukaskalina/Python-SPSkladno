import pygame
from settings import *

pygame.init()
screen = pygame.display.set_mode((800,600))
pygame.display.set_caption("SPACE INVADERS")
running = True


def vypis_menu():
    screen.blit(title_text, title_rect)
    screen.blit(play_text, play_rect)
    screen.blit(settings_text, settings_rect)
    screen.blit(quit_text, quit_rect)
    
state = "MENU"
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        if event.type == pygame.MOUSEBUTTONDOWN:
            mouse_pos = event.pos
            if state == "MENU":
                if play_rect.collidepoint(mouse_pos):
                    state = "PLAYING"
                if settings_rect.collidepoint(mouse_pos):
                    state = "SETTINGS"
                if quit_rect.collidepoint(mouse_pos):
                    running = False

    if state == "MENU":
        screen.fill((0,0,127))
        vypis_menu()
        pass
    elif state == "PLAYING":
        pass
    elif state == "PAUSED":
        pass
    elif state == "GAME_OVER":
        pass


    pygame.display.update()
