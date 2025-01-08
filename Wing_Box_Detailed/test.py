import numpy as np
import matplotlib.pyplot as plt
import wing_box_constants as wb
import shear_buckling as sb
import avg_shear2 as as2
# ---------------------------------------------------
# 1) Wingbox geometry parameters
# ---------------------------------------------------

b = 17.74         # Wing semi-span [m]
x_break = 5.0     # The middle spar disappears after y > 5 m (example)
k_v = 1

def get_chord(y):
    return 5.918 - (y / 17.74) * 4.4659

des1 = [0.2028, 0.2335] #1st number is distance between front and multibox spars
des2 = [0.2028, 0.347]  #2nd is distance between back and multibox, in x/c


def A1_1(y) : #A1 for des1 in m^2
    return (sb.getSparHeight(0, 1, y) + sb.getSparHeight(0, 3, y)) * get_chord(y) * 0.2028 / 2

def A2_1(y) : #A2 for des1 in m^2
    return (sb.getSparHeight(0, 2, y) + sb.getSparHeight(0, 3, y)) * get_chord(y) * 0.2335 / 2

def A1_2(y) : #A1 for des2 in m^2
    return (sb.getSparHeight(1, 1, y) + sb.getSparHeight(1, 3, y)) * get_chord(y) * 0.2028 / 2

def A2_2(y) : #A2 for des2 in m^2
    return (sb.getSparHeight(1, 2, y) + sb.getSparHeight(1, 3, y)) * get_chord(y) * 0.347 / 2

def t_skin_1(y) : #in m
    return sb.getSkinThickness(wb.span_t2_1, wb.t2_1, y)

def t_skin_2(y) : #in m
    return sb.getSkinThickness(wb.span_t2_2, wb.t2_2, y)

def T(y): #in Nm
    return wb.torque_06_deg[int(999 * float(y) / 17.74)] * 1000

def sum_ds_t_1_1(y) : #sum of ds/t in design 1 cell 1 
    return (sb.getSparHeight(0, 1, y) + sb.getSparHeight(0, 3, y)) / sb.getSkinThickness(wb.span_t1_1, wb.t1_1, y) + 2 * get_chord(y) * 0.2028 / t_skin_1(y)

def sum_ds_t_1_2(y) : #sum of ds/t in design 1 cell 2 
    return (sb.getSparHeight(0, 2, y) + sb.getSparHeight(0, 3, y)) / sb.getSkinThickness(wb.span_t1_1, wb.t1_1, y) + 2 * get_chord(y) * 0.2335 / t_skin_1(y)

def sum_ds_t_2_1(y) : #sum of ds/t in design 2 cell 1 
    return (sb.getSparHeight(1, 1, y) + sb.getSparHeight(1, 3, y)) / sb.getSkinThickness(wb.span_t1_2, wb.t1_2, y) + 2 * get_chord(y) * 0.2028 / t_skin_2(y)

def sum_ds_t_2_2(y) : #sum of ds/t in design 2 cell 2 
    return (sb.getSparHeight(1, 2, y) + sb.getSparHeight(1, 3, y)) / sb.getSkinThickness(wb.span_t1_2, wb.t1_2, y) + 2 * get_chord(y) * 0.347 / t_skin_2(y)

def solve_shear_flows_des1(y):
 
    if abs(sum_ds_t_1_2(y)) < 1.0e-12:
        # Avoid divide by zero if geometry is degenerate
        return 0.0, 0.0
    
    factor = sum_ds_t_1_1(y) / sum_ds_t_1_2(y)
    denom = 2.0 * (A1_1(y) + factor * A2_1(y))
    
    if abs(denom) < 1.0e-20:
        return 0.0, 0.0
    
    q1 = T(y) / denom
    q2 = factor * q1
    
    return q1, q2

def solve_shear_flows_des2(y):
 
    if abs(sum_ds_t_2_2(y)) < 1.0e-12:
        # Avoid divide by zero if geometry is degenerate
        return 0.0, 0.0
    
    factor = sum_ds_t_2_1(y) / sum_ds_t_2_2(y)
    denom = 2.0 * (A1_2(y) + factor * A2_2(y))
    
    if abs(denom) < 1.0e-20:
        return 0.0, 0.0
    
    q1 = T(y) / denom
    q2 = factor * q1
    
    return q1, q2

def q1_1(y) : #returns the shear flow in design 1 cell 1
    return solve_shear_flows_des1(y)[0]

def q2_1(y) : #returns the shear flow in design 1 cell 2
    return solve_shear_flows_des1(y)[1]

def q1_2(y) : #returns the shear flow in design 2 cell 1
    return solve_shear_flows_des2(y)[0]

def q2_2(y) : #returns the shear flow in design 2 cell 1
    return solve_shear_flows_des2(y)[1]

def Q1(y) : #shear flow in design 1 when single cell
    return T(y) / (2 * (sb.getSparHeight(0, 1, y) + sb.getSparHeight(0, 2, y)) * get_chord(y) * 0.4363 / 2)

def Q2(y) : #shear flow in design 2 when single cell
    return T(y) / (2 * (sb.getSparHeight(1, 1, y) + sb.getSparHeight(1, 2, y)) * get_chord(y) * 0.55 / 2)

def Q3(y) : #shear flow in design 3 
    return T(y) / (2 * (sb.getSparHeight(2, 1, y) + sb.getSparHeight(2, 2, y)) * get_chord(y) * 0.4294 / 2)

def tau_avg_des1_fs(y): #avg shear stress in des1 front spar
    if y < 5 :
        return as2.tau_avg_des1(y) - (q1_1(y) / sb.getSparThickness(wb.span_t1_1, wb.t1_1, y))
    else : return as2.tau_avg_des1(y) - (Q1(y) / sb.getSparThickness(wb.span_t1_1, wb.t1_1, y))

def tau_avg_des1_bs(y): #avg shear stress in des1 back spar
    if y < 5 :
        return as2.tau_avg_des1(y) + (q2_1(y) / sb.getSparThickness(wb.span_t1_1, wb.t1_1, y))
    else : return as2.tau_avg_des1(y) + (Q1(y) / sb.getSparThickness(wb.span_t1_1, wb.t1_1, y))

def tau_avg_des2_fs(y): #avg shear stress in des2 front spar
    if y < 10 :
        return as2.tau_avg_des2(y) - (q1_2(y) / sb.getSparThickness(wb.span_t1_2, wb.t1_2, y))
    else : return as2.tau_avg_des2(y) - (Q2(y) / sb.getSparThickness(wb.span_t1_2, wb.t1_2, y))

def tau_avg_des2_bs(y): #avg shear stress in des2 back spar
    if y < 10 :
        return as2.tau_avg_des2(y) + (q2_2(y) / sb.getSparThickness(wb.span_t1_2, wb.t1_2, y))
    else : return as2.tau_avg_des2(y) + (Q2(y) / sb.getSparThickness(wb.span_t1_2, wb.t1_2, y))

def tau_avg_des3_fs(y): #avg shear stress in des3 front spar
    return as2.tau_avg_des3(y) - (Q3(y) / sb.getSparThickness(wb.span_t1_3, wb.t1_3, y))

def tau_avg_des3_bs(y): #avg shear stress in des3 back spar
    return as2.tau_avg_des3(y) + (Q3(y) / sb.getSparThickness(wb.span_t1_3, wb.t1_3, y))

def tau_avg_des1_ms(y): #avg shear stress in des1 middle spar
    if y < 5 :
        return as2.tau_avg_des1(y) + ((q1_1(y) - q2_1(y)) / sb.getSparThickness(wb.span_t1_1, wb.t1_1, y))

def tau_avg_des2_ms(y): #avg shear stress in des2 middle spar
    if y < 10 :
        return as2.tau_avg_des2(y) + ((q1_2(y) - q2_2(y)) / sb.getSparThickness(wb.span_t1_1, wb.t1_1, y))

def tau_avg_des1_skin(y): #returns the max skin shear due to torsion in des1
    if y < 5:
        return max(q1_1(y)/sb.getSkinThickness(wb.span_t2_1, wb.t2_1, y) , q2_1(y)/sb.getSkinThickness(wb.span_t2_1, wb.t2_1, y))
    else : return Q1(y) / sb.getSkinThickness(wb.span_t2_1, wb.t2_1, y)

def tau_avg_des2_skin(y): #returns the max skin shear due to torsion in des2
    if y < 10:
        return max(q1_2(y)/sb.getSkinThickness(wb.span_t2_2, wb.t2_2, y) , q2_2(y)/sb.getSkinThickness(wb.span_t2_2, wb.t2_2, y))
    else : return Q2(y) / sb.getSkinThickness(wb.span_t2_2, wb.t2_2, y)

def tau_avg_des3_skin(y): #returns the max skin shear due to torsion in des1
    return Q3(y) / sb.getSkinThickness(wb.span_t2_3, wb.t2_3, y)

def main():
    # Define the y-range for plotting (adjust as needed).
    # For example: from y=0 up to 17.74 with 200 points:
    y_start, y_end = 0.0, 17.74
    n_points       = 200
    ys = np.linspace(y_start, y_end, n_points)

    # Evaluate each function at all y-points
    tau1_fs_vals = [tau_avg_des1_fs(y) for y in ys]  # design 1 front spar
    tau1_bs_vals = [tau_avg_des1_bs(y) for y in ys]  # design 1 back spar

    tau2_fs_vals = [tau_avg_des2_fs(y) for y in ys]  # design 2 front spar
    tau2_bs_vals = [tau_avg_des2_bs(y) for y in ys]  # design 2 back spar

    tau3_fs_vals = [tau_avg_des3_fs(y) for y in ys]  # design 3 front spar
    tau3_bs_vals = [tau_avg_des3_bs(y) for y in ys]  # design 3 back spar

    # Plot all on one figure
    plt.figure(figsize=(9,6))

    plt.plot(ys, tau1_fs_vals, label='Design 1: Front Spar', linewidth=2)
    plt.plot(ys, tau1_bs_vals, label='Design 1: Back Spar', linewidth=2)

    plt.plot(ys, tau2_fs_vals, label='Design 2: Front Spar', linewidth=2)
    plt.plot(ys, tau2_bs_vals, label='Design 2: Back Spar', linewidth=2)

    plt.plot(ys, tau3_fs_vals, label='Design 3: Front Spar', linewidth=2)
    plt.plot(ys, tau3_bs_vals, label='Design 3: Back Spar', linewidth=2)

    plt.xlabel('Spanwise Station, y [m]')
    plt.ylabel('Shear Stress [Pa]')  # or [N/m^2], depending on your units
    plt.title('Shear Stress vs. Span for Designs 1, 2, and 3')
    plt.grid(True)
    plt.legend()
    plt.show()

# Generate y values and compute shear values
y_values = np.linspace(0, 17.74, 100)
tau_des1 = [tau_avg_des1_skin(y) for y in y_values]
tau_des2 = [tau_avg_des2_skin(y) for y in y_values]
tau_des3 = [tau_avg_des3_skin(y) for y in y_values]

# Plot the results
plt.figure(figsize=(10, 6))
plt.plot(y_values, tau_des1, label="tau_avg_des1_skin")
plt.plot(y_values, tau_des2, label="tau_avg_des2_skin")
plt.plot(y_values, tau_des3, label="tau_avg_des3_skin")
plt.xlabel("y")
plt.ylabel("Tau (Skin Shear)")
plt.title("Skin Shear Due to Torsion vs. y")
plt.legend()
plt.grid()
plt.show()

if __name__ == "__main__":
    main()