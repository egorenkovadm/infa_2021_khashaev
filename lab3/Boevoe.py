import pygame
from pygame.draw import *


pygame.init()


screen = pygame.display.set_mode((600, 402))

brown = (153, 51, 0)
# Sand, water and air
rect(screen, (255, 255, 0), (0, 275, 600, 127))
rect(screen, (0, 0, 255), (0, 175, 600, 100))
rect(screen, (0, 255, 255), (0, 0, 600, 175))
# Sun
circle(screen, (255, 255, 0), (500, 75), 50)
# Cloud
def cloud(x, y, e, k):
    r = 25 * k
    g = 0.8
    for i in range(4):
        ellipse(screen, (255, 255, 255), [x + g * r * i, y - r, e * r, r], 0)
        ellipse(screen, (0, 0, 0), [x + g * r * i, y - r, e * r, r], 1)
    for i in range(3):
        ellipse(screen, (255, 255, 255), [x + g * r * (i + 1 / 2), y - r / 2, e * r, r], 0)
        ellipse(screen, (0, 0, 0), [x + g * r * (i + 1 / 2), y - r / 2, e * r, r], 1)    
    return None
cloud(90, 50, 1, 1.2)
# Umbrella
def umbrella(x, y, k): #x, y - coordinates of left bottom corner of stick, k - scale
    h = 150 * k #Heith of stick
    w = 8 * k #Width of stick
    rect(screen, (153, 51, 0), (x, y - h, w, h))
    wt = 70 * k #Width of hat
    polygon(screen, (255, 0, 0), 
    [(x - wt + w / 2, y - 5 * h / 6), (x + w / 2, y - h * 1.05), (x + wt + w / 2, y - 5 * h / 6), (x - wt + w / 2, y - 5 * h / 6)])
    for i in range(8):
        line(screen, (125, 40, 0), (x + w / 2, y - h * 1.05), (x - wt + w / 2 + i * wt * 2 / 8, y - 5 * h / 6))
    return None
umbrella(75, 375, 1)
# Ship
def ship(x, y, k):
    r = 25 * k #Radius of back
    circle(screen, (153, 51, 0), (x + r, y - r), r)
    rect(screen, (0, 0, 255), (x, y - 2 * r, 2 * r, r))
    rect(screen, (0, 0, 255), (x + r, y - r, r, r))
    w = 100 * k #Width of corpus
    rect(screen, (153, 51, 00), (x + r, y - r, w, r))
    line(screen, (0, 0, 0), (x + r, y - r), (x + r, y))
    a = 60 * k #Lenth of corma
    polygon(screen, brown, [(x + r + w, y - r), (x + r + w + a, y - r), (x + r + w, y), (x + r + w, y - r)])
    line(screen, (0, 0, 0), (x + r + w, y - r), (x + r + w, y))
    h = 90 * k #Heith of stick
    ws = 8 * k #Width of stick
    rect(screen, (0, 0, 0), (x + r + w * 0.5, y - r - h, ws, h))
    b = 60 * k #Width of parus
    xp = x + r + w * 0.5 + ws # x coordinate of left upper corner of parus
    polygon(screen, (200, 200, 200),
    [(xp, y - r - h), (xp + b, y - r - h / 2), (xp, y - r), (xp + b * 0.3, y - r - h / 2), (xp, y - r - h)])
    line(screen, (0, 0, 0), (xp + 0.3 *  b, y - r - h / 2), (xp + b, y - r - h / 2))
    circle(screen, (0, 0, 0), (x + r + w + 0.5 * r, y - r * 0.55), r * 0.35)
    circle(screen, (255, 255, 255), (x + r + w + 0.5 * r, y - r * 0.55), r * 0.2)
    return None
ship(200, 250, 1)

pygame.display.update()
clock = pygame.time.Clock()
finished = False

while not finished:
    clock.tick(60)
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            finished = True