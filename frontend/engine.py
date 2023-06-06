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

        self.pins = {}


        self.gates = {}
        self.add_gate(2,1,200,200,"And")
        self.add_gate(1,1,200,300,"Not")
        self.add_gate(2,1,200,400,"Or")



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
        self.pins[pin.uuid] = pin
        return pin.uuid
    def add_wire_connection(self):
        out = self.wireConnectionPin1.uuid
        inp = self.wireConnectionPin2.uuid
        if self.pins[out].kind == IN_PIN:
            inp , out = out , inp
        self.wireConnections[out].add(inp)
        return True
    def connect_wire_callback(self,uuid):
        pin = self.pins[uuid]
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
            parentPin = self.pins[pinID]
            isActive = parentPin.value == 1

            for kidPinID in self.wireConnections[pinID]:
                kidPin = self.pins[kidPinID]
                kidPin.value = isActive
                pygame.draw.line(
                                  screen,
                                 "white" if not isActive else "red",
                                 (parentPin.x,parentPin.y),
                                 (kidPin.x,kidPin.y),
                                  1 if not isActive else 3
                                )

    def add_gate(self,inCount,outCount,x,y,type="Not"):
        
        inPins  = [self.add_pin(x - 10 , y + 10 * inCount + i  * 40,kind=IN_PIN)  for i in range(inCount)]
        outPins = [self.add_pin(x + 90,  y + 35 * outCount + i * 40,kind=OUT_PIN) for i in range(outCount)]

        gate = Gate(inPins,outPins,x,y,funcs[type])
        self.gates[gate.uuid] = gate

        return gate.uuid

    def run(self,screen):
        self.render_wire_coonection(screen)
        self.mx,self.my = pygame.mouse.get_pos()
        for pin in self.pins.values():
            pin.update()
            pin.render(screen)

        for gate in self.gates.values():
            gate.update(self.pins)
            gate.render(screen)

