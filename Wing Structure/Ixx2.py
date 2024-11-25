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
b = con.b
alpha = con.alpha
def Wingbox_lengths (d1_root,d2_root, d3_root, y) :
    d1 = d1_root + (d1_root*taper - d1_root)/(b/2) * y
    d2 = d2_root + (d2_root*taper - d2_root)/(b/2) * y
    d3 = d3_root + (d3_root*taper - d3_root)/(b/2) * y
    return d1, d2, d3

#Calculation of Ixx
# h is the height of the centroid from bottom left
# alpha is in radians
# n1 is the number of stringers on the top skin
# n2 is the number of stringers on the bottom skin
# design_choice is an input for different designs. This was done to be able to compare between the different designs without having to input different numbers.
# q is the distance along the half span at which the third spar is added and thus the calculation for moment of inertia has to change
#Design 1

design_choice = 1
if(design_choice==1):
    span_n1 = [18,21,25,30,36,44,51,59,68]
    n1 = [18,21,25,30,36,44,51,59,68]
    span_n2 = [18,21,25,30,36,44,51,59,68]
    n2 = [27,33,38,45,55,65,80,100,120]
    span_t1 = [18,21,25,30,36,44,51,59,68]
    t1 = [18,21,25,30,36,44,51,59,68]
    span_t2 = [18,21,25,30,36,44,51,59,68]
    t2 = [18,21,25,30,36,44,51,59,68]
    span_An = [18,21,25,30,36,44,51,59,68]
    An = [18,21,25,30,36,44,51,59,68]

def Ixxcalculator(y,design_choice):
    lst= Wingbox_lengths(d1_root,d2_root, d3_root, y)
    d1=lst[0]
    d2=lst[1]
    d3=lst[2]
    n1=n1_inter(y)
    n2=n2_inter(y)
    t1=t1_inter(y)
    t2=t2_inter(y)
    An=An_inter(y)
    total_area = ((t1 * d1 + d2 * t2 + t1 * d3) + (d2 * t2 / math.cos(alpha))) + (As * (n1 + n2))
    h = ((d1 * d2 * t2) + (t1 * (d1 ** 2) / 2) + (t1 * d3 * d1) - ((d3 ** 2) * t1 / 2) + ((d2 ** 2) * t2 * math.tan(alpha) / (2 * math.cos(alpha)))) / total_area
    L = d2/math.cos(math.radians(alpha))*d3
    I1 = 1 / 12 * d1 ** 3 * t1 + d1 * t1 * (d1 / 2 - h) ** 2
    I2 = 1 * 12 * L ** 3 * t1 + L * t1 * (d2 * math.sin(alpha) + d3 / 2 - h) ** 2
    I3 = (1 / 12 * L ** 3 * t2 + t2 * L * (h - L / 2 * math.sin(alpha)) ** 2)(math.sin(alpha)) ** 2
    I4 = t2 * d2 * (d1 - h) ** 2
    I5 = As * n1 * (d1 - h) ** 2
    I6 = 0
    for i in range(n2):
        Ii = As * (h - i * math.sin(alpha) * spac) ** 2
        I6 += Ii

    I = I1 + I2 + I3 + I4 + I5 + I6

    return I

