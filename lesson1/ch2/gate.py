def AND(x1, x2):
    w1, w2, theta = 0.5, 0.5, 0.6
    tmp = x1*w1 + x2*w2
    if tmp <= theta:
        return 0
    elif tmp > theta:
        return 1

def OR(x1, x2):
    w1, w2, theta = 0.5, 0.5, 0.4
    tmp = x1*w1 + x2*w2

    if tmp <= theta:
        return 0
    elif tmp > theta:
        return 1

f = OR

print(f(0,0))
print(f(0,1))
print(f(1,0))
print(f(1,1))
