#Imports
import pygame, sys
from pygame.locals import *
import random, time
 
#Initialzing 
pygame.init()
 
#Setting up FPS 
FPS = 60
FramePerSec = pygame.time.Clock()
 
#Creating colors
BLUE  = (0, 0, 255)
RED   = (255, 0, 0)
GREEN = (0, 255, 0)
BLACK = (0, 0, 0)
WHITE = (255, 255, 255)
 
#Other Variables for use in the program
SCREEN_WIDTH = 400
SCREEN_HEIGHT = 600
SPEED = 5
SCORE = 0
COINS = 0  # NEW: счётчик монет
 
#Setting up Fonts
font = pygame.font.SysFont("Verdana", 60)
font_small = pygame.font.SysFont("Verdana", 20)
game_over = font.render("Game Over", True, BLACK)
 
background = pygame.image.load("AnimatedStreet.png")

#EXTRA: иконка монеты для UI (справа сверху)
_coin_icon = pygame.image.load("coin.png")
_coin_icon = pygame.transform.scale(_coin_icon, (20, 20))
 
#Create a white screen 
DISPLAYSURF = pygame.display.set_mode((400,600))
DISPLAYSURF.fill(WHITE)
pygame.display.set_caption("Game")
 
class Enemy(pygame.sprite.Sprite):
      def __init__(self):
        super().__init__() 
        self.image = pygame.image.load("redcar.png")
        self.rect = self.image.get_rect()
        self.rect.center = (random.randint(40, SCREEN_WIDTH-40), 0)  
 
      def move(self):
        global SCORE
        self.rect.move_ip(0,SPEED)
        if (self.rect.top > 600):
            SCORE += 1
            self.rect.top = 0
            self.rect.center = (random.randint(40, SCREEN_WIDTH - 40), 0)
 
class Player(pygame.sprite.Sprite):
    def __init__(self):
        super().__init__() 
        self.image = pygame.image.load("Player.png")
        self.rect = self.image.get_rect()
        self.rect.center = (160, 520)
        
    def move(self):
        pressed_keys = pygame.key.get_pressed()
       #if pressed_keys[K_UP]:
            #self.rect.move_ip(0, -5)
        #if pressed_keys[K_DOWN]:
            #self.rect.move_ip(0,5)
         
        if self.rect.left > 0:
              if pressed_keys[K_LEFT]:
                  self.rect.move_ip(-5, 0)
        if self.rect.right < SCREEN_WIDTH:        
              if pressed_keys[K_RIGHT]:
                  self.rect.move_ip(5, 0)

# NEW: класс монеты — падает сверху вниз и удаляется при выходе за экран
class Coin(pygame.sprite.Sprite):
    def __init__(self):
        super().__init__()
        img = pygame.image.load("coin.png")
        self.image = pygame.transform.scale(img, (28, 28))
        self.rect = self.image.get_rect()
        self.rect.centerx = random.randint(30, SCREEN_WIDTH - 30)
        self.rect.y = -random.randint(40, 200)  # появление выше экрана

    def move(self):
        fall_speed = max(2, SPEED // 2)  # монеты падают чуть медленнее потока
        self.rect.move_ip(0, fall_speed)
        if self.rect.top > SCREEN_HEIGHT:
            self.kill()  # убрать, если ушла за низ

#Setting up Sprites        
P1 = Player()
E1 = Enemy()
 
#Creating Sprites Groups
enemies = pygame.sprite.Group()
enemies.add(E1)
all_sprites = pygame.sprite.Group()
all_sprites.add(P1)
all_sprites.add(E1)

# EXTRA: группа для монет
coinss = pygame.sprite.Group()
 
#Adding a new User event 
INC_SPEED = pygame.USEREVENT + 1
pygame.time.set_timer(INC_SPEED, 1000)

# EXTRA: таймер для случайного появления монет
COIN_SPAWN = pygame.USEREVENT + 2
pygame.time.set_timer(COIN_SPAWN, 1200)  # раз в ~1.2 сек
MAX_COINS_ON_SCREEN = 4  # небольшой лимит
 
#Game Loop
while True:
    #Cycles through all events occurring  
    for event in pygame.event.get():
        if event.type == INC_SPEED:
              SPEED += 0.5
        # NEW: спавним монету по таймеру
        if event.type == COIN_SPAWN:
              if len(coinss) < MAX_COINS_ON_SCREEN:
                  c = Coin()
                  coinss.add(c)
                  all_sprites.add(c)
        if event.type == QUIT:
            pygame.quit()
            sys.exit()
 
    DISPLAYSURF.blit(background, (0,0))

    # score слева сверху
    scores = font_small.render(str(SCORE), True, BLACK)
    DISPLAYSURF.blit(scores, (10,10))

    # EXTRA: coins справа сверху с иконкой
    coins_text = font_small.render(str(COINS), True, BLACK)
    coins_text_x = SCREEN_WIDTH - 10 - coins_text.get_width()
    DISPLAYSURF.blit(_coin_icon, (coins_text_x - 6 - _coin_icon.get_width(), 10))
    DISPLAYSURF.blit(coins_text, (coins_text_x, 10))
 
    #Moves and Re-draws all Sprites
    for entity in all_sprites:
        DISPLAYSURF.blit(entity.image, entity.rect)
        entity.move()
 
    #To be run if collision occurs between Player and Enemy
    if pygame.sprite.spritecollideany(P1, enemies):
          try:
              pygame.mixer.Sound('crash.wav').play()
          except Exception:
              pass
          time.sleep(0.5)
                    
          DISPLAYSURF.fill(RED)
          DISPLAYSURF.blit(game_over, (30,250))
           
          pygame.display.update()
          for entity in all_sprites:
                entity.kill() 
          time.sleep(2)
          pygame.quit()
          sys.exit()

    # EXTRA: столкновения с монетами — увеличиваем счёт и удаляем собранные
    collected = pygame.sprite.spritecollide(P1, coinss, dokill=True)
    if collected:
        COINS += len(collected)
        
    pygame.display.update()
    FramePerSec.tick(FPS)
