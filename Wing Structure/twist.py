#This file calculates the torsional constant of a single-cell wingbox
import numpy as np

def area_trap (d1, d3, d2): #area of the wingbox

    return (d1 + d3)/2 * d2


def tors_const2(d1, d2, d3, d4, alpha, t1, t2, t3, G):
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

    return (J, twist)

    
print(tors_const2(1,1,1,0.5,1,1,1,1,1))

def tors_const (d1, d2, d3, alpha, t1, t2): #J = (4A^2)/integral(ds/t)
    A = area_trap(d1,d3,d2) 
    L = d2 / np.cos(alpha) #length of the diagonal
    denominator = d1 / t1 + d3 / t1 + d2 / t2 + L / t2 #integral of ds/t

    torsional_const = 4 * A ** 2 / (denominator)
    return torsional_const

def twist(T, G, J):
    twist = T / (G * J)
    return twist


