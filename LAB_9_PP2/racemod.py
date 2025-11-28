# Imports
import pygame, sys
from pygame.locals import *
import random, time

# Инициализация pygame
pygame.init()

# Настройка FPS
FPS = 60
FramePerSec = pygame.time.Clock()

# Цвета
BLUE  = (0, 0, 255)
RED   = (255, 0, 0)
GREEN = (0, 255, 0)
BLACK = (0, 0, 0)
WHITE = (255, 255, 255)

# Основные переменные
SCREEN_WIDTH = 400
SCREEN_HEIGHT = 600
SPEED = 5              # начальная скорость врага и движения потока
SCORE = 0              # очки за проезд врагов
COINS = 0              # общий счёт монет (с учётом веса)
COINS_FOR_SPEEDUP = 5  # каждые N монет увеличиваем скорость
next_speedup_at = COINS_FOR_SPEEDUP  # порог для следующего ускорения

# Шрифты
font = pygame.font.SysFont("Verdana", 60)
font_small = pygame.font.SysFont("Verdana", 20)
game_over = font.render("Game Over", True, BLACK)

# Задний фон
background = pygame.image.load("AnimatedStreet.png")

# Иконка монеты для UI
_coin_icon = pygame.image.load("coin.png")
_coin_icon = pygame.transform.scale(_coin_icon, (20, 20))

# Окно программы
DISPLAYSURF = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
DISPLAYSURF.fill(WHITE)
pygame.display.set_caption("Game")


class Enemy(pygame.sprite.Sprite):
    # Машина-противник
    def __init__(self):
        super().__init__()
        self.image = pygame.image.load("redcar.png")
        self.rect = self.image.get_rect()
        # Появляется сверху в случайной позиции по X
        self.rect.center = (random.randint(40, SCREEN_WIDTH - 40), 0)

    def move(self):
        # Двигаем врага вниз
        global SCORE
        self.rect.move_ip(0, SPEED)
        # Если вышел за нижнюю границу — возвращаем вверх и даём очко
        if self.rect.top > SCREEN_HEIGHT:
            SCORE += 1
            self.rect.top = 0
            self.rect.center = (random.randint(40, SCREEN_WIDTH - 40), 0)


class Player(pygame.sprite.Sprite):
    # Машина-игрок
    def __init__(self):
        super().__init__()
        self.image = pygame.image.load("Player.png")
        self.rect = self.image.get_rect()
        # Стартовая позиция игрока
        self.rect.center = (160, 520)

    def move(self):
        # Управление машиной по стрелкам влево/вправо
        pressed_keys = pygame.key.get_pressed()

        # Вверх/вниз отключены, как в оригинале
        # if pressed_keys[K_UP]:
        #     self.rect.move_ip(0, -5)
        # if pressed_keys[K_DOWN]:
        #     self.rect.move_ip(0, 5)

        # Двигаемся влево, если не выходим за левую границу
        if self.rect.left > 0:
            if pressed_keys[K_LEFT]:
                self.rect.move_ip(-5, 0)

        # Двигаемся вправо, если не выходим за правую границу
        if self.rect.right < SCREEN_WIDTH:
            if pressed_keys[K_RIGHT]:
                self.rect.move_ip(5, 0)


class Coin(pygame.sprite.Sprite):
    # Монета, которая падает сверху
    def __init__(self):
        super().__init__()
        img = pygame.image.load("coin.png")

        # Случайный вес монеты: 1, 2 или 3
        # Вес = сколько монет добавится к счёту при подборе
        self.weight = random.choice([1, 2, 3])

        # В зависимости от веса меняем размер монеты,
        # чтобы визуально они хоть немного отличались
        size_by_weight = {
            1: 20,  # лёгкая монета
            2: 26,  # средняя
            3: 32   # тяжёлая
        }
        size = size_by_weight[self.weight]

        self.image = pygame.transform.scale(img, (size, size))
        self.rect = self.image.get_rect()

        # Случайная позиция по X
        self.rect.centerx = random.randint(30, SCREEN_WIDTH - 30)
        # Появляется немного выше экрана, чтобы "падала"
        self.rect.y = -random.randint(40, 200)

    def move(self):
        # Скорость падения монеты (чуть меньше, чем у врагов)
        fall_speed = max(2, SPEED // 2)
        self.rect.move_ip(0, fall_speed)

        # Если монета вышла за экран снизу — удаляем её
        if self.rect.top > SCREEN_HEIGHT:
            self.kill()


# Создаём спрайты игрока и одного врага
P1 = Player()
E1 = Enemy()

# Группа врагов
enemies = pygame.sprite.Group()
enemies.add(E1)

# Группа всех спрайтов (игрок, враги, монеты)
all_sprites = pygame.sprite.Group()
all_sprites.add(P1)
all_sprites.add(E1)

# Группа только монет
coinss = pygame.sprite.Group()

# Событие для спавна монет
COIN_SPAWN = pygame.USEREVENT + 1
pygame.time.set_timer(COIN_SPAWN, 1200)  # каждые 1.2 секунды
MAX_COINS_ON_SCREEN = 4                  # максимум монет на экране


# Главный игровой цикл
while True:
    # Обработка событий
    for event in pygame.event.get():
        # Спавн новой монеты по таймеру
        if event.type == COIN_SPAWN:
            # Не спавним слишком много монет сразу
            if len(coinss) < MAX_COINS_ON_SCREEN:
                c = Coin()
                coinss.add(c)
                all_sprites.add(c)

        if event.type == QUIT:
            pygame.quit()
            sys.exit()

    # Рисуем фон
    DISPLAYSURF.blit(background, (0, 0))

    # Рисуем счёт (очки за врагов) слева сверху
    scores = font_small.render(str(SCORE), True, BLACK)
    DISPLAYSURF.blit(scores, (10, 10))

    # Рисуем количество монет справа сверху + иконка
    coins_text = font_small.render(str(COINS), True, BLACK)
    coins_text_x = SCREEN_WIDTH - 10 - coins_text.get_width()
    DISPLAYSURF.blit(_coin_icon,
                     (coins_text_x - 6 - _coin_icon.get_width(), 10))
    DISPLAYSURF.blit(coins_text, (coins_text_x, 10))

    # Двигаем и перерисовываем все спрайты
    for entity in all_sprites:
        DISPLAYSURF.blit(entity.image, entity.rect)
        entity.move()

    # Проверка столкновения игрока с врагом
    if pygame.sprite.spritecollideany(P1, enemies):
        # Экран Game Over
        DISPLAYSURF.fill(RED)
        DISPLAYSURF.blit(game_over, (30, 250))

        pygame.display.update()
        # Удаляем все спрайты и выходим
        for entity in all_sprites:
            entity.kill()
        time.sleep(2)
        pygame.quit()
        sys.exit()

    # Столкновение игрока с монетами
    # dokill=True — собранные монеты удаляются
    collected = pygame.sprite.spritecollide(P1, coinss, dokill=True)
    if collected:
        # Добавляем к счёту вес каждой монеты
        for coin in collected:
            COINS += coin.weight

        # Увеличиваем скорость врагов, если набрали достаточно монет
        # Например, каждые 5 монет SPEED + 1
        if COINS >= next_speedup_at:
            SPEED += 1
            # Следующий порог: ещё +5 монет
            next_speedup_at += COINS_FOR_SPEEDUP

    # Обновляем экран
    pygame.display.flip()
    FramePerSec.tick(FPS)