from frontend.gate import *

def And(a,b):
    return a & b
def Not(a):
    return not a
def Or(a,b):
    return a | b
def Nand(a,b):
    return not (a & b)
def Xor(a,b):
    return a ^ b

funcs = {
    "And": And,
    "Not": Not,
    "Or": Or,
    "Nand": Nand,
    "Xor": Xor,
}