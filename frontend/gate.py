import pygame
from frontend.pin import *

class Gate:
    def __init__(self,inCount,outCount,x,y,logic: lambda x : x):
        self.x , self.y = x , y
        self.inCount , self.outCount = inCount , outCount
        self.size = 80
    def update(self):
        pass

    def render(self,screen):
        pygame.draw.rect(screen, "white", pygame.Rect(self.x,self.y,self.size,self.size))


