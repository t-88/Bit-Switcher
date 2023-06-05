import pygame

class Pin:
    def __init__(self,x,y,value = 0):
        self.value = value
        self.x = x
        self.y = y
        self.toggled = False
        self.radius = 10
    def toggel(self):
        if self.toggled: return
        self.value = int(not self.value)
    def update(self):
        if pygame.mouse.get_pressed()[0] and not self.toggled:
            mx,my = pygame.mouse.get_pos()
            if (mx - self.x)**2 + (my - self.y)**2 < self.radius**2:
                self.toggel()  
                self.toggled = True
        elif not pygame.mouse.get_pressed()[0]:
            self.toggled = False


    def render(self,screen):
        pygame.draw.circle(screen,"white" if self.value == 0 else "red",(self.x,self.y),self.radius)

