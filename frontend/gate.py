import pygame
from frontend.pin import *
import uuid

class Gate:
    def __init__(self,inPins,outPins,x,y,logic: lambda x : x):
        self.x , self.y = x , y
        self.inCount , self.outCount = len(inPins) , len(outPins)
        self.size = 80
        self.uuid = uuid.uuid1()

        self.inPins =  inPins
        self.outPins = outPins
        self.logic = logic
    def update(self,pins):
        if len(self.inPins) == 1:
            pins[self.outPins[0]].value = self.logic(pins[self.inPins[0]].value)
        else:
            pins[self.outPins[0]].value = self.logic(pins[self.inPins[0]].value,pins[self.inPins[1]].value)

    def render(self,screen):
        pygame.draw.rect(screen, "white", pygame.Rect(self.x,self.y,self.size,self.size))


