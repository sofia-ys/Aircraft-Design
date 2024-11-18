import numpy as np
import matplotlib.pyplot as plt
from scipy.interpolate import interp1d
import re

file_path = ''

#function to give you the sectional lift coefficient at any span location
def getClSpan(AOA, y_dist):
    #insert the correct angle of attack into the filename
    file_path = 'Wing Structure/XFLR5_files/MainWing_' + str(AOA) + '_v=10.00ms.txt'
    print(file_path)
    #interpolate the function


# Step 1: Read the file and extract y-span and Cl values
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

# Step 2: Create interpolation function and evaluate it
cl_interp_function = interp1d(y_span, cl_values, kind='cubic')
y_new = np.linspace(min(y_span), max(y_span), 100)  # New y-span points for smooth curve
cl_new = cl_interp_function(y_new)

# Step 3: Plot the interpolated function
plt.figure(figsize=(10, 6))
plt.plot(y_new, cl_new, color='blue', label='Interpolated Cl Distribution')
plt.xlabel('Span (y)')
plt.ylabel('Lift Coefficient (Cl)')
plt.title('Interpolated Cl Distribution along the Span')
plt.legend()
plt.grid(True)
plt.show()