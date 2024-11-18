import numpy as np
import matplotlib.pyplot as plt
from scipy.interpolate import interp1d
import re

# Step 1: Read the file and extract values for y-span, chord, Ai, Cl, etc.
file_aoa0_path = 'Wing Structure/XFLR5_files/MainWing_a=0.00_v=10.00ms.txt'
file_aoa10_path = 'Wing Structure/XFLR5_files/MainWing_a=10.00_v=10.00ms.txt'

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

with open(file_aoa0_path, 'r') as file_0:
    for line in file_0:
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

# Step 3: Define a range of y values for smooth plotting
y_new = np.linspace(min(y_span), max(y_span), 100)

# Step 4: Plot each interpolated parameter
plt.figure(figsize=(12, 18))

# Plot chord
def plotEverything():  
    plt.subplot(6, 2, 1)
    plt.plot(y_new, chord_interp(y_new), label='Chord')
    plt.xlabel('Span (y)')
    plt.ylabel('Chord')
    plt.title('Chord Distribution along Span')
    plt.grid(True)

    # Plot ai
    plt.subplot(6, 2, 2)
    plt.plot(y_new, ai_interp(y_new), label='Ai')
    plt.xlabel('Span (y)')
    plt.ylabel('Ai')
    plt.title('Ai Distribution along Span')
    plt.grid(True)

    # Plot cl
    plt.subplot(6, 2, 3)
    plt.plot(y_new, cl_interp(y_new), label='Cl')
    plt.xlabel('Span (y)')
    plt.ylabel('Cl')
    plt.title('Cl Distribution along Span')
    plt.grid(True)

    # Plot pcd
    plt.subplot(6, 2, 4)
    plt.plot(y_new, pcd_interp(y_new), label='PCd')
    plt.xlabel('Span (y)')
    plt.ylabel('PCd')
    plt.title('PCd Distribution along Span')
    plt.grid(True)

    # Plot icd
    plt.subplot(6, 2, 5)
    plt.plot(y_new, icd_interp(y_new), label='ICd')
    plt.xlabel('Span (y)')
    plt.ylabel('ICd')
    plt.title('ICd Distribution along Span')
    plt.grid(True)

    # Plot cm_geom
    plt.subplot(6, 2, 6)
    plt.plot(y_new, cm_geom_interp(y_new), label='CmGeom')
    plt.xlabel('Span (y)')
    plt.ylabel('CmGeom')
    plt.title('CmGeom Distribution along Span')
    plt.grid(True)

    # Plot cm_airf
    plt.subplot(6, 2, 7)
    plt.plot(y_new, cm_airf_interp(y_new), label='CmAirf')
    plt.xlabel('Span (y)')
    plt.ylabel('CmAirf')
    plt.title('CmAirf Distribution along Span')
    plt.grid(True)

    # Plot xtr_top
    plt.subplot(6, 2, 8)
    plt.plot(y_new, xtr_top_interp(y_new), label='XTrTop')
    plt.xlabel('Span (y)')
    plt.ylabel('XTrTop')
    plt.title('XTrTop Distribution along Span')
    plt.grid(True)

    # Plot xtr_bot
    plt.subplot(6, 2, 9)
    plt.plot(y_new, xtr_bot_interp(y_new), label='XTrBot')
    plt.xlabel('Span (y)')
    plt.ylabel('XTrBot')
    plt.title('XTrBot Distribution along Span')
    plt.grid(True)

    # Plot xcp
    plt.subplot(6, 2, 10)
    plt.plot(y_new, xcp_interp(y_new), label='XCP')
    plt.xlabel('Span (y)')
    plt.ylabel('XCP')
    plt.title('XCP Distribution along Span')
    plt.grid(True)

    # Plot bm
    plt.subplot(6, 2, 11)
    plt.plot(y_new, bm_interp(y_new), label='BM')
    plt.xlabel('Span (y)')
    plt.ylabel('BM')
    plt.title('BM Distribution along Span')
    plt.grid(True)

    plt.tight_layout()
    plt.show()

plotEverything()