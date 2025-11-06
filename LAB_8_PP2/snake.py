import pygame, random, sys

pygame.init()

CELL = 20
W, H = 30 * CELL, 20 * CELL
FPS = 10

BG = (18, 18, 18)
SNAKE = (0, 200, 0)
FOOD = (200, 0, 0)
TXT = (220, 220, 220)

screen = pygame.display.set_mode((W, H))
clock = pygame.time.Clock()
font = pygame.font.SysFont(None, 36)

def draw_cell(pos, color):
    x, y = pos
    pygame.draw.rect(screen, color, (x * CELL, y * CELL, CELL, CELL))

def spawn_food(body):
    while True:
        p = (random.randrange(W // CELL), random.randrange(H // CELL))
        if p not in body: return p

def game_loop():
    snake = [(W // CELL // 2, H // CELL // 2)]
    dir_ = (1, 0)
    food = spawn_food(snake)
    score = 0
    game_over = False

    while True:
        for e in pygame.event.get():
            if e.type == pygame.QUIT:
                pygame.quit(); sys.exit()
            if e.type == pygame.KEYDOWN:
                if not game_over:
                    if e.key in (pygame.K_w, pygame.K_UP)   and dir_ != (0, 1):  dir_ = (0, -1)
                    elif e.key in (pygame.K_s, pygame.K_DOWN) and dir_ != (0,-1): dir_ = (0, 1)
                    elif e.key in (pygame.K_a, pygame.K_LEFT) and dir_ != (1, 0): dir_ = (-1, 0)
                    elif e.key in (pygame.K_d, pygame.K_RIGHT)and dir_ != (-1,0): dir_ = (1, 0)
                else:
                    if e.key == pygame.K_r: return True
                    if e.key in (pygame.K_q, pygame.K_ESCAPE):
                        pygame.quit(); sys.exit()

        if not game_over:
            hx, hy = snake[0]
            nx, ny = hx + dir_[0], hy + dir_[1]
            cols, rows = W // CELL, H // CELL
            if not (0 <= nx < cols and 0 <= ny < rows) or (nx, ny) in snake:
                game_over = True
            else:
                snake.insert(0, (nx, ny))
                if (nx, ny) == food:
                    score += 1
                    food = spawn_food(snake)
                else:
                    snake.pop()

        screen.fill(BG)
        for seg in snake: draw_cell(seg, SNAKE)
        draw_cell(food, FOOD)

        screen.blit(font.render(f"Score: {score}", True, TXT), (10, 10))
        if game_over:
            msg = "Game Over! R=Restart  Q=Quit"
            surf = font.render(msg, True, TXT)
            screen.blit(surf, surf.get_rect(center=(W // 2, H // 2)))

        pygame.display.flip()
        clock.tick(FPS)

while True:
    if not game_loop(): break
