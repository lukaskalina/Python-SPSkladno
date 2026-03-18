from multiprocessing.spawn import spawn_main
import pygame
from Player import *
from settings import *
from Asteroid import *
pygame.init()
screen = pygame.display.set_mode((WIDTH,HEIGHT))
pygame.display.set_caption("Uhybani")
running = True
clock = pygame.time.Clock()

player = Player(WIDTH//2, HEIGHT-10)
player_group = pygame.sprite.Group()
player_group.add(player)

asteroid_group = pygame.sprite.Group()
block_spawn_timer = 0

base_spawn_interval = 2000

game_over = False
game_over_time = 0
score = 0

try:
    with open("score.txt", "r") as file:
        highscore = int(file.read())
except:
    highscore = 0

while running:
    screen.fill((0, 0, 0))
    dt = clock.tick(60)

    if not game_over:
        block_spawn_timer += dt

    
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False

        if block_spawn_timer >= spawn_ :
            asteroid = Asteroid(random.randint(0+BLOCK_WIDTH//2, WIDTH-BLOCK_WIDTH//2),0)
            asteroid_group.add(asteroid)
            block_spawn_timer

        player_group.update()
        asteroid_group.update()

        for asteroid in asteroid_group:
            if asteroid.rect.top > HEIGHT:
                score += 1



        if pygame.sprite.spritecollide(player, asteroid_group, True, pygame.sprite.collide_mask):
            game_over = True
        game_over_time = pygame.time.get_ticks()
    else:
        font = pygame.font.Font(None , 74)
        game_over_text = font.render("GAMEOVER" , True, (255,0,0))
        screen.blit(game_over_text, (WIDTH //2 - game_over_text.get_width() //2 ,   HEIGHT // 2))

        if pygame.time.get_ticks() - game_over_time >=2000:
            if score > highscore:
                with open("score.txt", "w") as file:
                    file.write(f"{score}")
                highscore = score
            running = False

    font = pygame.font.Font(None , 36)

    score_text = font.render(f"SCORE: {score}", True, (255,255,255))
    screen.blit(score_text , (10,10))
    
    highscore_text = font.render(f"Highscore: {highscore}", True, (255,255,255))
    screen.blit(highscore_text, (WIDTH - highscore_text.get_width()-10,10))
            

    player_group.draw(screen)
    asteroid_group.draw(screen)
    pygame.display.update()
pygame.quit()



