import math as m
import scipy as sp
from scipy import integrate

def l(x):
    return (2*x)

def d(x):
    return x

def n(x,alpha):
    return(d(x)*m.sin(alpha)+l(x)*m.cos(alpha))

def w(x,alpha,l):
    return (-1*sp.integrate.quad(n(x,alpha),x,l))

