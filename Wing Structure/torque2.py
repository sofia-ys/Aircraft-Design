import math as m
import scipy as sp
from scipy import integrate
from constants import *
from input_xflr_data import get_cm_airf, get_chord, get_cl
from input_xflr_data import *

angl = 0
# Input data
y = y_new # Placeholder for spanwise locations
cm = get_cm_airf(y_new, angl)  # Pitching moment coefficient
c = get_chord(y_new, angl)  # Placeholder for chord distribution
cl = get_cl(y_new, angl)  # Placeholder for lift coefficient distribution
print(c)

import numpy as np
import matplotlib.pyplot as plt
from scipy.integrate import cumulative_trapezoid



thrust = 80000  # Total thrust (N)
d_thrust = 1   # Perpendicular distance of thrust from quarter chord (m)
y_thrust_positions = [-10, 10]  # Spanwise positions of engines

# Dynamic pressure (assuming q=1 for simplicity)
q = 1  # You can update this if actual values for air density and velocity are available

# Calculate lift force distribution (L(y) = Cl * q * c)
lift = cl * q * c

# Calculate aerodynamic moment about 0.5c (M_0.5c)
moment_0_5c = cm * q * c - 0.25 * lift * c  # Adjusting for mid-chord reference

# Torque due to lift at each y (integrate lift force to get torque due to lift)
torque_due_to_lift = cumulative_trapezoid(lift * (y[1] - y[0]), y, initial=0)

# Torque due to thrust
torque_due_to_thrust = np.zeros_like(y, dtype=float)
for y_thrust in y_thrust_positions:
    torque_due_to_thrust += thrust * d_thrust * (1 / (y[-1] - y[0])) * np.heaviside(y - y_thrust, 1)

# Total torque distribution
total_torque = moment_0_5c + torque_due_to_lift + torque_due_to_thrust

# Plot the torque distribution
plt.figure(figsize=(10, 6))
plt.plot(y, total_torque, label="Total Torque Distribution (0.5c)", color="blue", linewidth=2)
plt.axhline(0, color="black", linestyle="--", linewidth=0.8)
plt.title("Torque Distribution Along the Span at Mid-Chord (0.5c)")
plt.xlabel("Spanwise Position (y)")
plt.ylabel("Torque (Nm)")
plt.legend()
plt.grid()
plt.show()