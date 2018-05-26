from time import sleep
import sys, pygame, random
from pygame import *
 
 
pygame.init()
window = pygame.display.set_mode((800,800))
draw.rect(window, (0,0,0), (0,0,800,800))
draw.rect(window, (255,255,255), (10, 10, 780, 780))
display.update()
 
running = True
drawing = False
drawingCross = False
width = 0
crosswidthupdown = 0
crosswidthleftright = 0
posX = 250
posY = 260
dirX = 2
dirY = 2
targetX = random.randint(20, 780)
targetY = random.randint(20, 780)
timer = 6000
numClicks = 0
win = False
freeze = False
freezeCharges = 3
 
myfont = pygame.font.SysFont("monospace", 15)
 
while running:
   
    for EVENT in pygame.event.get():
        if EVENT.type == MOUSEBUTTONDOWN:
            if EVENT.button == 1:
                pos = pygame.mouse.get_pos()
                x = pos[0]
                y = pos[1]
                drawing = True
               
                red = random.randint (0, 254)
                green = random.randint (0, 255)
                blue = random.randint (0, 255)
               
                red2 = random.randint (0, 255)
                green2 = random.randint (0, 255)
                blue2 = random.randint (0, 255)
               
                numClicks = numClicks + 1
 
            elif EVENT.button == 3 and freezeCharges >0:
                freeze = True
                freezeTime = 300
                freezeCharges = freezeCharges - 1
 
 
               
 
        elif EVENT.type == MOUSEBUTTONUP:
            drawing = False
            width = 0
        elif EVENT.type == QUIT:
            running = False
    if drawing:
        width = width + 1
        draw.rect(window, (red2,green2,blue2), (x-width,y-width,width*2,width*2))
        draw.circle(window, (red,green,blue), (x, y) ,width)
        if window.get_at((targetX, targetY)) != (0,255,0):
            print "you lose"
            running = False
       
 
 
       
       
    if freeze == False:
        posX = posX + dirX
        posY = posY + dirY
    if window.get_at((posX, posY)) == (0, 255,0):
        win = True
        running = False
       
    if window.get_at((posX,posY+dirY)) != (255,255,255) and window.get_at((posX,posY+dirY)) != (255,0,0) and window.get_at((posX,posY+dirY)) != (0,255,0):
        dirY = -dirY
 
    if window.get_at((posX+dirX, posY)) != (255,255,255) and window.get_at((posX+dirX,posY)) != (255,0,0) and window.get_at((posX+dirX,posY)) != (0,255,0):
        dirX = -dirX
 
    draw.circle(window, (255,0,0), (posX,posY), 1)
    draw.circle(window, (0,255,0), (targetX, targetY), 5)
 
    draw.rect(window, (255,255,255), (300, 10, 35, 15))
    draw.rect(window, (0,0,0), (300, 10, 35, 15), 2)
    label = myfont.render(str(timer), 1, (0,0,0))
    window.blit(label, (300, 10))
 
 
   
    sleep(0.01)
    display.update()
   
    if freeze == False:
        timer = timer - 1
 
    if freeze == True:
        freezeTime = freezeTime - 1
        if freezeTime == 0:
            freeze = False
    if timer == 0:
        print "Game over!"
        running = False
quit()
if win == True:
    print "Timer left: " + str(timer)
    if numClicks == 0:
        numClicks = 1
    print "times clicked: " + str (numClicks)
    finalscore = timer/numClicks*(freezeCharges + 1)
    print "Final score: " + str (finalscore)
