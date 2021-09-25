import pygame
from pygame.draw import *
import numpy as np


pygame.init()


screen = pygame.display.set_mode((600, 402))

brown = (153, 51, 0)
# Sand, water and air
rect(screen, (255, 255, 0), (0, 275, 600, 127))
rect(screen, (0, 0, 255), (0, 175, 600, 100))
rect(screen, (0, 255, 255), (0, 0, 600, 175))
# Sun
circle(screen, (255, 255, 0), (500, 75), 50)
n = 7
r = 60
def triangle(a):
    polygon(screen, (255, 255, 0),
    [(500 + r * np.cos(2 * np.pi / n + a), 75 + r * np.sin(2 * np.pi / n + a)),
    (500 + r * np.cos(2 * np.pi / n + a + 2 * np.pi / 3), 75 + r * np.sin(2 * np.pi / n + a + 2 * np.pi / 3)),
    (500 + r * np.cos(2 * np.pi / n + a + 4 * np.pi / 3), 75 + r * np.sin(2 * np.pi / n + a + 4 * np.pi / 3)),
    (500 + r * np.cos(2 * np.pi / n + a), 75 + r * np.sin(2 * np.pi / n + a))])
    return None
for i in range(n):
    triangle(i * 2 * np.pi / 3 / n)
#for i in range(n):
#    line(screen, (255, 255, 0),
#    (500 + r * np.cos(2 * np.pi / n * i), 75 + r * np.sin(2 * np.pi / n * i)),
#    (500 + r * np.cos(2 * np.pi / n * (i + 1)), 75 + r * np.sin(2 * np.pi / n * (i + 1))), 4)
#for i in range(n):
#    line(screen, (255, 255, 0),
#    (500 + r * np.cos(2 * np.pi / n * (i + 0.5)), 75 + r * np.sin(2 * np.pi / n * (i + 0.5))),
#    (500 + r * np.cos(2 * np.pi / n * (i + 1.5)), 75 + r * np.sin(2 * np.pi / n * (i + 1.5))), 4)
triangle(0)
# Wave
for i in range(7):
    ellipse(screen, (255, 255, 0), ((i * 2) * 600 / 14, 265, 600 / 14, 20))
    ellipse(screen, (0, 0, 255), ((i * 2 + 1) * 600 / 14, 265, 600 / 14, 20))
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

ship(130, 210, 0.6)
ship(350, 230, 1)

cloud(110, 50, 1, 1)
cloud(230, 80, 1.1, 1.4)
cloud(50, 130, 1.5, 1.3)

umbrella(70, 340, 1)
umbrella(200, 350, 0.8)

pygame.display.update()
clock = pygame.time.Clock()
finished = False

while not finished:
    clock.tick(60)
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            finished = True