import pygame
import random
import sys

pygame.init()
FPS = 60
FramePerSec = pygame.time.Clock()

BLUE  = (0, 0, 255)
RED   = (255, 0, 0)
GREEN = (0, 255, 0)
BLACK = (0, 0, 0)
WHITE = (255, 255, 255)

SCREEN_WIDTH = 400
SCREEN_HEIGHT = 600
SPEED = 5              
SCORE = 0              
TRIANGLE = 0              
TRIANGLE_FOR_SPEEDUP = 5  
next_speedup_at = TRIANGLE_FOR_SPEEDUP 
DISPLAYSURF = pygame.display.set_mode(400, 600)

font = pygame.font.SysFont("Verdana", 60)
font_small = pygame.font.SysFont("Verdana", 20)
game_over = font.render("Game Over", True, BLACK)

