#This file calculates the twist
import numpy as np
import constants as con
import matplotlib.pyplot as plt
import scipy as sp
from Ixx import Wingbox_lengths as lengths

def Wing_design (y):
    return lengths(con.d_1, con.d_2, con.d_3, con.d_4, con.b, y)

G = 25e9

t_1 = sp.interpolate.interp1d(con.span_t1_1, con.t1_1, kind="previous",fill_value="extrapolate")
t_2 = sp.interpolate.interp1d(con.span_t2_1, con.t2_1, kind="previous",fill_value="extrapolate")

def area_trap (d1, d3, d2): #area of the wingbox

    return (d1 + d3)/2 * d2


def tors_const2(y): #multi-cell torsional constant calculation
    #Set unit torsion
    T = 1
    
    d1, d2, d3, d4 = Wing_design(y)
    t1 = t_1(y)
    t2 = t_2(y)
   
    alpha = np.arctan((d3-d1) / d2)
    #Set lengths of stringers 1-3 going from front to back and top to bottom
    vert1 = d1
    vert2 = vert1 - np.sin(alpha) * d4
    vert3 = d3
    
    hoz1 = d2
    diag = d2 / np.cos(alpha)
    
    # Calculate the areas of each cell
    A1 = area_trap(vert1, vert2, d4 )
    A2 = area_trap(vert2, vert3, (d2 - d4))
    
    #q1 q2 dtheta/dy
    lin1 = [
        1 / (2* A1) * (vert2 / (G * t2) + d4/(G * t2) + d1/(t1 * G) + (diag * d2/d4)/(G* t2)),
        -1 / (2*A1) * (vert2/ (G* t2)),
        -1
    ]
    lin2 = [
        -1 / (2*A2) * (vert2 / (G* t2)),
        1 / (2* A2) * ((d2-d4)/(G* t2) + d3/(G* t1) + diag * (1-d2/d4)/(G* t2) + vert2/(G*t2)),
        -1
    ]
    lin3 = [
        2*A1,
        2*A2,
        0
    ]

    matrix = np.array([lin1, lin2, lin3])
    righthand_side = np.array([0, 0, 1])

    solution = np.linalg.solve(matrix, righthand_side)
    J = 1 / (solution[2] * G)
    return J

print(tors_const2(5))