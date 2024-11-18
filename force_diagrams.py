import numpy as np
from scipy.interpolate import interp1d

# Load the file while skipping the header and footer
filename = "MainWing_a=10.00_v=10.00ms.txt"
data = np.genfromtxt(filename, skip_header=14, skip_footer=120, usecols=(0, 3, 4, 6))

# Extract data for positive y-coordinates
y_coords = data[:, 0]
C_l = data[:, 1]
C_d = data[:, 2]
C_m = data[:, 3]

# Filter positive y-coordinates (assuming symmetry in the spanwise distribution)
positive_y_mask = y_coords > 0
ylst = y_coords[positive_y_mask]
Cllst = C_l[positive_y_mask]
Cdlst = C_d[positive_y_mask]
Cmlst = C_m[positive_y_mask]

# Create interpolation functions
lift_interp = interp1d(ylst, Cllst, kind='cubic', fill_value="extrapolate")
drag_interp = interp1d(ylst, Cdlst, kind='cubic', fill_value="extrapolate")
moment_interp = interp1d(ylst, Cmlst, kind='cubic', fill_value="extrapolate")

# Example: Compute coefficients at a specific y-location
y_query = 5.0
print(f"Lift coefficient at y={y_query}: {lift_interp(y_query):.5f}")
print(f"Drag coefficient at y={y_query}: {drag_interp(y_query):.5f}")
print(f"Moment coefficient at y={y_query}: {moment_interp(y_query):.5f}")
