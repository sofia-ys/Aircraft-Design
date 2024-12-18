import numpy as np
import wing_box_constants as wb
import sys
sys.path.append('Wing Structure')
import Ixx
import matplotlib.pyplot as plt
#half-span divided into 100 sections
y_values = array = np.linspace(0, wb.b / 2, 100)

def getSparHeight(spar_id, y): # get b
    d = []
    d = Ixx.Wingbox_lengths(wb.d_1, wb.d_2, wb.d_3, wb.d_4, wb.b, y)
    if(spar_id > 3 or spar_id < 0):
        print('spar id out of range')
    else:
        return d[spar_id - 1]

def getSparThickness(span_t1, t1, y):
    spar_thickness = 0
    for i in range(len(span_t1) - 1):  # adjustable to the number of discontinuities for the design types
        if span_t1[i] < y <= span_t1[i+1]:  # between the first point in the list and the next point
            spar_thickness = t1[i]  # spar thickness is that point
        elif y > span_t1[i+1]:  # just in case out of range
            print("Spar position out of range")
    return spar_thickness


def getCritShear(k_s, E, poisson, t, b):
    tau_cr = np.pi**2 * k_s * E / (12 * (1 - poisson**2)) * (t/b)**2 
    return tau_cr

#insert a shear force value V (needs to be integrated from the distribution at a particular span y
def avgShear(y, h, t):
    #compute the shear force at a particular span y by integrating
    
    denominator = 0
    for i in range(0, len(h)):
        denominator += h[i] * t
    avg_shear = V / denominator
    return avg_shear

def maxShear(avg_shear, k_v = wb.k_v):
    return avg_shear * k_v

#tau_cr = criticalShear(wb.k_s1, wb.E, wb.poisson, wb.spar_t1, wb.spar_b1)

def get_ks(a, b):
    values = [15, 13.6, 12.8, 12.3, 11.9, 11.6, 11.35, 11, 10.8, 10.55, 10.35, 10.2, 10.1, 10, 9.9, 9.85, 9.8, 9.78, 9.76, 9.74, 9.73, 9.7, 9.68, 9.64, 9.62, 9.6, 9.58, 9.56, 9.54, 9.54, 9.54, 9.52, 9.52, 9.52, 9.52, 9.52, 9.52, 9.53, 9.53, 9.53, 9.53]
    aspect_ratio = a/b
    # Return 9.53 if the input number is greater than 5
    if aspect_ratio > 5:
        return 9.53

    # Calculate the index from the input number
    increment = 0.1
    start_value = 1.0
    index = (aspect_ratio - start_value) / increment

    # Ensure the index is within bounds
    if index < 0 or index >= len(values) - 1:
        print(str(index) + ' :')
        raise ValueError("Input number is out of interpolation range.")

    # Find the lower and upper bounds for interpolation
    lower_index = int(index)
    upper_index = lower_index + 1

    # Perform linear interpolation
    lower_value = values[lower_index]
    upper_value = values[upper_index]
    fraction = index - lower_index

    interpolated_value = lower_value + fraction * (upper_value - lower_value)
    return interpolated_value

def get_bay_width(y, lst):
    for i in range(len(lst) - 1):
        if lst[i] <= y < lst[i + 1]:  # Check if y lies between two consecutive elements
            return lst[i + 1] - lst[i]  # Return the width of the bay
    return None  # Return None if y is not within any range
        
def getCritSkinBuckling(k_c, E, poisson, t, b):
    omega_cr = np.pi**2 * k_c * E / (12 * (1 - poisson**2)) * (t/b)**2 
    return omega_cr

crit_shear_spar1 = []
crit_shear_spar2 = []
crit_shear_spar3 = []

t1_vals = [wb.t1_1, wb.t1_2, wb.t1_3]
t1_spans = [wb.span_t1_1, wb.span_t1_2, wb.span_t1_3]
t2_vals = [wb.t2_1, wb.t2_2, wb.t2_3]
t2_spans = [wb.span_t2_1, wb.span_t2_2, wb.span_t2_3]
q_values = [wb.q1, wb.q2, wb.q3]

def plotCritShear(E, poisson, y_values):
    for design_id in range(0,2):
        for y in y_values:
            if(get_bay_width(y, wb.ribs)/getSparHeight(1, y) < 1):
                continue
            for i in y_values: #for debug
                print(get_bay_width(i, wb.ribs))
            crit_shear_spar1.append(getCritShear(get_ks(getSparHeight(1, y), get_bay_width(y, wb.ribs)), E, poisson, getSparThickness(t1_spans[design_id], t1_vals[design_id], y), getSparHeight(1, y)))
            print("Critical shear spar 1: " + str(crit_shear_spar1))
            crit_shear_spar2.append(getCritShear(get_ks(getSparHeight(2, y), get_bay_width(y, wb.ribs)), E, poisson, getSparThickness(t1_spans[design_id], t1_vals[design_id], y), getSparHeight(2, y)))
            print("Critical shear spar 2: " + str(crit_shear_spar2))
            if(y < q_values[design_id]):
                crit_shear_spar3.append(getCritShear(get_ks(getSparHeight(3, y), get_bay_width(y, wb.ribs)), E, poisson, getSparThickness(t1_spans[design_id], t1_vals[design_id], y), getSparHeight(3, y)))
    plt.figure()
    plt.plot(y_values, crit_shear_spar1, label='Critical shear for spar 1')
    plt.xlabel('Spanwise Position (m)')
    plt.ylabel('Critical shear stress (Pa)')
    plt.title('Critical shear stress along the wing span')
    plt.legend()

plotCritShear(wb.E, wb.poisson, y_values)
        
def getCritSkinBuckling(spar_id, span_t2, t2, y):
    omega_cr = np.pi**2 * 7 * E / (12 * (1 - wb.poisson**2)) * (getSparThickness(span_t2, t2, y)/getSparHeight(spar_id, y))**2 
    return omega_cr
