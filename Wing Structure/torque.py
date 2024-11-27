import math as m
import scipy as sp
from scipy import integrate
from input_xflr_data import get_cm_airf, get_chord, get_cl
from input_xflr_data import *
import numpy as np
from constants import *

#CM 1/4 vs CM 1/2
aoa = 10
rho = density_cruise
v = V_cruise 
q = 0.5*rho*v**2
we = 3008*9.81 #engine weight

pos = 6.2
thrust = 80000 # [N]
d_thrust = -1.1 # vertical distance of engines [m]
d_engine = 2.6 # horizontal distance of engine relative to torsion box[m]
weight = 78826 # [kg]


def total_thrust(aoa, weight):
    cl=0
    cd=0
    x_values = np.linspace(0, max(y_new), 100)
    for x in x_values:
        cl += get_cl(x, aoa)
        cd = cd + get_icd(x,aoa) + C_D_0
    return ((cd/cl)*weight*9.80665) 


def thrust_dsit(x,pos, d_thrust, t_thrust):
    if x < pos or x < -pos:
        return t_thrust*d_thrust
    else:
        return 0 

def ew_dsit(x,pos, d_engine):  # engine weight distance
    if x < pos or x < -pos:
        return we*d_engine
    else:
        return 0 



def lift_dist(x, aoa):
    return get_cl(x, aoa) * q * get_chord(x, aoa)

def d(x, aoa):    #distance from quarter cord to centroid of wing box
    return 0.25 * get_chord(x, aoa)

def cm_dist(x,aoa):
    return get_cm_airf(x,aoa) * q * get_chord(x,aoa)**2

def torque_dist(x, aoa, pos, d_thrust, d_engine):
    return integrate.quad(lambda x: lift_dist(x,aoa) * d(x,aoa) + cm_dist(x,aoa), x, max(y_new))[0] +  thrust_dsit(x, pos, d_thrust, t_thrust) + ew_dsit(x,pos, d_engine)


x_values = np.linspace(0, max(y_new), 100)
aoa_range = np.linspace(0, 10, 5)  # AoA values in degrees (0°, 2.5°, 5°, 7.5°, 10°)


# Plotting the torque distraibution
plt.figure()
# Loop over each AoA and calculate torque values
for aoa in aoa_range:
    t_thrust = total_thrust(aoa, weight)
    torque_values = [torque_dist(x, aoa, pos, d_thrust, d_engine) for x in x_values]
    plt.plot(x_values, torque_values, label=f'AoA = {aoa}°')

# Plot customization
plt.xlabel('Spanwise Position (m)')
plt.ylabel('Torque (Nm)')
plt.title('Torque Distribution along the Wing Span for Different AoA')
plt.legend()
plt.grid(True)
plt.show()

'''
import numpy as np
import matplotlib.pyplot as plt
from scipy import integrate
from input_xflr_data import get_cm_airf, get_chord, get_cl, get_icd
from constants import density_cruise, V_cruise, C_D_0

# Constants
rho = density_cruise
v = V_cruise
q = 0.5 * rho * v ** 2
we = 3008 * 9.81  # Engine weight [N]

# Parameters
pos = 9  # Position of engines from centerline [m]
thrust = 80000  # Thrust [N]
d_thrust = -1.1  # Vertical distance of engines [m]
d_engine = 2.6  # Horizontal distance of engine relative to torsion box [m]
weight = 78826  # Aircraft weight [kg]

# Spanwise positions (y_new represents half-span)
wing_half_span = 18  # Assuming half-span of 18 meters (full span of 36 meters)
y_new = np.linspace(0, wing_half_span, 100)

# Spanwise positions (assuming y_new is available and represents half-span)
x_values = y_new  # Use y_new as the x positions along the wing span


# Define functions for distributions
def lift_dist(x, aoa):
    cl = get_cl(x, aoa)
    chord = get_chord(x, aoa)
    return cl * q * chord


def d(x):  # Distance from quarter chord to centroid of wing box
    return 0.2 * get_chord(x, 0)  # Assuming chord distribution doesn't change significantly with AoA


def cm_dist(x, aoa):
    cm = get_cm_airf(x, aoa)
    chord = get_chord(x, aoa)
    return cm * q * chord ** 2


def thrust_dist(x, pos, d_thrust):
    if abs(x) <= pos:
        return thrust * d_thrust
    return 0


def ew_dist(x, pos, d_engine):
    if abs(x) <= pos:
        return we * d_engine
    return 0


# Calculate torque distribution using quad integration
def torque_dist(x, aoa, pos, d_thrust, d_engine):
    # Lift contribution integrated from current position x to the tip (wing_half_span)
    lift_contribution, _ = integrate.quad(lambda xi: lift_dist(xi, aoa) * d(xi), x, wing_half_span)

    # Aerodynamic moment contribution from current position x to the tip
    cm_contribution, _ = integrate.quad(lambda xi: cm_dist(xi, aoa), x, wing_half_span)

    # Thrust and engine weight contributions (point loads)
    thrust_contribution = thrust_dist(x, pos, d_thrust) if x <= pos else 0
    engine_weight_contribution = ew_dist(x, pos, d_engine) if x <= pos else 0

    # Total torque at position x
    return lift_contribution + cm_contribution + thrust_contribution + engine_weight_contribution


# Plotting the torque distribution
plt.figure()
aoa_range = np.linspace(0, 10, 5)  # AoA values in degrees (0°, 2.5°, 5°, 7.5°, 10°)

for aoa in aoa_range:
    # Calculate torque values along the span using quad integration
    torque_values = [torque_dist(x, aoa, pos, d_thrust, d_engine) for x in x_values]

    # Plot torque distribution
    plt.plot(x_values, torque_values, label=f'AoA = {aoa}°')

# Plot customization
plt.xlabel('Spanwise Position (m)')
plt.ylabel('Torque (Nm)')
plt.title('Torque Distribution along the Wing Span for Different AoA')
plt.legend()
plt.grid(True)
plt.show()
'''
