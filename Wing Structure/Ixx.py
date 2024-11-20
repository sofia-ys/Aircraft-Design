import scipy
import math


#Calculation of Ixx
# h is the height of the centroid from bottom left
# alpha is in radians
# n1 is the number of stringers on the top skin
# n2 is the number of stringers on the bottom skin
def Ixxcalculator(d1, d2, L, d3, t1, t2, h, alpha, n1, n2):
    I1 = 1/12*d1**3*t1 + d1*t1*(d1/2-h)**2
    I2 = 1*12*L**3*t1 + L*t1*(d2*math.sin(alpha)+d3/2-h)**2
    I3 = (1/12*L**3*t2+t2*L*(h-L/2*math.sin(alpha))**2)(math.sin(alpha))**2
    I4 = t2*d2*(d1-h)**2
    I5 = n1*(d1-h)**2
    I6 = 0
    for i in range(n2):
        Ii = (h-i*math.sin(alpha)/n2)**2
        I6 += Ii

    I = I1 + I2 + I3 + I4 + I5 + I6

    return I

