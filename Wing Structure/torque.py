import math as m
import scipy as sp
from scipy import integrate
from input_xflr_data import get_cm_airf, get_chord, get_cl
from input_xflr_data import *
import numpy as np
from constants import *

#CM 1/4 vs CM 1/2
aoa = 0
rho = density_cruise
v = V_cruise
q = 0.5*rho*v**2
we = 3008*9.81 #engine weight

pos = 9
thrust = 80000 # [N]
d_thrust = -1.1 
d_engine = 2.6 



def thrust_dsit(x,pos, d_thrust):
    if x < pos or x < -pos:
        return thrust*d_thrust
    else:
        return 0 

def ew_dsit(x,pos, d_engine):
    if x < pos or x < -pos:
        return we*d_engine
    else:
        return 0 



def lift_dist(x, aoa):
    return get_cl(x, aoa) * q * get_chord(x, aoa)

def d(x, aoa):
    return 0.25 * get_chord(x, aoa)

def h(x, aoa):
    return lift_dist(x,aoa) * d(x,aoa)

def cm_dist(x,aoa):
    return get_cm_airf(x,aoa) * q * get_chord(x,aoa)**2

def torque_dist(x, aoa, pos, d_thrust, d_engine):
    return integrate.quad(lambda x: lift_dist(x,aoa) * d(x,aoa) + cm_dist(x,aoa), x, max(y_new))[0] +  thrust_dsit(x, pos, d_thrust) + ew_dsit(x,pos, d_engine)

aoa_range = np.linspace(0, 10, 5)  # AoA values in degrees (0°, 2.5°, 5°, 7.5°, 10°)
x_values = np.linspace(0, max(y_new), 100)

# Loop over each AoA and calculate torque values
for aoa in aoa_range:
    torque_values = [torque_dist(x, aoa, pos, d_thrust, d_engine) for x in x_values]
    plt.plot(x_values, torque_values, label=f'AoA = {aoa}°')

# Plot customization
plt.xlabel('Spanwise Position (m)')
plt.ylabel('Torque (Nm)')
plt.title('Torque Distribution along the Wing Span for Different AoA')
plt.legend()
plt.grid(True)
plt.show()

