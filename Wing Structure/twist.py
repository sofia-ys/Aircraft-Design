#This file calculates the twist
import numpy as np
import constants as con
import torque
import matplotlib.pyplot as plt
import scipy as sp

d1 = con.d_1
d2 = con.d_2
d3 = con.d_3
d4 = con.d_4
alpha = np.arctan((d3-d1) / d2)
t1 = con.t_1
t2 = con.t_2
t3 = con.t_1
G = 25e9

def area_trap (d1, d3, d2): #area of the wingbox

    return (d1 + d3)/2 * d2

def tors_const (d1, d2, d3, alpha, t1, t2): #Single-cell torsional constant calculation: J = (4A^2)/integral(ds/t) 
    A = area_trap(d1,d3,d2) 
    L = d2 / np.cos(alpha) #length of the diagonal
    denominator = d1 / t1 + d3 / t1 + d2 / t2 + L / t2 #integral of ds/t

    torsional_const = 4 * A ** 2 / (denominator)
    return torsional_const

def tors_const2(d1, d2, d3, d4, alpha, t1, t2, t3, G): #multi-cell torsional constant calculation
    #Set unit torsion
    T = 1

    #Set lengths of stringers 1-3 going from front to back and top to bottom
    vert1 = d1
    vert2 = vert1 - np.sin(alpha) * d4
    vert3 = d3

    hoz1 = d2
    diag = d2 / np.cos(alpha)
    
    # Calculate the areas of each cell
    A1 = area_trap(vert1, vert2, d4 )
    A2 = area_trap(vert2, vert3, (d2 - d4))
    
    #find matrix rows of unkowns q1, q2, and twist: [q1, q2, twist]
    lin1 = [
            1/(2*A1) * 1/G * (vert1/t1 + hoz1/t2 * d4/d3 + diag/t2 * d4/d3),
            -1* vert2/(2*A1*G * t3),
            -1 
        ]
    lin2 = [
            -1 * vert2 / (2 * A2 * G * t3), 
            1 / (2 * A1) * 1/G * (vert3/t1 + hoz1 / t2 * (1 - d4/d3) + diag/t2 * (1 - d4/d3)), 
            -1
        ]
    lin3 = [
            2 * A1, 
            2 * A2, 
            0
        ]
    
    #right side of the matrix to be solve
    righthandside = [0, 0, 1]

    #set up matrix to be solved
    matrix = np.array([lin1, 
                       lin2, 
                       lin3])

    #solve for q1, q2, and the twist
    solution = np.linalg.solve(matrix, righthandside)
    twist = solution[2]

    #find the torsional constant (J) from the previously found twist ({dtheta/dy} = T/{GJ})
    J = twist * G

    return J

J = tors_const(d1,d2,d3,alpha,t1,t2)
print(J)

torques = sp.interpolate.interp1d(torque.x_values, torque.torque_values, kind="previous",fill_value="extrapolate")

def dtheta (y):
    x = torques(y) * 1000 / (J * G)
    return x

twist_distribution = np.array([0])
error = 0

for i in range(len(torque.x_values) - 1):
    integrated_part, e = sp.integrate.quad(dtheta, torque.x_values[i], torque.x_values[i+1])
    twist_distribution = np.append(twist_distribution, [integrated_part + twist_distribution[-1]])

twist_distribution = twist_distribution * 180 / np.pi

plt.plot(torque.x_values ,twist_distribution)
plt.xlabel('Spanwise Position [m]')
plt.ylabel('Twist [deg]')
plt.title('Twist Distribution along the Wing Span')
plt.grid(True)
plt.show()