import sys
sys.path.append('Wing Structure')
sys.path.append('Wing_Box_Detailed')
import shear_bending_flight as sbf
import wing_box_constants as wb
import shear_buckling as sb
import numpy as np
import matplotlib.pyplot as plt
import Ixx

def getSparHeight(design_id, spar_id, y):
    """
    Returns the spar height (vertical dimension) at a spanwise location y
    for a given design (design_id) and spar (spar_id).
    
    :param design_id: 0, 1, or 2 (corresponding to Design #1, #2, #3)
    :param spar_id:   1 (front spar), 2 (rear spar), or 3 (middle spar)
    :param y:         spanwise station
    :return:          height of the specified spar at location y, in meters
    """
    # 'd' is a list of four dimension values for the wing box cross-section
    #   depending on the current y. The actual Ixx.Wingbox_lengths(...) function
    #   presumably interpolates or otherwise computes these distances along the span.
    d = Ixx.Wingbox_lengths(
        wb.all_spar_d[design_id][0],
        wb.all_spar_d[design_id][1],
        wb.all_spar_d[design_id][2],
        wb.all_spar_d[design_id][3],
        wb.b,
        y
    )
    
    if spar_id == 1:
        # Front spar height
        return d[0]  # dimension d1
    elif spar_id == 2:
        # Rear spar height
        return d[2]  # dimension d3
    elif spar_id == 3:
        # Middle spar
        if design_id == 0:
            # Design #1 => middle spar up to y=5 m
            if y > 5:
                return 0.0
            else:
                # Some geometry formula for middle spar height
                return (d[0] - d[3] / d[1] * (d[0] - d[2]))
        elif design_id == 1:
            # Design #2 => middle spar up to y=10 m
            if y > 10:
                return 0.0
            else:
                return (d[0] - d[3] / d[1] * (d[0] - d[2]))
        elif design_id == 2:
            # Design #3 => no middle spar
            return 0.0
    else:
        print("Error: invalid spar_id.")
        return 0.0

def getSparThickness(design_id, spar_id, span_t1, t1, y):
    """
    Returns the spar thickness at a spanwise station y for the specified
    spar_id (front=1, rear=2, middle=3) in a given design_id (0,1,2).
    
    If the middle spar (spar_id=3) is 'out of range' for that design,
    this function returns 0.0. Otherwise, it uses the piecewise logic
    to pick the correct thickness from span_t1 / t1 arrays.
    """
    # --- 1) Middle spar disappearance logic ---
    if spar_id == 3:
        # Design #1 => middle spar up to y=5 m
        if design_id == 0 and y > 5:
            return 0.0
        # Design #2 => middle spar up to y=10 m
        if design_id == 1 and y > 10:
            return 0.0
        # Design #3 => always no middle spar
        if design_id == 2:
            return 0.0

    # --- 2) Normal piecewise thickness logic ---
    # If we reach here, either we have spar_id in {1,2} 
    # or we are within the y-range for spar_id=3.
    for i in range(len(span_t1) - 1):
        if span_t1[i] <= y <= span_t1[i+1]:
            return t1[i]
        elif y >= span_t1[i+1]:
            # Keep going to the next segment
            pass
        else:
            break  # y is below the first breakpoint => thickness = t1[i] (already returned)

    # If y is beyond the last breakpoint, return the last thickness
    return t1[-1]

def V(y):
    return sbf.shear_force_vals[int(999 * float(y) / 17.74)]


def tau_avg_des1(y_value) :
    x = V(y_value) / (getSparHeight(0, 1, y_value) * getSparThickness(0, 1, wb.span_t1_1, wb.t1_1, y_value) + (getSparHeight(0, 2, y_value) * getSparThickness(0, 2, wb.span_t1_1, wb.t1_1, y_value) + (getSparHeight(0, 3, y_value) * getSparThickness(0, 3, wb.span_t1_1, wb.t1_1, y_value))))
    return x

def tau_avg_des2(y_value) :
    x = V(y_value) / (getSparHeight(1, 1, y_value) * getSparThickness(1, 1, wb.span_t1_2, wb.t1_2, y_value) + (getSparHeight(1, 2, y_value) * getSparThickness(1, 2, wb.span_t1_2, wb.t1_2, y_value) + (getSparHeight(1, 3, y_value) * getSparThickness(1, 3, wb.span_t1_2, wb.t1_2, y_value))))
    return x

def tau_avg_des3(y_value) :
    x = V(y_value) / (getSparHeight(2, 1, y_value) * getSparThickness(2, 1, wb.span_t1_3, wb.t1_3, y_value) + (getSparHeight(2, 2, y_value) * getSparThickness(2, 2, wb.span_t1_3, wb.t1_3, y_value) + (getSparHeight(2, 3, y_value) * getSparThickness(2, 3, wb.span_t1_3, wb.t1_3, y_value))))
    return x

# 2) Create a range of y-values from 0 to 17.74
y_values = np.linspace(0, 17.74, 1000)  # 200 points

# 3) Evaluate each tau function on that range
tau1 = [tau_avg_des1(y) for y in y_values]
tau2 = [tau_avg_des2(y) for y in y_values]
tau3 = [tau_avg_des3(y) for y in y_values]

# 4) Plot all three designs on the same figure
plt.figure(figsize=(8,6))
plt.plot(y_values, tau1, label='Design #1')
plt.plot(y_values, tau2, label='Design #2')
plt.plot(y_values, tau3, label='Design #3')
plt.xlabel('Spanwise location, y (m)')
plt.ylabel('Average shear stress, τ (Pa)')
plt.title('Shear Stress vs. Spanwise Location for Three Designs')
plt.legend()
plt.grid(True)
plt.show()