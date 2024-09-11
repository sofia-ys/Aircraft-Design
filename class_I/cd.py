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
cd_cruise = cd0 + cdi

l_d_max = 0.5*((math.pi*AR*oswald)/(cd0))**0.5
l_d_cruise = cl_cruise/cd_cruise