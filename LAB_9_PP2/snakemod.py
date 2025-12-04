import time
import pygame, random, sys
import psycopg2
from configparser import ConfigParser


def load_config(filename='database.ini', section='postgresql'):
    parser = ConfigParser()
    parser.read(filename, encoding='utf-8')
    config = {}
    if parser.has_section(section):
        for k, v in parser.items(section):
            config[k] = v
    return config

def get_connection():
    return psycopg2.connect(**load_config())

def init_database():
    conn = get_connection()
    with conn, conn.cursor() as cur:
        cur.execute("""
            CREATE TABLE IF NOT EXISTS game_user (
                id SERIAL PRIMARY KEY,
                username VARCHAR(50) UNIQUE NOT NULL,
                level INTEGER NOT NULL DEFAULT 1
            );
        """)

        cur.execute("""
            CREATE TABLE IF NOT EXISTS user_score (
                id SERIAL PRIMARY KEY,
                user_id INTEGER REFERENCES game_user(id) ON DELETE CASCADE,
                score INTEGER NOT NULL,
                level INTEGER NOT NULL,
                created_at TIMESTAMP DEFAULT NOW()
            );
        """)
    conn.commit()
    conn.close()
    print("Database is ready.")

def get_or_create_user(username):
    conn = get_connection()
    with conn, conn.cursor() as cur:
        cur.execute("SELECT id, level FROM game_user WHERE username=%s", (username,))
        row = cur.fetchone()
        if row:
            conn.close()
            return row[0], row[1]
        cur.execute("INSERT INTO game_user(username, level) VALUES(%s, %s) RETURNING id, level", (username,1))
        user_id, level = cur.fetchone()
        conn.commit()
    conn.close()
    return user_id, level

def save_game_state(username, level, score):
    conn = get_connection()
    with conn, conn.cursor() as cur:
        cur.execute("SELECT id, level FROM game_user WHERE username=%s", (username,))
        user_id, current_level = cur.fetchone()
        if level > current_level:
            cur.execute("UPDATE game_user SET level=%s WHERE id=%s", (level, user_id))
        cur.execute("""
    INSERT INTO user_score(user_id, username, score, level)
    VALUES(%s, %s, %s, %s)
""", (user_id, username, score, level))

    conn.commit()
    conn.close()

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

FOOD_WEIGHTS = [1,2,3]
FOOD_LIFETIME_MS = 4000
LEVEL_STEP = 5

def draw_cell(pos, color):
    x, y = pos
    pygame.draw.rect(screen, color, (x*CELL, y*CELL, CELL, CELL))

def spawn_food(body):
    while True:
        p = (random.randrange(W//CELL), random.randrange(H//CELL))
        if p not in body:
            return {"pos": p, "weight": random.choice(FOOD_WEIGHTS), "expires": pygame.time.get_ticks() + FOOD_LIFETIME_MS}

def game_loop(username, start_level=1):
    global FPS

    snake = [(W//CELL//2, H//CELL//2)]
    direction = (1,0)
    level = start_level
    score = 0
    game_over = False

    food = spawn_food(snake)
    FPS = BASE_FPS + (level-1)*2

    time.sleep(5)

    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                save_game_state(username, level, score)
                pygame.quit(); sys.exit()

            if event.type == pygame.KEYDOWN:
                if not game_over:
                    if event.key in (pygame.K_w, pygame.K_UP) and direction != (0,1):
                        direction = (0,-1)
                    elif event.key in (pygame.K_s, pygame.K_DOWN) and direction != (0,-1):
                        direction = (0,1)
                    elif event.key in (pygame.K_a, pygame.K_LEFT) and direction != (1,0):
                        direction = (-1,0)
                    elif event.key in (pygame.K_d, pygame.K_RIGHT) and direction != (-1,0):
                        direction = (1,0)

                if event.key == pygame.K_r and game_over:
                    save_game_state(username, level, score)
                    return True

                if event.key == pygame.K_ESCAPE:
                    save_game_state(username, level, score)
                    return False

        if not game_over:
            hx, hy = snake[0]
            nx, ny = hx + direction[0], hy + direction[1]

            if not (0<=nx<W//CELL and 0<=ny<H//CELL) or (nx,ny) in snake:
                game_over = True
            else:
                snake.insert(0,(nx,ny))
                if (nx,ny)==food["pos"]:
                    score += food["weight"]
                    if score >= level * LEVEL_STEP:
                        level += 1
                        FPS = BASE_FPS + (level-1)*2
                    food = spawn_food(snake)
                else:
                    snake.pop()

            if pygame.time.get_ticks() >= food["expires"]:
                food = spawn_food(snake)

        screen.fill(BG)
        for seg in snake:
            draw_cell(seg, SNAKE)
        draw_cell(food["pos"], FOOD)

        screen.blit(font.render(f"Score: {score}", True, TXT),(10,10))
        screen.blit(font.render(f"Level: {level}", True, TXT),(10,40))

        if game_over:
            t = font.render("GAME OVER — Press R to Save", True, TXT)
            screen.blit(t, t.get_rect(center=(W//2,H//2)))

        pygame.display.flip()
        clock.tick(FPS)


print("Initializing database...")
init_database()

username = input("Enter username: ")
user_id, user_level = get_or_create_user(username)
print(f"Welcome {username}, starting at level {user_level}")

while True:
    if not game_loop(username, user_level):
        break

