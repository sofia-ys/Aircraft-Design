from Ixx import Ixxfinal
from shear_bending_flight import getBendingMomentFlight
import scipy as sp
import matplotlib.pyplot as plt
import constants as con

E = 70 * 10^9 # change it when you choose material
b = con.b
#import Moment function
def bending_moment(y):
    return getBendingMomentFlight(y, -1)
#import moment of inertia function
def Ixx(y):
    return Ixxfinal(1,y)
def second_derivative_deflection(y):
    return -1 * bending_moment(y) / (E * Ixx(y))
def first_derivative_deflection(y):
    slope,error = sp.integrate.quad(second_derivative_deflection,0,y)
    return slope
def deflection(y):
    defl,error = sp.integrate.quad(first_derivative_deflection,0,y)
    return defl
y_tab = []
step = 0.05
y = 0
step_number = 0
deflection_tab = []
slope_tab = []
while y <= b / 2 :
    y_tab.append(y)
    y = y + step
    step_number = step_number + 1
for el in y_tab:
    slope_tab.append(first_derivative_deflection(el))
    deflection_tab.append(deflection(el))
plt.plot(y_tab, slope_tab, label='Slope')
plt.xlabel('Position along half-span')
plt.ylabel('Slope at each point along half-span')


plt.plot(y_tab, deflection_tab)
plt.xlabel('Position along half-span')
plt.ylabel('Deflection')
plt.show()
