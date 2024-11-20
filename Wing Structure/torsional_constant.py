#This file calculates the torsional constant of a single-cell wingbox
import numpy

def area_trap (d1, d2, d3): #area of the wingbox
    return (d1 + d3)/2 * d2

def tors_const (d1, d2, d3, alpha, t1, t2): #J = (4A^2)/integral(ds/t)
    A = area_trap(d1,d2,d3) 
    L = d2 / numpy.cos(alpha) #length of the diagonal
    denominator = d1 / t1 + d3 / t1 + d2 / t2 + L / t2 #integral of ds/t

    torsional_const = 4 * A ** 2 / (denominator)
    return torsional_const

