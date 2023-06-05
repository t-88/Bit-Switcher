# how to connect a gate to its self
import pygame
from backend.backend import *
from frontend.pin import *

pygame.init()
screen = pygame.display.set_mode((600,600))
clock = pygame.time.Clock()
done = False


pin1 = Pin(100,200)
pin2 = Pin(100,400)
pin3 = Pin(500,300)
pin4 = Pin(550,300)
pines = [pin1,pin2,pin3,pin4]


while(not done): 
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            done = True

    screen.fill("black")

    for pin in pines:
        pin.update()
        pin.render(screen)


    pygame.display.flip()
    clock.tick(60)

pygame.quit()