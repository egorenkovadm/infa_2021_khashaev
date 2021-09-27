import pygame
from pygame.draw import *
import numpy as np


pygame.init()


screen = pygame.display.set_mode((600, 402))

#colors
black = (0,0,0)
sand_color = (255, 232, 173)
water_color = (0, 0, 205)
sun_color = (245, 235, 30)

#Functions for drawing objects

# Sun
def sun(x,y,n,r,sun_color):
    '''
    Function draws a sun - circle with n*3 rays
    x,y - coordinates of center of circle
    n*3 - number of rays
    sun_color - color of sun
    '''

    circle(screen, sun_color, (x, y), 50)
    
    def triangle(a):
        '''
        Function draws a equilateral triangle
        a - integer
        '''
        polygon(screen, sun_color,
        [(x + r * np.cos(2 * np.pi / n + a),
        y + r * np.sin(2 * np.pi / n + a)),
        (x + r * np.cos(2 * np.pi / n + a + 2 * np.pi / 3),
        y + r * np.sin(2 * np.pi / n + a + 2 * np.pi / 3)),
        (x + r * np.cos(2 * np.pi / n + a + 4 * np.pi / 3),
        y + r * np.sin(2 * np.pi / n + a + 4 * np.pi / 3))])

    triangle(0)
    for i in range(n):
       triangle((i * 2 * np.pi / 3 / n))



# Cloud
def cloud(surface, x, y, e, k, color_fill, color_border):
    '''
    Function draws a cloud of ellipses on the screen
    surface - an object pygame.surface
    x,y - coordinates of center of left border
    e - radius * e = width of ellipse
    k - r*k = radius of circle
    color_fill - color of ellipses' fill
    color_border - color of ellipses' border
    '''
    r = 25 * k
    g = 0.8
    for i in range(4):
        ellipse(surface, color_border, [x + g * r * i, y - r, e * r, r], 0)
        ellipse(surface, color_fill, [x + g * r * i, y - r, e * r, r], 1)
    for i in range(3):
        ellipse(surface, color_border, [x + g * r * (i + 1 / 2),
                y - r / 2, e * r, r], 0)
        ellipse(surface, color_fill, [x + g * r * (i + 1 / 2),
                y - r / 2, e * r, r], 1)    

# Umbrella
def umbrella(surface,x, y, k,color_hat,color_stick,color_strip):  
    '''
    Function draws an umbrella
    surface - an object pygame.surface
    x,y - coordinates of left bottom corner of stick
    k - scale
    color_hat - color of umbrella's hat
    color_stick - color of umbrella's stick
    color_strip - color of strips on a hat
    '''
    h = 150 * k #Heith of stick
    w = 8 * k #Width of stick
    stick(surface,h,w,x,y,color_stick)
    umbrella_hat(surface,x,y,k,h,w,color_hat,color_strip)
    
def stick(surface,h,w,x,y,color_stick):
    '''
    Function draws a stick - high and thin rectangle
    surface - an object pygame.surface
    h - height of stick
    w - width of stick
    x,y - coordinates of left bottom corner of stick
    k - scale
    color_stick - color of stick
    '''
    rect(surface, color_stick, (x, y - h, w, h))

def umbrella_hat(surface, x, y, k,h,w,color_hat,color_strip):
    '''
    Function draws an umbrella's hat - triangle with strips on it
    surface - an object pygame.surface
    x,y - coordinates of left bottom corner of stick
    k - scale
    h - height of stick
    w - width of stick
    color_hat - color of umbrella's hat
    color_strip - color of hat's strip
    '''
    wt = 70 * k #Width of hat
    polygon(screen, color_hat, 
            [(x - wt + w / 2, y - 5 * h / 6), (x + w / 2, y - h * 1.05),
            (x + wt + w / 2, y - 5 * h / 6)])
    for i in range(8):
       line(surface, color_strip, (x + w / 2, y - h * 1.05),
            (x - wt + w / 2 + i * wt * 2 / 8, y - 5 * h / 6))


# Ship
def ship(surface, x, y, k, body_color, sail_color, window_color):
    '''
    Function draws a ship
    x,y - coordinates of left corner of ship
    k - scale
    body_color - color of ship
    sail_color - color of triangle sail
    window_color - color of window
    '''
    r = 25 * k #Radius of back
    width_of_body = 100 * k
    length_of_stern = 60 * k 
    
    ship_body(surface, x,y,k,r,width_of_body,length_of_stern,body_color)
    
    sail(surface, x,y,k,r,width_of_body,sail_color)

    window(surface,x,y,r,width_of_body,window_color)

def ship_body(surface,x,y,k,r,w,a,body_color):
    '''
    Function draws ship back
    surface - an object pygame.surface
    x,y - coordinates of left corner of ship
    k - scale
    r - radius of back
    w - width of body
    a - length of stern
    body_color - color of ship body
    '''
    #back of ship
    circle(surface, body_color, (x + r, y - r), r,draw_bottom_left=True) 
    #center of ship 
    rect(surface, body_color, (x + r, y - r, w, r)) 
    line(surface, black, (x + r, y - r), (x + r, y))
    #stern
    polygon(surface, body_color, [(x + r + w, y - r), (x + r + w + a, y - r),
            (x + r + w, y), (x + r + w, y - r)])
    line(surface, black, (x + r + w, y - r),
        (x + r + w, y))

def sail(surface, x,y,k,r,width_of_body,sail_color):
    '''
    Function draws sail - two triangles and a stick
    surface - an object pygame.surface
    x,y - coordinates of left corner of ship
    k - scale
    r - radius of back
    w - width of body
    sail_color - color of sail
    '''
    #stick
    h = 90 * k #Heith of stick
    ws = 8 * k #Width of stick
    stick(surface, h, ws, x + r + width_of_body * 0.5, y - r, black)
    #sail
    b = 60 * k #Width of sail

    # x coordinate of left upper corner of sail
    xp = x + r + width_of_body * 0.5 + ws
    
    polygon(surface, sail_color,
            [(xp, y - r - h), (xp + b, y - r - h / 2), (xp, y - r),
            (xp + b * 0.3, y - r - h / 2), (xp, y - r - h)])
    line(surface, black, (xp + 0.3 *  b, y - r - h / 2),
        (xp + b, y - r - h / 2))

def window(surface, x, y ,r, width_of_body,window_color):
    circle(surface, black, (x + r + width_of_body + 0.5 * r, y - r * 0.55),
           r * 0.35)
    circle(surface, window_color, (x + r + width_of_body + 0.5 * r,
                                   y - r * 0.55), r * 0.2)
    
#Drawing
    
#Sand, water and air
rect(screen, sand_color, (0, 275, 600, 127))
rect(screen, water_color, (0, 175, 600, 100))
rect(screen, (135, 206, 250), (0, 0, 600, 175))

# Wave
for i in range(7):
    ellipse(screen,  sand_color, ((i * 2) * 600 / 14, 265, 600 / 14, 20))
    ellipse(screen, water_color, ((i * 2 + 1) * 600 / 14, 265, 600 / 14, 20))

#Drawing objects
sun(500, 75, 7, 60, sun_color)    

ship(screen, 130, 210, 0.6,(153, 51, 0),(100,100,100),(255,255,255))
ship(screen, 350, 230, 1,(153, 51, 0),(200,200,200),(255,255,255))

cloud(screen, 110, 50, 1, 1,(112, 128, 144),(176, 196, 222))
cloud(screen, 230, 80, 1.1, 1.4, black,(173, 216, 230))
cloud(screen, 50, 130, 1.3, 1.5, black,(255, 255, 255))

umbrella(screen, 70, 340, 1,(255,0,0),(153,51,0), black)
umbrella(screen, 200, 350, 0.8,(255, 99, 71),(139, 69, 19),(0,0,128))

#Updating display
pygame.display.update()
clock = pygame.time.Clock()
finished = False

while not finished:
    clock.tick(60)
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            finished = True
