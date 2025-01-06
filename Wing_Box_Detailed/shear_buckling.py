import numpy as np
import wing_box_constants as wb
import sys
sys.path.append('Wing Structure')
import Ixx
import matplotlib.pyplot as plt
import math
#half-span divided into 100 sections
y_values = array = np.linspace(0, wb.b / 2, 100)

def getSparHeight(design_id, spar_id, y): # get b
    d = []
    d = Ixx.Wingbox_lengths(wb.all_spar_d[design_id][0], wb.all_spar_d[design_id][1], wb.all_spar_d[design_id][2], wb.all_spar_d[design_id][3], wb.b, y)
    if(spar_id == 1):
        return d[0] #dimension d1 for first spar height
    elif(spar_id == 2):
        return d[2] #dimension d3 for the second spar height
    elif(spar_id == 3):
        return (d[0] - d[3]/d[1] * (d[0] - d[2])) #d4 for middle spar, if applicable: this calculates the height of the middle spar
    else:
        print("error")

def getSparThickness(span_t1, t1, y):
    spar_thickness = 0
    for i in range(len(span_t1) - 1):  # adjustable to the number of discontinuities for the design types
        if span_t1[i] <= y and y <= span_t1[i+1]:  # between the first point in the list and the next point
            spar_thickness = t1[i]  # spar thickness is that point
        elif y >= span_t1[i+1]:
            spar_thickness = t1[i+1]
        else:
            break
            print('Spar position out of range')
    return spar_thickness

def getSkinThickness(span_t2, t2, y):
    skin_thickness = 0
    for i in range(len(span_t2) - 1):  # adjustable to the number of discontinuities for the design types
        if span_t2[i] <= y and y <= span_t2[i+1]:  # between the first point in the list and the next point
            skin_thickness = t2[i]  # spar thickness is that point
        elif y >= span_t2[i+1]:
            skin_thickness = t2[i+1]
        else:
            break
            print('Spar position out of range')
    return skin_thickness

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
    return 2  # Return None if y is not within any range
        
def getCritSkinBuckling(k_c, E, poisson, t, b):
    omega_cr = np.pi**2 * k_c * E / (12 * (1 - poisson**2)) * (t/b)**2 
    return omega_cr

crit_shear_spar1 = [[], [], []]
crit_shear_spar2 = [[], [], []]
crit_shear_spar3 = [[], [], []]

t1_vals = [wb.t1_1, wb.t1_2, wb.t1_3]
t1_spans = [wb.span_t1_1, wb.span_t1_2, wb.span_t1_3]
t2_vals = [wb.t2_1, wb.t2_2, wb.t2_3]
t2_spans = [wb.span_t2_1, wb.span_t2_2, wb.span_t2_3]
q_values = [wb.q1, wb.q2, wb.q3]

def plotCritShear(E, poisson, y_values):
    for design_id in range(0,3): #design_id is from 0 to 2, represents design cases 1 to 3!
        for y in y_values:
            crit_shear_spar1[design_id].append(getCritShear(get_ks(get_bay_width(y, wb.ribs), getSparHeight(design_id, 1, y)), E, poisson, getSparThickness(t1_spans[design_id], t1_vals[design_id], y), getSparHeight(design_id, 1, y)))
            crit_shear_spar2[design_id].append(getCritShear(get_ks(get_bay_width(y, wb.ribs), getSparHeight(design_id, 2, y)), E, poisson, getSparThickness(t1_spans[design_id], t1_vals[design_id], y), getSparHeight(design_id, 2, y)))      
            if(design_id < 2):
                crit_shear_spar3[design_id].append(getCritShear(get_ks(get_bay_width(y, wb.ribs), getSparHeight(design_id, 3, y)), E, poisson, getSparThickness(t1_spans[design_id], t1_vals[design_id], y), getSparHeight(design_id, 3, y)))
            else:
                crit_shear_spar3[design_id].append(0)
    critShearSpar1 = np.array(crit_shear_spar1)
    critShearSpar2 = np.array(crit_shear_spar2)
    critShearSpar3 = np.array(crit_shear_spar3)

    plt.figure()
    for designCase in range(0,3):
        plt.plot(y_values, critShearSpar1[designCase], label='Critical shear for spar 1, DC ' + str(designCase + 1))
        plt.plot(y_values, critShearSpar2[designCase], label='Critical shear for spar 2, DC ' + str(designCase + 1))
        print("Minimum critical shear [Pa] for spar 1 (d1), design case " + str(designCase + 1) + ": " + str(np.min(critShearSpar1[designCase])))
        print("Minimum critical shear [Pa] for spar 2 (d3), design case " + str(designCase + 1) + ": " + str(np.min(critShearSpar2[designCase])))
        if(designCase < 2):
            plt.plot(y_values, critShearSpar3[designCase], label='Critical shear for spar 3, DC ' + str(designCase + 1))
            print("Minimum critical shear [Pa] for spar 3 (mid spar), design case " + str(designCase + 1) + ": " + str(np.min(critShearSpar3[designCase])))
        
    plt.xlabel('Spanwise Position (m)')
    plt.ylabel('Critical shear stress (Pa)')
    plt.title('Critical shear stress along the wing span')
    plt.legend()
    plt.show()

def plotCritSkin(E, poisson, y_values):
    crit_skin = [[], [], []]
    for design_id in range(0,3): #design_id is from 0 to 2, represents design cases 1 to 3!
        for y in y_values:
            crit_skin[design_id].append(getCritSkinBuckling(wb.k_c, E, poisson, getSkinThickness(t2_spans[design_id], t2_vals[design_id], y), get_bay_width(y, wb.ribs)))
    crit_skin = np.array(crit_skin)

    plt.figure()
    for designCase in range(0,3):
        plt.plot(y_values, crit_skin[designCase], label='Critical shear for skin, DC ' + str(designCase + 1))
        print("Minimum critical shear [Pa] for skin, design case " + str(designCase + 1) + ": " + str(np.min(crit_skin[designCase])))
        
    plt.xlabel('Spanwise Position (m)')
    plt.ylabel('Critical shear stress (Pa)')
    plt.title('Critical shear stress along the wing span')
    plt.legend()
    plt.show()

plotCritShear(wb.E, wb.poisson, y_values)
plotCritSkin(wb.E, wb.poisson, y_values)