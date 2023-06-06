# how to connect a gate to its self
import pygame
from frontend.engine import *

pygame.init()
screen = pygame.display.set_mode((600,600))
clock = pygame.time.Clock()
done = False



engine = Engine()




while(not done): 
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            done = True

    screen.fill("black")


    engine.run(screen)



    pygame.display.flip()
    clock.tick(60)

pygame.quit()