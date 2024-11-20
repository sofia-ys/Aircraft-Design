import scipy
import math
import constants as con


d1_root = con.d_1
d2_root = con.d_2
d3_root = con.d_3
t1 = con.t_1
t2 = con.t_2
n1 = con.n_1
n2 = con.n_2
n3 = con.n_3
taper = con.taper
As = con.As

def Wingbox_lengths (d1_root,d2_root, d3_root, y)
    d1 = d1_root + (d1_root*taper - d1_root)/(b/2) * y
    d2 = d2_root + (d2_root*taper - d2_root)/(b/2) * y
    d3 = d3_root + (d3_root*taper - d3_root)/(b/2) * y
    return d1, d2, d3

alpha = math.atan((d1-d3)/d2)


h= ((d1*d2*t2) + (t1*(d1**2)/2) + (t1*d3*d1) - ((d3**2)*t1/2) + ((d2**2)*t2*math.tan(alpha)/(2*math.cos(alpha))))/ ((t1*d1+d2*t2+t1*d3)+(d2*t2/math.cos(alpha)))

#Calculation of Ixx
# h is the height of the centroid from bottom left
# alpha is in radians
# n1 is the number of stringers on the top skin
# n2 is the number of stringers on the bottom skin
def Ixxcalculator(d1, d2, L, d3, t1, t2, h, alpha, n1, n2, As):
    I1 = 1/12*d1**3*t1 + d1*t1*(d1/2-h)**2
    I2 = 1*12*L**3*t1 + L*t1*(d2*math.sin(alpha)+d3/2-h)**2
    I3 = (1/12*L**3*t2+t2*L*(h-L/2*math.sin(alpha))**2)(math.sin(alpha))**2
    I4 = t2*d2*(d1-h)**2
    I5 = As*n1*(d1-h)**2
    I6 = 0
    for i in range(n2):
        Ii = As*(h-i*math.sin(alpha)/n2)**2
        I6 += Ii

    I = I1 + I2 + I3 + I4 + I5 + I6

    return I

