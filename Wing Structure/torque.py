import math as m
import scipy as sp
from scipy import integrate
from extra_constants import *
from input_xflr_data import get_cm_airf, get_chord, get_cl
from input_xflr_data import *
thust_torque = 1 #Ignoring the drag becasue invicid fow

# Engine thrust parameters
T = 80000  # Engine thrust in N (replace with actual value)
y_engine = 1.18  # Engine position along the span (e.g., at the centerline)

angl = 0
# Input data
y = y_new # Placeholder for spanwise locations
Cm_14 = get_cm_airf(y_new, angl)  # Pitching moment coefficient
c = get_chord(y_new, angl)  # Placeholder for chord distribution
Cl = get_cl(y_new, angl)  # Placeholder for lift coefficient distribution
print(c)
# Parameters
import numpy as np
import matplotlib.pyplot as plt



# Engine thrust parameters


# Aerodynamic parameters
rho = 1.225  # Air density in kg/m^3 (at sea level)
V = 50.0  # Flight velocity in m/s
q_inf = 0.5 * rho * V**2  # Dynamic pressure

# Calculate the lift distribution
L = q_inf * c * Cl  # Lift at each spanwise location

# Calculate the pitching moment distribution
M_pitch = q_inf * c**2 * Cm_14  # Pitching moment at each spanwise location

# Engine thrust torque (simple linear contribution from the engine location)
thrust_moment = T * (y - y_engine)

# Numerical integration using trapezoidal rule
# We use the trapezoidal rule to approximate the integrals of the lift and pitching moment distributions
torque_lift = np.trapz(L * (y[:, None] - y), y, axis=0)  # Integral of lift contribution
torque_pitch = np.trapz(M_pitch * (y[:, None] - y), y, axis=0)  # Integral of pitching moment contribution

# Total torque at each spanwise location
torque = torque_lift + torque_pitch + thrust_moment

# Boundary conditions: Torque at both wing tips (y = -17 and y = 17) should be zero
torque[0] = 0  # Enforce torque at the left wingtip (y = -17) to be zero
torque[-1] = 0  # Enforce torque at the right wingtip (y = 17) to be zero

# Plot the torque distribution along the wing
plt.figure(figsize=(10, 6))
plt.plot(y, torque, label="Torque Distribution")
plt.xlabel("Spanwise Location (y) [m]")
plt.ylabel("Torque [Nm]")
plt.title("Torque Distribution Over the Wing Including Engine Thrust")
plt.grid()
plt.legend()
plt.show()


