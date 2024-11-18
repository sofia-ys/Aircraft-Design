import numpy as np
import matplotlib.pyplot as plt
from scipy.interpolate import interp1d
import re

# Step 1: Read the file and extract values for y-span, chord, Ai, Cl, etc.
file_path = 'Wing Structure/XFLR5_files/MainWing_a=0.00_v=10.00ms.txt'

# Initialize lists for each column
y_span = []
chord = []
ai = []
cl = []
pcd = []
icd = []
cm_geom = []
cm_airf = []
xtr_top = []
xtr_bot = []
xcp = []
bm = []

with open(file_path, 'r') as file:
    for line in file:
        # Adjust regex pattern to capture each column
        match = re.match(
            r'\s*(-?\d+\.\d+)\s+(-?\d+\.\d+)\s+(-?\d+\.\d+)\s+(-?\d+\.\d+)\s+(-?\d+\.\d+)\s+(-?\d+\.\d+)\s+(-?\d+\.\d+)\s+(-?\d+\.\d+)\s+(-?\d+\.\d+)\s+(-?\d+\.\d+)\s+(-?\d+\.\d+)\s+(-?\d+\.\d+)',
            line
        )
        if match:
            # Append each matched group to its respective list
            y_span.append(float(match.group(1)))
            chord.append(float(match.group(2)))
            ai.append(float(match.group(3)))
            cl.append(float(match.group(4)))
            pcd.append(float(match.group(5)))
            icd.append(float(match.group(6)))
            cm_geom.append(float(match.group(7)))
            cm_airf.append(float(match.group(8)))
            xtr_top.append(float(match.group(9)))
            xtr_bot.append(float(match.group(10)))
            xcp.append(float(match.group(11)))
            bm.append(float(match.group(12)))

# Convert lists to numpy arrays
y_span = np.array(y_span)
chord = np.array(chord)
ai = np.array(ai)
cl = np.array(cl)
pcd = np.array(pcd)
icd = np.array(icd)
cm_geom = np.array(cm_geom)
cm_airf = np.array(cm_airf)
xtr_top = np.array(xtr_top)
xtr_bot = np.array(xtr_bot)
xcp = np.array(xcp)
bm = np.array(bm)

# Step 2: Create interpolation functions for each value
chord_interp = interp1d(y_span, chord, kind='cubic')
ai_interp = interp1d(y_span, ai, kind='cubic')
cl_interp = interp1d(y_span, cl, kind='cubic')
pcd_interp = interp1d(y_span, pcd, kind='cubic')
icd_interp = interp1d(y_span, icd, kind='cubic')
cm_geom_interp = interp1d(y_span, cm_geom, kind='cubic')
cm_airf_interp = interp1d(y_span, cm_airf, kind='cubic')
xtr_top_interp = interp1d(y_span, xtr_top, kind='cubic')
xtr_bot_interp = interp1d(y_span, xtr_bot, kind='cubic')
xcp_interp = interp1d(y_span, xcp, kind='cubic')
bm_interp = interp1d(y_span, bm, kind='cubic')

# Step 3: Define functions that take y-span and angle of attack (AoA) as inputs
# For this example, AoA is used as a parameter; if you have specific calculations
# based on AoA, adjust accordingly.

def get_chord(y, aoa=0):
    return chord_interp(y)

def get_ai(y, aoa=0):
    return ai_interp(y)  # Modify as needed if AoA-dependent

def get_cl(y, aoa=0):
    return cl_interp(y)  # Modify as needed if AoA-dependent

def get_pcd(y, aoa=0):
    return pcd_interp(y)

def get_icd(y, aoa=0):
    return icd_interp(y)

def get_cm_geom(y, aoa=0):
    return cm_geom_interp(y)

def get_cm_airf(y, aoa=0):
    return cm_airf_interp(y)

def get_xtr_top(y, aoa=0):
    return xtr_top_interp(y)

def get_xtr_bot(y, aoa=0):
    return xtr_bot_interp(y)

def get_xcp(y, aoa=0):
    return xcp_interp(y)

def get_bm(y, aoa=0):
    return bm_interp(y)

# Example usage
y_example = 0.0  # Example y-span value
print("Chord at y =", y_example, ":", get_chord(y_example))
print("Cl at y =", y_example, ":", get_cl(y_example))