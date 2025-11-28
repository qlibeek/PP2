import pygame
import random
import sys

pygame.init()
WIDTH, HEIGHT = 800, 600
screen = pygame.display.set_mode((WIDTH, HEIGHT))
clock = pygame.time.Clock()
WHITE = (255, 255, 255)
BLUE = (0, 0, 255)
RED = (255, 0, 0)
player_radius = 20
player_x = WIDTH - 150
player_y = HEIGHT // 2
player_speed = 5
enemies = []
enemy_width = 50
enemy_height = 50
enemy_speed = 5
enemy_spawn_rate = 20
running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
    keys = pygame.key.get_pressed()
    if keys[pygame.K_LEFT] and player_x - player_radius > 0:
        player_x -= player_speed
    if keys[pygame.K_RIGHT] and player_x + player_radius < WIDTH:
        player_x += player_speed
    if keys[pygame.K_UP] and player_y - player_radius > 0:
        player_y -= player_speed
    if keys[pygame.K_DOWN] and player_y + player_radius < HEIGHT:
        player_y += player_speed
    if random.randint(1, enemy_spawn_rate) == 1:
        enemy_y = random.randint(0, HEIGHT - enemy_height)
        rect = pygame.Rect(-enemy_width, enemy_y, enemy_width, enemy_height)
        enemies.append(rect)
    for rect in enemies[:]: 
        rect.x += enemy_speed
        if rect.x > WIDTH:
            enemies.remove(rect)
    player_rect = pygame.Rect(player_x - player_radius, player_y - player_radius, 
                              player_radius * 2, player_radius * 2)
    for rect in enemies:
        if player_rect.colliderect(rect):
            print("lose")
            running = False
    screen.fill(WHITE)
    pygame.draw.circle(screen, BLUE, (player_x, player_y), player_radius)
    for rect in enemies:
        pygame.draw.rect(screen, RED, rect)
    pygame.display.flip()
    clock.tick(60)
pygame.quit()
sys.exit()