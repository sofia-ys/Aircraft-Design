import numpy as np
import matplotlib.pyplot as plt
from scipy.interpolate import interp1d
import re

# Paths to files for different angles of attack
file_aoa0_path = 'Wing Structure/XFLR5_files/MainWing_a=0.00_v=10.00ms.txt'
file_aoa10_path = 'Wing Structure/XFLR5_files/MainWing_a=10.00_v=10.00ms.txt'

# Function to read data and create interpolation functions for a given file
def load_data(file_path):
    # Define all the lists
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
    # Open the file
    with open(file_path, 'r') as file:
        # This is just to process the XFLR5 output files and save the results to the lists
        #---------------------------------------------------------------------------------
        for line in file:
            match = re.match(
                r'\s*(-?\d+\.\d+)\s+(-?\d+\.\d+)\s+(-?\d+\.\d+)\s+(-?\d+\.\d+)\s+(-?\d+\.\d+)\s+(-?\d+\.\d+)\s+(-?\d+\.\d+)\s+(-?\d+\.\d+)\s+(-?\d+\.\d+)\s+(-?\d+\.\d+)\s+(-?\d+\.\d+)\s+(-?\d+\.\d+)',
                line
            )
            if match:
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
        #---------------------------------------------------------------------------------
    # Get a numpy array out of the span locations analyzed
    y_span = np.array(y_span)
    # Create parameters for the interpolation functions
    interpolations = {
        'chord': interp1d(y_span, chord, kind='cubic'),
        'ai': interp1d(y_span, ai, kind='cubic'),
        'cl': interp1d(y_span, cl, kind='cubic'),
        'icd': interp1d(y_span, icd, kind='cubic'),
        'cm_airf': interp1d(y_span, cm_airf, kind='cubic'),
    }
    return y_span, interpolations

# Load data for AoA 0 and AoA 10
y_span_aoa0, interpolations_aoa0 = load_data(file_aoa0_path)
y_span_aoa10, interpolations_aoa10 = load_data(file_aoa10_path)

# Define functions to access interpolated values based on AoA (we only have 0 and 10) and y location
def get_value(param, y, aoa):
    if aoa == 0:
        return interpolations_aoa0[param](y)
    elif aoa == 10:
        return interpolations_aoa10[param](y)
    else:
        raise ValueError("Angle of attack must be 0 or 10 degrees.")

# Specific interpolated functions for each parameter, you just insert any y location and the desired angle of attack & you get the output
def get_chord(y, aoa):
    return get_value('chord', y, aoa)

def get_ai(y, aoa):
    return get_value('ai', y, aoa)

def get_cl(y, aoa):
    return get_value('cl', y, aoa)

def get_icd(y, aoa):
    return get_value('icd', y, aoa)

def get_cm_geom(y, aoa):
    return get_value('cm_geom', y, aoa)

def get_cm_airf(y, aoa):
    return get_value('cm_airf', y, aoa)

#----------------------------------------------
# THIS IS JUST TO DO SANITY CHECK WITH PLOTTING
#----------------------------------------------
# Define a range of y values for smooth plotting
y_new = np.linspace(min(y_span_aoa0), max(y_span_aoa0), 100) #note that y_span_aoa0 or y_span_aoa10 are same, I just needed to get the y_span out of the load function

# Plot each parameter for AoA = 0 and AoA = 10
def plot_all_parameters():
    plt.figure(figsize=(12, 18))
    
    # Plot chord
    plt.subplot(3, 2, 1)
    plt.plot(y_new, get_chord(y_new, 0), label='Chord (AoA=0)')
    plt.plot(y_new, get_chord(y_new, 10), label='Chord (AoA=10)', linestyle='--')
    plt.xlabel('Span (y)')
    plt.ylabel('Chord')
    plt.title('Chord Distribution along Span')
    plt.legend()
    plt.grid(True)

    # Plot ai
    plt.subplot(3, 2, 2)
    plt.plot(y_new, get_ai(y_new, 0), label='Ai (AoA=0)')
    plt.plot(y_new, get_ai(y_new, 10), label='Ai (AoA=10)', linestyle='--')
    plt.xlabel('Span (y)')
    plt.ylabel('Ai')
    plt.title('Ai Distribution along Span')
    plt.legend()
    plt.grid(True)

    # Plot cl
    plt.subplot(3, 2, 3)
    plt.plot(y_new, get_cl(y_new, 0), label='Cl (AoA=0)')
    plt.plot(y_new, get_cl(y_new, 10), label='Cl (AoA=10)', linestyle='--')
    plt.xlabel('Span (y)')
    plt.ylabel('Cl')
    plt.title('Cl Distribution along Span')
    plt.legend()
    plt.grid(True)

    # Plot icd
    plt.subplot(3, 2, 4)
    plt.plot(y_new, get_icd(y_new, 0), label='ICd (AoA=0)')
    plt.plot(y_new, get_icd(y_new, 10), label='ICd (AoA=10)', linestyle='--')
    plt.xlabel('Span (y)')
    plt.ylabel('ICd')
    plt.title('ICd Distribution along Span')
    plt.legend()
    plt.grid(True)

    # Plot cm_airf
    plt.subplot(3, 2, 5)
    plt.plot(y_new, get_cm_airf(y_new, 0), label='CmAirf (AoA=0)')
    plt.plot(y_new, get_cm_airf(y_new, 10), label='CmAirf (AoA=10)', linestyle='--')
    plt.xlabel('Span (y)')
    plt.ylabel('CmAirf')
    plt.title('CmAirf Distribution along Span')
    plt.legend()
    plt.grid(True)
    
    plt.tight_layout()
    plt.show()

# Call the function to plot all parameters
plot_all_parameters()