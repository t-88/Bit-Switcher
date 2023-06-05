# how to connect a gate to its self

import pygame



class Gate:
    def __init__(self,value = 0,inCount = 0):
        self.value = [value]
        self.inCount = inCount
    def __call__(self, *args, **kwds):
        if len(args) == 0:
            return self.eval()
        if len(args[0]) != self.inCount:
            print("[ERROR]: Wrong number of inputs")
            exit(1)
        
        if type(args[0]) != Gate:
            self.value = args[0]
            return self.eval()
        return args[0]()        
class gNot(Gate):
    def __init__(self,value = 0,inCount = 0):
        super().__init__(value,inCount)
    def eval(self):
        return not self.value[0]
class gAnd(Gate):
    def __init__(self,value = 0,inCount = 0):
        super().__init__(value,inCount)
    def eval(self):
        return self.value[0] & self.value[1]    
notGate = gNot(inCount=1) 
andGate = gAnd(inCount=2) 


def And(a,b):
    return andGate([a,b])
def Not(a):
    return notGate([a])
def Or(a,b):
    return Not(And(Not(a),Not(b)))
def Nand(a,b):
    return Not(And(a,b))
def Xor(a,b):
    return Or(And(Not(a),b),And(Not(b),a))






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


a = 0
b = 0




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