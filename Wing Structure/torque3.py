import math as m
import scipy as sp
from scipy import integrate
from input_xflr_data import get_cm_airf, get_chord, get_cl
from input_xflr_data import *
import numpy as np


aoa = 0
rho = 0.4
v = 100 
q = 0.5*rho*v**2



def lift_dist(x, aoa):
    return 0.5 * get_cl(x, aoa) * q * get_chord(x, aoa)

def d(x, aoa):
    return 0.25 * get_chord(x, aoa)

def h(x, aoa):
    return lift_dist(x,aoa) * d(x,aoa)

def torque_dist(x, aoa):
    return integrate.quad(lambda x: lift_dist(x,aoa) * d(x,aoa), min(y_new), x)[0]


x_values = np.linspace(min(y_new), 0, 100)

torque_values = [torque_dist(x, aoa) for x in x_values]

# Plotting the torque distribution
plt.figure()
plt.plot(x_values, torque_values, label='Torque Distribution', color='b')
plt.xlabel('Spanwise Position (m)')
plt.ylabel('Torque (Nm)')
plt.title('Torque Distribution along the Wing Span')
plt.legend()
plt.grid(True)
plt.show()

