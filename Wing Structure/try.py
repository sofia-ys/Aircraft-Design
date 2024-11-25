import numpy as np
import scipy as sp
import math
import constants as con


d1_root = con.d_1
d2_root = con.d_2
d3_root = con.d_3
d4_root = con.d_4
taper = con.taper
b= con.b
y_tab = []
i=0
step = 0.05
count = 0
design_choice=1
q = 20 #value along the span at which 3rd spar stops being there
if(design_choice==1):
    #Design 1
    span_n1 = [0,21,25,30,36,44,51,59,68]
    n1 = [18,21,25,30,36,44,51,59,68] # n1 is the number of stringers on the top skin
    span_n2 = [0,21,25,30,36,44,51,59,68]
    n2 = [27,33,38,45,55,65,80,100,120] # n2 is the number of stringers on the bottom skin
    span_t1 = [0,21,25,30,36,44,51,59,68]
    t1 = [18,21,25,30,36,44,51,59,68]
    span_t2 = [0,21,25,30,36,44,51,59,68]
    t2 = [18,21,25,30,36,44,51,59,68]
    span_As = [0,21,25]
    As = [1,1,1] # cross sectional area of a stringer
elif(design_choice==2):
    #Design 2
    span_n1 = [18, 21, 25, 30, 36, 44, 51, 59, 68]
    n1 = [18, 21, 25, 30, 36, 44, 51, 59, 68] # n1 is the number of stringers on the top skin
    span_n2 = [18, 21, 25, 30, 36, 44, 51, 59, 68]
    n2 = [27, 33, 38, 45, 55, 65, 80, 100, 120] # n2 is the number of stringers on the bottom skin
    span_t1 = [18, 21, 25, 30, 36, 44, 51, 59, 68]
    t1 = [18, 21, 25, 30, 36, 44, 51, 59, 68]
    span_t2 = [18, 21, 25, 30, 36, 44, 51, 59, 68]
    t2 = [18, 21, 25, 30, 36, 44, 51, 59, 68]
    span_As = [18, 21, 25]
    As = [1, 1, 1] # cross sectional area of a stringer
else:
    #Design 3
    span_n1 = [0, 21, 25, 30, 36, 44, 51, 59, 68]
    n1 = [18, 21, 25, 30, 36, 44, 51, 59, 68] # n1 is the number of stringers on the top skin
    span_n2 = [0, 21, 25, 30, 36, 44, 51, 59, 68]
    n2 = [27, 33, 38, 45, 55, 65, 80, 100, 120] # n2 is the number of stringers on the bottom skin
    span_t1 = [0, 21, 25, 30, 36, 44, 51, 59, 68]
    t1 = [18, 21, 25, 30, 36, 44, 51, 59, 68]
    span_t2 = [0, 21, 25, 30, 36, 44, 51, 59, 68]
    t2 = [18, 21, 25, 30, 36, 44, 51, 59, 68]
    span_As = [0, 21, 25]
As = [1, 1, 1] # cross sectional area of a stringer
n1_inter = sp.interpolate.interp1d(span_n1, n1, kind="previous", fill_value="extrapolate")
n2_inter = sp.interpolate.interp1d(span_n2, n2, kind="previous", fill_value="extrapolate")
t1_inter = sp.interpolate.interp1d(span_t1, t1, kind="previous", fill_value="extrapolate")
t2_inter = sp.interpolate.interp1d(span_t2, t2, kind="previous", fill_value="extrapolate")
As_inter = sp.interpolate.interp1d(span_As, As, kind="previous", fill_value="extrapolate")
while i<=b/2 :
    i = i + step
    y_tab.append(i)
    count = count +1

def Wingbox_lengths (d1_root,d2_root, d3_root, d4_root, b, y) :
    d1_a = d1_root + (d1_root*taper - d1_root)/(b/2) * y
    d2_a = d2_root + (d2_root*taper - d2_root)/(b/2) * y
    d3_a = d3_root + (d3_root*taper - d3_root)/(b/2) * y
    d4_a = d4_root + (d4_root*taper - d4_root)/(b/2) * y
    return d1_a, d2_a, d3_a, d4_a
def CentroidZcontribution(AS, sb, st, alpha, n2, n1, d1, d2, d3, d4):
    CB_z = sum(AS * i * sb * math.sin(alpha) for i in range(0, int(n2))) #for bottom

    CB_x = sum(AS * i * sb * math.cos(alpha) for i in range(0, int(n2))) #top

    CT_x = sum(AS * i * st for i in range(0, int(n1))) #top
    u=d4*math.tan(alpha)
    if d4 > 0:
        total_area= ((t1*d1+d2*t2+t1*d3)+(d2*t2/math.cos(alpha))) + (As * (n1+n2))
        h= ((d1*d2*t2) + (t1*(d1**2)/2) + (t1*d3*d1) - ((d3**2)*t1/2) + ((d2**2)*t2*math.tan(alpha)/(2*math.cos(alpha)))+CB_z+d1*n1*AS)/ total_area #Z centroid positon single box
        x= ((d2**2)*t2/2)+d3*d2*t1+ ((d2**2)*t2/(2*math.cos(alpha))+CB_x+CT_x) #X centroid position single box
    else:
        total_area= ((t1*d1+d2*t2+t1*d3)+(d2*t2/math.cos(alpha))) + (As * (n1+n2))+ (t1*(d1-u))
        h= ((d1*d2*t2) + (t1*(d1**2)/2) + (t1*d3*d1) - ((d3**2)*t1/2) + ((d2**2)*t2*math.tan(alpha)/(2*math.cos(alpha)))+CB_z+d1*n1*AS+(u+((d1-u)/2)*(t1*(d1-u))))/ total_area #Z centroid positon multi box
        x= ((d2**2)*t2/2)+d3*d2*t1+ ((d2**2)*t2/(2*math.cos(alpha))+CB_x+CT_x)+((t1*(d1-u))*d4) #X centroid positon multi box
    return h, x

def Ixxcalculator(d1, d2, L, d3, t1, t2, h, alpha, n1, n2, As, sb):
    I1 = 1/12*d1**3*t1 + d1*t1*(d1/2-h)**2
    I2 = 1*12*L**3*t1 + L*t1*(d2*math.sin(alpha)+d3/2-h)**2
    I3 = (1/12 * L ** 3 * t2 + t2 * L * (h - L / 2 * math.sin(alpha)) ** 2) * (math.sin(alpha)) ** 2
    I4 = t2*d2*(d1-h)**2
    I5 = As*n1*(d1-h)**2
    I6 = 0

    for i in range(0,int(n2)):
        Ii = As*(h-i*math.sin(alpha)*sb)**2
        I6 += Ii
    I = I1 + I2 + I3 + I4 + I5 + I6

    return I
def Ixx2calculator(d1, d2, L, d3, t1, t2, h, alpha, n1, n2, As, sb):
    u = d4 * math.tan(alpha)
    I1 = 1/12*d1**3*t1 + d1*t1*(d1/2-h)**2
    I2 = 1*12*L**3*t1 + L*t1*(d2*math.sin(alpha)+d3/2-h)**2
    I3 = (1/12 * L ** 3 * t2 + t2 * L * (h - L / 2 * math.sin(alpha)) ** 2) * (math.sin(alpha)) ** 2
    I4 = t2*d2*(d1-h)**2
    I5 = As*n1*(d1-h)**2
    I6 = 0
    I7 = 1 / 12 * (d1 - u) ** 3 * t1 + t1 * (d1 - u) * (d1 / 2 - h + u / 2) ** 2
    for i in range(0,int(n2)):
        Ii = As*(h-i*math.sin(alpha)*sb)**2
        I6 += Ii
    I = I1 + I2 + I3 + I4 + I5 + I6 + I7

    return I

for y in y_tab:
    n1 = n1_inter(y)
    n2 = n2_inter(y)
    t1 = t1_inter(y)
    t2 = t2_inter(y)
    As = As_inter(y)
    d1, d2, d3, d4, = Wingbox_lengths(d1_root,d2_root, d3_root, d4_root, b, y)
    alpha = math.atan((d1-d3)/d2)
    L = (d1-d3)/math.cos(alpha)
    sb = L/(n2-1)
    st = d2/(n1-1)
    h, x = CentroidZcontribution(As, sb, st, alpha, n2, n1, d1, d2, d3, d4)
    if (y <= q):
        Ixx = Ixx2calculator(d1, d2, L, d3, t1, t2, h, alpha, n1, n2, As, sb)
    else:
        Ixx = Ixx2calculator(d1, d2, L, d3, t1, t2, h, alpha, n1, n2, As, sb)

#Calculation of Ixx
# h is the height of the centroid from bottom left
# alpha is in radians
# n1 is the number of stringers on the top skin
# n2 is the number of stringers on the bottom skin
# spac is stringer spacing