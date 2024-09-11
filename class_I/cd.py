import sys
import os

# Add the parent directory to sys.path
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

# Now import the variable from aircraft_data.py
from aircraft_data import *

c_friction = 0.0029 #From fig 6.3
cd0 = S_wet_to_S *c_friction
cdi = 0