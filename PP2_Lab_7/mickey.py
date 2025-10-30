import pygame 
import time
import math
pygame.init()


screen = pygame.display.set_mode((800, 600))
clock = pygame.time.Clock()


pygame.display.set_caption("Mickey clock")

mainclock = pygame.transform.scale(pygame.image.load(r"C:\Users\burak\OneDrive\Изображения\base_micky.jpg"), (800, 600)).convert()

leftarm = pygame.image.load(r"C:\Users\burak\OneDrive\Изображения\second.png").convert_alpha()
rightarm = pygame.image.load(r"C:\Users\burak\OneDrive\Изображения\minute.png").convert_alpha()

done = False

while not done: 
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            done = True
    
    current_time = time.localtime()
    minute = current_time.tm_min
    second = current_time.tm_sec
    
    
    minute_angle = minute * 6    + (second / 60) * 6   
    second_angle = second * 6  
    
    rotated_rightarm = pygame.transform.rotate(rightarm, -minute_angle)
    rightarmrect = rotated_rightarm.get_rect(center=(800 // 2, 600 // 2 + 12))
    
    rotated_leftarm = pygame.transform.rotate(leftarm, -second_angle)
    leftarmrect = rotated_leftarm.get_rect(center=(800 // 2, 600 // 2 + 10))
    
    
    screen.blit(mainclock, (0,0))
    screen.blit(rotated_rightarm, rightarmrect)
    screen.blit(rotated_leftarm, leftarmrect)
    
    pygame.display.update()
    clock.tick(60)
    
pygame.quit()