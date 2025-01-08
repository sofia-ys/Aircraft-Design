from Ixx import CentroidZcontribution
from Ixx import Wingbox_lengths
from Ixx import Ixxfinal
from Izz import Izzcalculator
from Ixz import Ixzfinal
from shear_bending_flight import getBendingMomentFlight
import scipy
from math import atan,cos
import matplotlib.pyplot as plt
import constants as con
from longestdistance import findlongestdistance

d1_root = con.d_1
d2_root = con.d_2
d3_root = con.d_3
d4_root = con.d_4
As = con.As_4
t1 = con.t1_4
t2 = con.t2_4
b = con.b
span_n1 = con.span_n1_4
span_n2 = con.span_n2_4
span_t1 = con.span_t1_4
span_t2 = con.span_t2_4
span_As = con.span_As_4
n1 = con.n1_4
n2 = con.n2_4

n1_inter = scipy.interpolate.interp1d(span_n1, n1, kind="previous", fill_value="extrapolate")
n2_inter = scipy.interpolate.interp1d(span_n2, n2, kind="previous", fill_value="extrapolate")
t1_inter = scipy.interpolate.interp1d(span_t1, t1, kind="previous", fill_value="extrapolate")
t2_inter = scipy.interpolate.interp1d(span_t2, t2, kind="previous", fill_value="extrapolate")
As_inter = scipy.interpolate.interp1d(span_As, As, kind="previous", fill_value="extrapolate")

x_compressive = 1.3 # change this when the function calculates the maximum distance is imported
z_compressive =0.33 # change this when the function calculates the maximum distance is imported
x_tensile = 1.3 # change this when the function calculates the maximum distance is imported
z_tensile = 0.33 # change this when the function calculates the maximum distance is imported
y = 0
step = 0.1
tensile_stress_tab = []
compressive_stress_tab = []
y_tab = []
def bending_moment(y):
    return getBendingMomentFlight(y, 2.5)

while y<=b/2 :
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
    sb = s2
    st = s1
    h, x = CentroidZcontribution(As, s2, s1, alpha, n2, n1, d1, d2, d3, d4, t1, t2)
    print(Ixxfinal(4,y))
    x_tensile, z_tensile, x_compressive, z_compressive = findlongestdistance(d1, d2, L, d3, d4, t1, t2, h, alpha, n1, n2, As, x, 4, y)
    tensile_stress = ((bending_moment(y) * Izzcalculator(d1, d2, d3, d4, alpha, t1, t2, x, As, n1, n2, L, y) * z_tensile) - (bending_moment(y) * Ixzfinal(4,y) * x_tensile)) / (Ixxfinal(4,y) * Izzcalculator(d1, d2, d3, d4, alpha, t1, t2, x, As, n1, n2, L, y) - Ixzfinal(4,y)**2)
    compressive_stress = ((bending_moment(y) * Izzcalculator(d1, d2, d3, d4, alpha, t1, t2, x, As, n1, n2, L,y) * z_compressive) - (bending_moment(y) * Ixzfinal(4, y) * x_compressive)) / (Ixxfinal(4, y) * Izzcalculator(d1, d2, d3, d4, alpha, t1, t2, x, As, n1, n2, L,y) - Ixzfinal(4, y) ** 2)
    tensile_stress_tab.append(tensile_stress)
    compressive_stress_tab.append(compressive_stress)
    y_tab.append(y)
    y += step
plt.figure(figsize=(10, 5))

plt.subplot(1, 2, 1)
plt.plot(y_tab, tensile_stress_tab, label="Tensile", color='blue')
plt.xlabel('Position along half-span')
plt.ylabel('Stress [Pa]')
plt.title('Tensile Stress')
plt.legend()

plt.subplot(1, 2, 2)
plt.plot(y_tab, compressive_stress_tab, label="Compressive", color='red')
plt.xlabel('Position along half-span')
plt.ylabel('Stress [Pa]')
plt.title('Compressive Stress')
plt.legend()

plt.tight_layout()
plt.show()


safety_margin_compressive_tab = [4.5e8 / stress for stress in compressive_stress_tab]
safety_margin_tensile_tab = [4.5e8 / stress for stress in tensile_stress_tab]
safety_margin_compressive_tab = safety_margin_compressive_tab[:-15]
safety_margin_tensile_tab = safety_margin_tensile_tab[:-15]
y_tab2 = y_tab[:-15]

plt.plot(y_tab2, safety_margin_tensile_tab, label="Tensile", color='blue')
plt.xlabel('Position along half-span')
plt.ylabel('Margin of safety')
plt.title('Margin of safety for tensile strength failure')
plt.legend()
plt.show()


plt.plot(y_tab2, safety_margin_compressive_tab, label="compressive", color='blue')
plt.xlabel('Position along half-span')
plt.ylabel('Margin of safety')
plt.title('Margin of safety for compressive strength failure')
plt.legend()
plt.show()

min_safety_compressive = min(safety_margin_compressive_tab)
min_safety_tensile = min(safety_margin_tensile_tab)
print(min_safety_tensile)
print(min_safety_compressive)