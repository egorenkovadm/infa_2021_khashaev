import pygame
from pygame.draw import *


pygame.init()

screen = pygame.display.set_mode((400, 400))

circle(screen, (255, 255, 0), (200, 200), 150)

circle(screen, (255, 0, 0), (140, 150), 30)
circle(screen, (255, 0, 0), (260, 150), 20)

circle(screen, (0, 0, 0), (140, 150), 8)
circle(screen, (0, 0, 0), (260, 150), 8)

polygon(screen, (0, 0, 0), [(110, 90), (190, 140)], 20)
polygon(screen, (0, 0, 0), [(300, 110), (210, 140)], 20)

polygon(screen, (0, 0, 0), [(125, 260), (275, 260)], 20)

pygame.display.update()
clock = pygame.time.Clock()
finished = False

while not finished:
    clock.tick(30)
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            finished = True
            
pygame.quit()