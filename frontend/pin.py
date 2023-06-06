import pygame
import uuid

IN_PIN = 0
OUT_PIN = 1


class Pin:
    def __init__(self,x,y,value = 0,kind=OUT_PIN):
        self.value = value
        self.x = x
        self.y = y
        self.toggled = False
        self.radius = 10
        self.kind = kind

        self.uuid = uuid.uuid1()

        self.connect_wire_callback = lambda _: print("[Error] Pin connect wire callback no implemented")
    def toggel(self):
        if self.toggled: return
        self.value = int(not self.value)
    def update(self):
        mx,my = pygame.mouse.get_pos()
        if pygame.mouse.get_pressed()[0] and not self.toggled and self.kind == OUT_PIN:
            if (mx - self.x)**2 + (my - self.y)**2 < self.radius**2:
                self.toggel()  
                self.toggled = True
        elif pygame.mouse.get_pressed()[2] and not self.toggled:
            if (mx - self.x)**2 + (my - self.y)**2 < self.radius**2:
                self.connect_wire_callback(self.uuid)
                self.toggled = True
        elif not pygame.mouse.get_pressed()[0] and not pygame.mouse.get_pressed()[2]:
            self.toggled = False




    def render(self,screen):
        pygame.draw.circle(screen,"white" if self.value == 0 else "red",(self.x,self.y),self.radius)

