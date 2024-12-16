import math as math
from Ixx import Ixx2calculator


def findlongestdistance(d1, d2, L, d3, t1, t2, h, alpha, n1, n2, As, sb, q):
    f1 = math.sqrt(x**2 + h**2)
    f2 = math.sqrt(x**2 + (d1-h)**2)
    f3 = math.sqrt((d2-x)**2 + (d1-h)**2)
    f4 = math.sqrt((d2-x)**2 + (d1-d3-h)**2)
    e1 = x
    e2 = x
    e3 = d2 - x
    e4 = d2 - x
    P1 = math.acos(e1/f1)
    P2 = math.acos(e2/f2)
    P3 = math.acos(e3/f3)
    P4 = math.acos(e4/f4)
    Ixx = Ixx2calculator(d1, d2, L, d3, t1, t2, h, alpha, n1, n2, As, sb)
    Izz =
    A =
    B1 = P1 -
