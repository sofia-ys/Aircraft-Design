import numpy as np
import matplotlib.pyplot as plt
import wing_box_constants as wb
import shear_buckling as sb

# ---------------------------------------------------
# 1) Wingbox geometry parameters
# ---------------------------------------------------

b = 17.74         # Wing semi-span [m]
x_break = 5.0     # The middle spar disappears after y > 5 m (example)

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

def sum_ds_t_2_1(y) : #sum of ds/t in design 2 cell 2 
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

def q1_2(y) : #returns the shear flow in design 1 cell 1
    return solve_shear_flows_des2(y)[0]

def q2_2(y) : #returns the shear flow in design 1 cell 1
    return solve_shear_flows_des2(y)[1]

print(solve_shear_flows_des1(2)[1])