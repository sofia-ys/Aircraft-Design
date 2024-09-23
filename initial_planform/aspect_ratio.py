import sys
import os
import numpy as np

# Add the parent directory to sys.path
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

# Now import the variable from aircraft_data.py
from matching_diagram import landing_field_length, climb_gradient_121b
from class_I import mass_est


area = (mass_est.M_mto * 9.81) / landing_field_length
thrust = climb_gradient_121b[int(np.floor(landing_field_length))] * (mass_est.M_mto * 9.81)

print(area, thrust)