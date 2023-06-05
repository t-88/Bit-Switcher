# how to connect a gate to its self

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
a = 0
b = 0
while(True): 
    orGate = notGate([andGate([notGate([a]),notGate([b])])])
    print(orGate)