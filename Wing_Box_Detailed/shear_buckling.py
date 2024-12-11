import numpy as np
import wing_box_constants as wb

def Wingbox_lengths(d1_root, d2_root, d3_root, d4_root, b, y):
    taper = wb.taper
    d1_a = d1_root + (d1_root * taper - d1_root) / (b / 2) * y
    d2_a = d2_root + (d2_root * taper - d2_root) / (b / 2) * y
    d3_a = d3_root + (d3_root * taper - d3_root) / (b / 2) * y
    d4_a = d4_root + (d4_root * taper - d4_root) / (b / 2) * y
    return d1_a, d2_a, d3_a, d4_a

def getSparHeight(spar_id, y):
    d1, d2, d3, d4 = Wingbox_lengths(wb.d_1, wb.d_2, wb.d_3, wb.d_4, wb.b, y)
    return d1

def criticalShear(k_s, E, poisson, t, b):
    tau_cr = np.pi**2 * k_s * E / (12 * (1 - poisson**2)) * (t/b)**2 
    return tau_cr

#insert a shear force value V (needs to be integrated from the distribution at a particular span y
def avgShear(V, y, h_1, h_2, h_3, t_1, t_2, t_3):
    #compute the shear force at a particular span y by integrating
    avg_shear = V/(h_1 * t_1 + h_2 * t_2 + h_3 * t_3)
    return avg_shear

tau_cr = criticalShear(wb.k_s1, wb.E, wb.poisson, wb.spar_t1, wb.spar_b1)

def get_ks(aspect_ratio):
    values = [15, 13.6, 12.8, 12.3, 11.9, 11.6, 11.35, 11, 10.8, 10.55, 10.35, 10.2, 10.1, 10, 9.9, 9.85, 9.8, 9.78, 9.76, 9.74, 9.73, 9.7, 9.68, 9.64, 9.62, 9.6, 9.58, 9.56, 9.54, 9.54, 9.54, 9.52, 9.52, 9.52, 9.52, 9.52, 9.52, 9.53, 9.53, 9.53, 9.53]
    
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

