import constants as con
from Ixx import CentroidZcontribution
from Ixx import Wingbox_lengths
from math import sqrt, tan, cos, sin, radians
import scipy as sp
d1_root = con.d_1
d2_root = con.d_2
d3_root = con.d_3
d4_root = con.d_4
alpha = con.alpha
As = con.As_1
sb = con.sb
t1 = con.t1
t2 = con.t2
b = con.b
span_n1 = con.span_n1
span_n2 = con.span_n2
span_t1 = con.span_t1
span_t2 = con.span_t2
span_As = con.span_as


def Izz(d1,d2,d3,d4,alpha,t1,t2,x,As,n1,n2,L,y):

    s1 = d2 / (n1 - 1)
    s2 = L / (n2 - 1)

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

    d1, d2, d3, d4 = Wingbox_lengths(d1_root, d2_root, d3_root, d4_root, b, y)
    h, x = CentroidZcontribution(As, s2, s1, alpha, n2, n1, d1, d2, d3, d4, t1, t2)

    I_zz = d1 * t1 * x**2 + d3 * t1 * (d2 - x)**2
    I_zz = I_zz + (d1 - d4 * tan(alpha)) * t1 * (d4 - x)**2 + 1 / 12 * t2 * d2**3 + d2 * t2 * (d2 / 2 - x)**2
    I_zz = I_zz + 1 / 12 * t2 * L**3 * cos(alpha)**2 + L * t2 * (L * cos(alpha) / 2 - x) ** 2

    for i in range(0,n1):
        Izz = Izz + As * (x - s1 * i)**2
    for i in range(0,n2):
        Izz = Izz + As * (x - s2 * i * cos(alpha))**2
    return I_zz