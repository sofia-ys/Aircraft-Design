import sys
import os
import math

# Add the parent directory to sys.path
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

# Now import the variable from aircraft_data.py
from aircraft_data import *

c_friction = 0.0029 #From fig 6.3
cd0 = S_wet_to_S *c_friction
cdi = (cl_cruise**2)/(math.pi*AR*oswald)
cd_cruise = (4/3)*cd0

l_d_max = 0.5*((math.pi*AR*oswald)/(cd0))**0.5
l_d_cruise = cl_cruise/cd_cruise


print("Cd_0",cd0, "Cd_cruise", cd_cruise)
# Drag Coefficients based on ref.area

#  Cd Zero-Lift              0.01277    (52.4 %)
#  Cd Lift-Induced           0.01022    (41.9 %)
#  Cd Compressibility        0.00071    ( 2.9 %)
#  Cd Trim                   0.00069    ( 2.8 %)
#  Delta Cd (polar-mod)      0.00000    ( 0.0 %)
#                            -------    --------
#  Cd Total                  0.02439    ( 100 %)