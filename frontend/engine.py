import pygame
from backend.backend import *
from frontend.pin import *
from frontend.gate import *
import uuid
from collections import defaultdict



WIRE_CONECTION_EMPTY = 0
WIRE_CONECTION_PENDING = 1
class Engine:
    def __init__(self):

        self.pines = {}


        self.gates = {}
        self.add_gate(100,200,"and")



        self.add_pin(100,100)
        self.add_pin(100,400)
        self.add_pin(500,300,kind=IN_PIN)
        self.add_pin(550,300,kind=IN_PIN)


        self.wireConnectionState = WIRE_CONECTION_EMPTY 
        self.wireConnectionPin1 = None
        self.wireConnectionPin2 = None
        self.wireConnections = defaultdict(set)

        self.mx,self.my = 0 ,0 
    def add_pin(self,x,y,kind=1,value=0):
        pin = Pin(x,y,kind=kind,value=value)
        pin.connect_wire_callback = self.connect_wire_callback
        self.pines[pin.uuid] = pin
    def add_wire_connection(self):
        out = self.wireConnectionPin1.uuid
        inp = self.wireConnectionPin2.uuid
        if self.pines[out].kind == IN_PIN:
            inp , out = out , inp
        self.wireConnections[out].add(inp)
        return True
    def connect_wire_callback(self,uuid):
        pin = self.pines[uuid]
        if self.wireConnectionState == WIRE_CONECTION_EMPTY:
            self.wireConnectionState = WIRE_CONECTION_PENDING
            self.wireConnectionPin1 = pin
        else:
            if (pin.kind != self.wireConnectionPin1.kind):
                self.wireConnectionPin2 = pin
                self.add_wire_connection()
                self.wireConnectionState = WIRE_CONECTION_EMPTY
            else:
                self.wireConnectionState = WIRE_CONECTION_EMPTY
    def render_wire_coonection(self,screen):
        if self.wireConnectionState == WIRE_CONECTION_PENDING and self.wireConnectionPin1:
            pygame.draw.line(screen, "white", (self.wireConnectionPin1.x,self.wireConnectionPin1.y), (self.mx,self.my))


        for pinID in self.wireConnections:
            parentPin = self.pines[pinID]
            isActive = parentPin.value == 1

            for kidPinID in self.wireConnections[pinID]:
                kidPin = self.pines[kidPinID]
                pygame.draw.line(
                                  screen,
                                 "white" if not isActive else "red",
                                 (parentPin.x,parentPin.y),
                                 (kidPin.x,kidPin.y),
                                  1 if not isActive else 3
                                )


    def run(self,screen):
        self.render_wire_coonection(screen)

        self.mx,self.my = pygame.mouse.get_pos()
        for pin in self.pines.values():
            pin.update()
            pin.render(screen)
