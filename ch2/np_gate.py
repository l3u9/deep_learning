import numpy as np


def AND(x1, x2):
    x = np.array([x1, x2])
    w = np.array([0.5, 0.5])
    b = -0.7
    
    tmp = np.sum(x*w) + b

    if tmp <= 0:
        return 0
    elif tmp > 0:
        return 1

def NAND(x1, x2):
    x = np.array([x1, x2])
    w = np.array([-0.5, -0.5])
    b = 0.7

    tmp = np.sum(x*w) + b

    if tmp <= 0:
        return 0
    elif tmp > 0:
        return 1


def OR(x1, x2):
    x = np.array([x1, x2])
    w = np.array([0.5, 0.5])
    b = -0.4
    
    tmp = np.sum(x*w) + b

    if tmp <= 0:
        return 0
    elif tmp > 0:
        return 1       


def XOR(x1, x2):
    s1 = NAND(x1, x2)
    s2 = OR(x1, x2)
    y = AND(s1, s2)
    return y


functions = {"OR" : OR, "AND": AND, "NAND" : NAND, "XOR": XOR}



f = functions[input("input gate: ")]

print(f(0,0))
print(f(0,1))
print(f(1,0))
print(f(1,1))
