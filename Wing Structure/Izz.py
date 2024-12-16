import constants as con
from Ixx import CentroidZcontribution, Wingbox_lengths
from math import sqrt, tan, cos, sin, radians, acos, atan
import scipy.interpolate
import matplotlib.pyplot as plt

d1_root = con.d_1
d2_root = con.d_2
d3_root = con.d_3
d4_root = con.d_4
As = con.As_1
t1 = con.t1_1
t2 = con.t2_1
b = con.b
span_n1 = con.span_n1_1
span_n2 = con.span_n2_1
span_t1 = con.span_t1_1
span_t2 = con.span_t2_1
span_As = con.span_As_1
n1 = con.n1_1
n2 = con.n2_1

def Izzcalculator(d1, d2, d3, d4, alpha, t1, t2, x, As, n1, n2, L, y):
    s1 = d2 / (n1 - 1)
    s2 = L / (n2 - 1)
    h, x = CentroidZcontribution(As, s2, s1, alpha, n2, n1, d1, d2, d3, d4, t1, t2)

    I_zz = (
        d1 * t1 * x**2 +
        d3 * t1 * (d2 - x)**2 +
        (d1 - d4 * tan(alpha)) * t1 * (d4 - x)**2 +
        1 / 12 * t2 * d2**3 + d2 * t2 * (d2 / 2 - x)**2 +
        1 / 12 * t2 * L**3 * cos(alpha)**2 + L * t2 * (L * cos(alpha) / 2 - x) ** 2
    )

    for i in range(int(n1)):
        I_zz += As * (x - s1 * i)**2
    for i in range(int(n2)):
        I_zz += As * (x - s2 * i * cos(alpha))**2

    return I_zz

y = 0
step = 0.1
I_zz_tab = []
y_tab = []

n1_inter = scipy.interpolate.interp1d(span_n1, n1, kind="previous", fill_value="extrapolate")
n2_inter = scipy.interpolate.interp1d(span_n2, n2, kind="previous", fill_value="extrapolate")
t1_inter = scipy.interpolate.interp1d(span_t1, t1, kind="previous", fill_value="extrapolate")
t2_inter = scipy.interpolate.interp1d(span_t2, t2, kind="previous", fill_value="extrapolate")
As_inter = scipy.interpolate.interp1d(span_As, As, kind="previous", fill_value="extrapolate")

while y <= b / 2:
    n1 = n1_inter(y)
    n2 = n2_inter(y)
    t1 = t1_inter(y)
    t2 = t2_inter(y)
    As = As_inter(y)


    d1, d2, d3, d4 = Wingbox_lengths(d1_root, d2_root, d3_root, d4_root, b, y)
    alpha = atan((d1 - d3) / d2)
    L = (d1 - d3) / cos(alpha)
    s1 = d2 / (n1 - 1)
    s2 = L / (n2 - 1)
    h, x = CentroidZcontribution(As, s2, s1, alpha, n2, n1, d1, d2, d3, d4, t1, t2)
    I_zz = Izzcalculator(d1, d2, d3, d4, alpha, t1, t2, x, As, n1, n2, L, y)
    I_zz_tab.append(I_zz)
    y_tab.append(y)
    y += step

plt.plot(y_tab, I_zz_tab)
plt.xlabel('Position along half-span')
plt.ylabel('Izz [m^4]')
plt.title('Moment of inertia at each position along the half-span')
plt.show()
