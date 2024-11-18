import numpy as np
from scipy.interpolate import interp1d
import re

# Step 1: Read the file and extract y-span and Cl values
file_path = 'MainWing_a=0.00_v=10.00ms.txt'
y_span = []
cl_values = []

with open(file_path, 'r') as file:
    for line in file:
        # Use regex to match lines with numerical data in the expected format
        match = re.match(r'\s*(-?\d+\.\d+)\s+[\d\.\-]+\s+[\d\.\-]+\s+([\d\.\-]+)', line)
        if match:
            y_span.append(float(match.group(1)))  # y-span values
            cl_values.append(float(match.group(2)))  # Cl values

# Convert lists to numpy arrays
y_span = np.array(y_span)
cl_values = np.array(cl_values)

# Step 2: Interpolate using scipy's interp1d
cl_interp_function = interp1d(y_span, cl_values, kind='cubic')

# Example usage of the interpolation function
y_new = np.linspace(min(y_span), max(y_span), 100)  # New y-span points for evaluation
cl_new = cl_interp_function(y_new)

print("Interpolated Cl values:", cl_new)
