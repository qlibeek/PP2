import pygame
import random
import sys

pygame.init()

WIDTH, HEIGHT = 800, 600
screen = pygame.display.set_mode((WIDTH, HEIGHT))
clock = pygame.time.Clock()

BLUE  = (0, 0, 255)
RED   = (255, 0, 0)
GREEN = (0, 255, 0)
BLACK = (0, 0, 0)
WHITE = (255, 255, 255)

player_w = 150
player_h = 20
player_x = WIDTH // 2 - player_w // 2
player_y = HEIGHT - 60
player_speed = 7

triangles = []
tri_size = 30
tri_speed_min = 2
tri_speed_max = 4
spawn_rate = 20

score = 0
font = pygame.font.SysFont(None, 36)

running = True
while running:
    for e in pygame.event.get():
        if e.type == pygame.QUIT:
            running = False

    keys = pygame.key.get_pressed()
    if keys[pygame.K_LEFT] and player_x > 0:
        player_x -= player_speed
    if keys[pygame.K_RIGHT] and player_x + player_w < WIDTH:
        player_x += player_speed

    if random.randint(1, spawn_rate) == 1:
        x = random.randint(tri_size, WIDTH - tri_size)
        y = -tri_size
        dy = random.randint(tri_speed_min, tri_speed_max)
        rect = pygame.Rect(x - tri_size // 2, y, tri_size, tri_size)
        triangles.append([rect, dy])

    for t in triangles[:]:
        t[0].y += t[1]
        if t[0].top > HEIGHT:
            triangles.remove(t)

    player_rect = pygame.Rect(player_x, player_y, player_w, player_h)
    for t in triangles[:]:
        if player_rect.colliderect(t[0]):
            score += 1
            triangles.remove(t)

    screen.fill(WHITE)
    pygame.draw.rect(screen, BLUE, player_rect)

    for t in triangles:
        r = t[0]
        p1 = (r.centerx, r.top)
        p2 = (r.left, r.bottom)
        p3 = (r.right, r.bottom)
        pygame.draw.polygon(screen, RED, [p1, p2, p3])

    text = font.render(f"Score: {score}", True, BLACK)
    screen.blit(text, (10, 10))

    pygame.display.flip()
    clock.tick(60)

pygame.quit()
sys.exit()
