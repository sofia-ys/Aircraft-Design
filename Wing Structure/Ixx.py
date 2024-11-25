import scipy
import math
import constants as con


d1_root = con.d_1
d2_root = con.d_2
d3_root = con.d_3
d4_root = con.d_4
t1 = con.t_1
t2 = con.t_2
n1 = con.n_1
n2 = con.n_2
n3 = con.n_3
taper = con.taper
As = con.As
b= con.b
def Wingbox_lengths (d1_root,d2_root, d3_root, d4_root, b, y)
    d1 = d1_root + (d1_root*taper - d1_root)/(b/2) * y
    d2 = d2_root + (d2_root*taper - d2_root)/(b/2) * y
    d3 = d3_root + (d3_root*taper - d3_root)/(b/2) * y
    d4 = d4_root + (d4_root*taper - d4_root)/(b/2) * y
    return d1, d2, d3, d4

    alpha = math.atan((d1-d3)/d2)

def BottomskinCentroidZcontribution(AS, s, alpha, n2):
    CB_z = sum(AS * i * s * math.sin(alpha) for i in range(0, n2))
    return CB_z
def BottomskinCentroidXcontribution(AS, s, alpha, n2):
    CB_x = sum(AS * i * s * math.cos(alpha) for i in range(0, n2))
    return CB_x
def TopskinCentroidXcontribution(AS, s, alpha, n1):
    CT_x = sum(AS * i * s  for i in range(0, n1))
    return CT_x
u=d4*math.tan(alpha)
if d4 > 0:
    total_area= ((t1*d1+d2*t2+t1*d3)+(d2*t2/math.cos(alpha))) + (As * (n1+n2))
    h= ((d1*d2*t2) + (t1*(d1**2)/2) + (t1*d3*d1) - ((d3**2)*t1/2) + ((d2**2)*t2*math.tan(alpha)/(2*math.cos(alpha)))+CB_Z+d1*N1*AS)/ total_area #Z centroid positon single box
    x= ((d2**2)*t2/2)+d3*d2*t1+ ((d2**2)*t2/(2*math.cos(alpha))+CB_x+CT_x) #X centroid position single box
else:
    total_area= ((t1*d1+d2*t2+t1*d3)+(d2*t2/math.cos(alpha))) + (As * (n1+n2))+ (t1*(d1-u))
    h= ((d1*d2*t2) + (t1*(d1**2)/2) + (t1*d3*d1) - ((d3**2)*t1/2) + ((d2**2)*t2*math.tan(alpha)/(2*math.cos(alpha)))+CB_Z+d1*N1*AS+(u+((d1-u)/2)*(t1*(d1-u))))/ total_area #Z centroid positon multi box
    x= ((d2**2)*t2/2)+d3*d2*t1+ ((d2**2)*t2/(2*math.cos(alpha))+CB_x+CT_x)+((t1*(d1-u))*d4) #X centroid positon multi box


#Calculation of Ixx
# h is the height of the centroid from bottom left
# alpha is in radians
# n1 is the number of stringers on the top skin
# n2 is the number of stringers on the bottom skin
# spac is stringer spacing
def Ixxcalculator(d1, d2, L, d3, t1, t2, h, alpha, n1, n2, As, spac):

    I1 = 1/12*d1**3*t1 + d1*t1*(d1/2-h)**2
    I2 = 1*12*L**3*t1 + L*t1*(d2*math.sin(alpha)+d3/2-h)**2
    I3 = (1/12*L**3*t2+t2*L*(h-L/2*math.sin(alpha))**2)(math.sin(alpha))**2
    I4 = t2*d2*(d1-h)**2
    I5 = As*n1*(d1-h)**2
    I6 = 0
    for i in range(n2):
        Ii = As*(h-i*math.sin(alpha)*spac)**2
        I6 += Ii

    I = I1 + I2 + I3 + I4 + I5 + I6

    return I

