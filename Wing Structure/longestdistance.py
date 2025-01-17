import math as math
from Ixx import Ixxfinal
from Ixz import Ixzfinal
from Izz import Izzcalculator


def findlongestdistance(d1, d2, L, d3, d4, t1, t2, h, alpha, n1, n2, As, x, design_choice, y):
    f1 = math.sqrt(x ** 2 + h ** 2)
    f2 = math.sqrt(x ** 2 + (d1 - h) ** 2)
    f3 = math.sqrt((d2 - x) ** 2 + (d1 - h) ** 2)
    f4 = math.sqrt((d2 - x) ** 2 + (d1 - d3 - h) ** 2)
    e1 = x
    e2 = x
    e3 = d2 - x
    e4 = d2 - x
    P1 = math.acos(e1 / f1)
    P2 = math.acos(e2 / f2)
    P3 = math.acos(e3 / f3)
    P4 = math.acos(e4 / f4)
    Ixz = Ixzfinal(design_choice, y)
    Izz = Izzcalculator(d1, d2, d3, d4, alpha, t1, t2, x, As, n1, n2, L, y)
    A = math.atan(Izz / Ixz)
    B1 = P1 + A
    B2 = P2 - A
    B3 = P3 + A
    B4 = P4 - A
    g1 = f1 * math.sin(B1)  # distance from neutral axis for corner 1
    g2 = f2 * math.sin(B2)  # distance from neutral axis for corner 2
    g3 = f3 * math.sin(B3)  # distance from neutral axis for corner 3
    g4 = f3 * math.sin(B4)  # distance from neutral axis for corner 4

    if g1 >= g3:
        x_compressive = x
        z_compressive = -d1 + h
    else:
        x_compressive = -d2 + x
        z_compressive = -d1 + h

    if g2 >= g4:
        x_tensile = x
        z_tensile = h

    else:
        x_tensile = -d2 + x
        z_tensile = h

    return x_tensile, z_tensile, x_compressive, z_compressive


