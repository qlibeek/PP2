import pygame, random, sys

pygame.init()

CELL = 20
W, H = 30 * CELL, 20 * CELL

BASE_FPS = 10
FPS = BASE_FPS

BG   = (18, 18, 18)
SNAKE = (0, 200, 0)
FOOD  = (200, 0, 0)
TXT   = (220, 220, 220)

screen = pygame.display.set_mode((W, H))
clock = pygame.time.Clock()
font = pygame.font.SysFont(None, 36)

# еда может давать разное количество очков
FOOD_WEIGHTS = [1, 2, 3]
# еда исчезает через это время
FOOD_LIFETIME_MS = 4000

LEVEL_STEP = 5  


def draw_cell(pos, color):
    x, y = pos
    pygame.draw.rect(screen, color, (x * CELL, y * CELL, CELL, CELL))


def spawn_food(body):
    # находим свободную клетку + выбираем случайный вес + время исчезновения
    while True:
        p = (random.randrange(W // CELL), random.randrange(H // CELL))
        if p not in body:
            return {
                "pos": p,
                "weight": random.choice(FOOD_WEIGHTS),
                "expires_at": pygame.time.get_ticks() + FOOD_LIFETIME_MS
            }


def game_loop():
    global FPS

    snake = [(W // CELL // 2, H // CELL // 2)]
    dir_ = (1, 0)

    level = 1
    score = 0
    game_over = False

    food = spawn_food(snake)

    FPS = BASE_FPS + (level - 1) * 2

    while True:

        for e in pygame.event.get():
            if e.type == pygame.QUIT:
                pygame.quit(); sys.exit()

            if e.type == pygame.KEYDOWN:
                if not game_over:
                    # обычное управление
                    if e.key in (pygame.K_w, pygame.K_UP) and dir_ != (0, 1):
                        dir_ = (0, -1)
                    elif e.key in (pygame.K_s, pygame.K_DOWN) and dir_ != (0, -1):
                        dir_ = (0, 1)
                    elif e.key in (pygame.K_a, pygame.K_LEFT) and dir_ != (1, 0):
                        dir_ = (-1, 0)
                    elif e.key in (pygame.K_d, pygame.K_RIGHT) and dir_ != (-1, 0):
                        dir_ = (1, 0)
                
        if not game_over:
            hx, hy = snake[0]
            nx, ny = hx + dir_[0], hy + dir_[1]

            # проверка стены и самопересечения
            if not (0 <= nx < W // CELL and 0 <= ny < H // CELL) or (nx, ny) in snake:
                game_over = True
            else:
                snake.insert(0, (nx, ny))

                # еда съедена
                if (nx, ny) == food["pos"]:
                    score += food["weight"]

                    # уровень растёт каждые N очков
                    if score >= level * LEVEL_STEP:
                        level += 1
                        FPS = BASE_FPS + (level - 1) * 2

                    food = spawn_food(snake)
                else:
                    snake.pop()

            # если еда просрочена — создаём новую
            if pygame.time.get_ticks() >= food["expires_at"]:
                food = spawn_food(snake)

        # рисуем всё
        screen.fill(BG)

        for seg in snake:
            draw_cell(seg, SNAKE)

        draw_cell(food["pos"], FOOD)

        # текст
        screen.blit(font.render(f"Score: {score}", True, TXT), (10, 10))
        screen.blit(font.render(f"Level: {level}", True, TXT), (10, 40))
        screen.blit(font.render(f"Food: {food['weight']}", True, TXT), (10, 70))

        if game_over:
            surf = font.render("GAME OVER", True, TXT)
            screen.blit(surf, surf.get_rect(center=(W // 2, H // 2)))

        pygame.display.flip()
        clock.tick(FPS)


while True:
    if not game_loop():
        break