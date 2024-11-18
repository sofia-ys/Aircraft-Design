import math as m


def l(x):
    return (2*x)

def d(x):
    return x

def n(x,alpha):
    return(d(x)*m.sin(alpha)+l(x)*m.cos(alpha))

print(n(1,m.pi/2))