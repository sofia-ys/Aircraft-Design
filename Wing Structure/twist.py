#This file calculates the twist
import numpy as np
import constants as con
import torque
import matplotlib.pyplot as plt
import scipy as sp
from Ixx import Wingbox_lengths as lengths

def Wing_design (y):
    return lengths(con.d_1, con.d_2, con.d_3, con.d_4, con.b, y)

#temporary wingbox design with scaled wingbox along wingspan
# d1 = np.array([0.65,0.6,0.55,0.45,0.4,0.35,0.3,0.2,0.15,0.1])
# d2 = d1 / 0.65 * con.d_2 
# d3 = d1 / 0.65 * con.d_3
# d4 = d1 / 0.65 * con.d_4
#alpha = np.arctan((d3-d1) / d2)
# t1 = con.t_1
# t2 = con.t_2
# t3 = con.t_1
G = 25e9
# x = [0,2,4,6,8,10,12,14,16,18]

t_1 = sp.interpolate.interp1d(con.span_t1_1, con.t1_1, kind="previous",fill_value="extrapolate")
t_2 = sp.interpolate.interp1d(con.span_t2_1, con.t2_1, kind="previous",fill_value="extrapolate")

def area_trap (d1, d3, d2): #area of the wingbox

    return (d1 + d3)/2 * d2

def tors_const (y): #Single-cell torsional constant calculation: J = (4A^2)/integral(ds/t) 

    d1, d2, d3, d4 = Wing_design(y)
    alpha = np.arctan((d3-d1)/d2)
    t1 = t_1(y)
    t2 = t_2(y)

    A = area_trap(d1,d3,d2) 
    L = d2 / np.cos(alpha) #length of the diagonal
    denominator = d1 / t1 + d3 / t1 + d2 / t2 + L / t2 #integral of ds/t

    torsional_const = 4 * A ** 2 / (denominator)
    return torsional_const

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
    J = -1 / (solution[2] * G)
    return J

def J(y):
    if y <= con.q1:
         J = tors_const2(y)
    else:
         J = tors_const(y)

    return J

def dtheta (y):
        x = torques(y) * 1000 / (J(y) * G)
        return x

#J = sp.interpolate.interp1d(x, tors_const2(d1,d2,d3,alpha,t1,t2), kind="previous",fill_value="extrapolate") 

x_values = np.linspace(0,17.74,10000)
torsional_stiffness = []
for i in x_values:
    torsional_stiffness.append(J(i))
plt.plot(x_values, torsional_stiffness)

plt.xlabel('Spanwise Position [m]')
plt.ylabel('Torsional Stiffness')
plt.title('Torsional Stiffness along the Wing Span')
plt.grid(True)
plt.show()

for aoa in range(len(torque.aoa_range)):
    torques = sp.interpolate.interp1d(torque.x_values, torque.torques[aoa], kind="previous",fill_value="extrapolate")

    twist_distribution = np.array([0])
    error = 0

    for i in range(len(torque.x_values) - 1):
        integrated_part, e = sp.integrate.quad(dtheta, torque.x_values[i], torque.x_values[i+1])
        twist_distribution = np.append(twist_distribution, [integrated_part + twist_distribution[-1]])

    twist_distribution = twist_distribution * 180 / np.pi

    plt.plot(torque.x_values ,twist_distribution, label=f'AoA = {torque.aoa_range[aoa]}°')





plt.xlabel('Spanwise Position [m]')
plt.ylabel('Twist [deg]')
plt.title('Twist Distribution along the Wing Span for different Angles of Attack')
plt.legend()
plt.grid(True)
plt.show()