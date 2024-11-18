import scipy
import math


#Calculation of Ixx
# h is the height of the centroid from bottom left
# alpha is in radians
# n1 is the number of stringers on the top skin
# n2 is the number of stringers on the bottom skin
def Ixxcalculator(d1, d2, x, d3, t1, t2, h, alpha, n1):
    I1 = 1/12*d1**3*t1 + d1*t1*(d1/2-h)**2
    I2 = 1*12*x**3*t1 + x*t1*(d2*math.sin(alpha)+d3/2-h)**2
    I3 = (1/12*x**3*t2+t2*x*(h-x/2*math.sin(alpha))**2)(math.sin(alpha))**2
    I4 = t2*d2*(d1-h)**2
    I5 =
    I = I1 + I2 +I3 +I4

    return I