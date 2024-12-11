import scipy as sp
import math

from matplotlib import pyplot as plt

import constants as con
from Ixx import CentroidZcontribution
from Ixx import Wingbox_lengths

def Ixx2calculator(d1, d2, L, d3, t1, t2, h, alpha, n1, n2, As, sb, d4):
    u = d4 * math.tan(alpha)
    I1 = 1 / 12 * d1 ** 3 * t1 + d1 * t1 * (d1 / 2 - h) ** 2
    I2 = 1 / 12 * L ** 3 * t1 + L * t1 * (d2 * math.sin(alpha) + d3 / 2 - h) ** 2
    I3 = (1 / 12 * L ** 3 * t2 * (math.sin(alpha)) ** 2)+L*t2*(h-d1/2*math.sin(alpha))**2
    I4 = t2 * d2 * (d1 - h) ** 2
    I5 = As * n1 * (d1 - h) ** 2
    I6 = 0
    I7 = 1 / 12 * (d1 - u) ** 3 * t1 + t1 * (d1 - u) * (d1 / 2 - h + u / 2) ** 2
    for i in range(0, int(n2)):
        Ii = As * (h - i * math.sin(alpha) * sb) ** 2
        I6 += Ii
    I = I1 + I2 + I3 + I4 + I5 + I6 + I7

    return I


def Ixyfinal(design_choice, y):
    d1_root = con.d_1
    d2_root = con.d_2
    d3_root = con.d_3
    d4_root = con.d_4
    b = con.b
    if design_choice == 1:
        span_n1 = con.span_n1_1
        n1 = con.n1_1  # n1 is the number of stringers on the top skin
        span_n2 = con.span_n2_1
        n2 = con.n2_1  # n2 is the number of stringers on the bottom skin
        span_t1 = con.span_t1_1
        t1 = con.t1_1
        span_t2 = con.span_t2_1
        t2 = con.t2_1
        span_As = con.span_As_1
        As = con.As_1  # cross sectional area of a stringer
        q = con.q1
    elif design_choice == 2:
        span_n1 = con.span_n1_2
        n1 = con.n1_2  # n1 is the number of stringers on the top skin
        span_n2 = con.span_n2_2
        n2 = con.n2_2  # n2 is the number of stringers on the bottom skin
        span_t1 = con.span_t1_2
        t1 = con.t1_2
        span_t2 = con.span_t2_2
        t2 = con.t2_2
        span_As = con.span_As_2
        As = con.As_1  # cross sectional area of a stringer
        q = con.q2
    else:
        span_n1 = con.span_n1_3
        n1 = con.n1_3  # n1 is the number of stringers on the top skin
        span_n2 = con.span_n2_3
        n2 = con.n2_3  # n2 is the number of stringers on the bottom skin
        span_t1 = con.span_t1_3
        t1 = con.t1_3
        span_t2 = con.span_t2_3
        t2 = con.t2_3
        span_As = con.span_As_3
        As = con.As_3  # cross sectional area of a stringer
        q = con.q3
    n1_inter = sp.interpolate.interp1d(span_n1, n1, kind="previous", fill_value="extrapolate")
    n2_inter = sp.interpolate.interp1d(span_n2, n2, kind="previous", fill_value="extrapolate")
    t1_inter = sp.interpolate.interp1d(span_t1, t1, kind="previous", fill_value="extrapolate")
    t2_inter = sp.interpolate.interp1d(span_t2, t2, kind="previous", fill_value="extrapolate")
    As_inter = sp.interpolate.interp1d(span_As, As, kind="previous", fill_value="extrapolate")

    n1 = n1_inter(y)
    n2 = n2_inter(y)
    t1 = t1_inter(y)
    t2 = t2_inter(y)
    As = As_inter(y)

    d1, d2, d3, d4, = Wingbox_lengths(d1_root, d2_root, d3_root, d4_root, b, y)
    alpha = math.atan((d1 - d3) / d2)
    L = (d1 - d3) / math.cos(alpha)
    sb = L / (n2 - 1)
    st = d2 / (n1 - 1)
    h, x = CentroidZcontribution(As, sb, st, alpha, n2, n1, d1, d2, d3, d4, t1, t2)

    if y < q:
        Ixx = Ixx2calculator(d1, d2, L, d3, t1, t2, h, alpha, n1, n2, As, sb, d4)
    else:
        Ixx = Ixxcalculator(d1, d2, L, d3, t1, t2, h, alpha, n1, n2, As, sb)
    return Ixx


y_tab = []
Ixx_tab=[]
i = 0
step = 0.05
count = 0
b = con.b

while i <= b / 2:
    i = i + step
    y_tab.append(i)
    count = count + 1

for y in y_tab:
     Ixy = Ixyfinal(1, y)
     Ixy_tab.append(Ixx)

plt.plot(y_tab, Ixx_tab)
plt.xlabel('Position along half-span (m)')
plt.ylabel('Ixx (m^4)')
plt.title('Moment of inertia at each position along the half-span ')
plt.show()



(t1*d1*x*(h-d1/2))
-(t1*d3(x-d2)*(L*sin(alpha)+(d3/2)-h))
+(d2*t2*(h-d1)*(x-d2))
+(((L**3)*t2*sin(alpha)*cos(alpha)/12)+(Lt2*(x-d2)(h-(L*sin(alpha)/2))))
-((d1-u)t1*(x-d4)*(u-h+((d1-u)/2)))
