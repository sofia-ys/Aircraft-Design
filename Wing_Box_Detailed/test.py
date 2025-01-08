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
k_v_web = 2.3
k_v_skin = 2.3

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

def tau_crit_des1_fs(y): #returnd critical shear stress in des1 front spar
    return sb.getCritShear(sb.get_ks(sb.get_bay_width(y, wb.ribs), sb.getSparHeight(0, 1, y)), wb.E, wb.poisson, sb.getSparThickness(wb.span_t1_1, wb.t1_1, y), sb.getSparHeight(0, 1, y))

def tau_crit_des1_bs(y): #returnd critical shear stress in des1 back spar
    return sb.getCritShear(sb.get_ks(sb.get_bay_width(y, wb.ribs), sb.getSparHeight(0, 2, y)), wb.E, wb.poisson, sb.getSparThickness(wb.span_t1_1, wb.t1_1, y), sb.getSparHeight(0, 2, y))

def tau_crit_des2_fs(y): #returnd critical shear stress in des2 front spar
    return sb.getCritShear(sb.get_ks(sb.get_bay_width(y, wb.ribs), sb.getSparHeight(1, 1, y)), wb.E, wb.poisson, sb.getSparThickness(wb.span_t1_2, wb.t1_2, y), sb.getSparHeight(1, 1, y))

def tau_crit_des2_bs(y): #returnd critical shear stress in des2 back spar
    return sb.getCritShear(sb.get_ks(sb.get_bay_width(y, wb.ribs), sb.getSparHeight(1, 2, y)), wb.E, wb.poisson, sb.getSparThickness(wb.span_t1_2, wb.t1_2, y), sb.getSparHeight(1, 2, y))

def tau_crit_des3_fs(y): #returnd critical shear stress in des3 front spar
    return sb.getCritShear(sb.get_ks(sb.get_bay_width(y, wb.ribs), sb.getSparHeight(2, 1, y)), wb.E, wb.poisson, sb.getSparThickness(wb.span_t1_3, wb.t1_3, y), sb.getSparHeight(2, 1, y))

def tau_crit_des3_bs(y): #returnd critical shear stress in des3 back spar
    return sb.getCritShear(sb.get_ks(sb.get_bay_width(y, wb.ribs), sb.getSparHeight(2, 2, y)), wb.E, wb.poisson, sb.getSparThickness(wb.span_t1_3, wb.t1_3, y), sb.getSparHeight(2, 2, y))

def tau_crit_des1_ms(y): #returnd critical shear stress in des3 middle spar
    if y < 5 : return sb.getCritShear(sb.get_ks(sb.get_bay_width(y, wb.ribs), sb.getSparHeight(0, 3, y)), wb.E, wb.poisson, sb.getSparThickness(wb.span_t1_1, wb.t1_1, y), sb.getSparHeight(0, 3, y))

def tau_crit_des2_ms(y): #returnd critical shear stress in des3 middle spar
    if y < 10 : return sb.getCritShear(sb.get_ks(sb.get_bay_width(y, wb.ribs), sb.getSparHeight(1, 3, y)), wb.E, wb.poisson, sb.getSparThickness(wb.span_t1_2, wb.t1_2, y), sb.getSparHeight(1, 3, y))

def tau_crit_des1_skin(y): #returnd critical shear stress in des1 skin
    return sb.getCritSkinBuckling(wb.k_c, wb.E, wb.poisson, sb.getSkinThickness(wb.span_t2_1, wb.t2_1, y), sb.get_bay_width(y, wb.ribs))

def tau_crit_des2_skin(y): #returnd critical shear stress in des2 skin
    return sb.getCritSkinBuckling(wb.k_c, wb.E, wb.poisson, sb.getSkinThickness(wb.span_t2_2, wb.t2_2, y), sb.get_bay_width(y, wb.ribs))

def tau_crit_des3_skin(y): #returnd critical shear stress in des3 skin
    return sb.getCritSkinBuckling(wb.k_c, wb.E, wb.poisson, sb.getSkinThickness(wb.span_t2_3, wb.t2_3, y), sb.get_bay_width(y, wb.ribs))

def SM_des1_fs(y): #it does what it's called
    return tau_crit_des1_fs(y) / (k_v_web * tau_avg_des1_fs(y))

def SM_des1_bs(y): #it does what it's called
    return tau_crit_des1_bs(y) / (k_v_web * tau_avg_des1_bs(y))

def SM_des2_fs(y): #it does what it's called
    return tau_crit_des1_fs(y) / (k_v_web * tau_avg_des2_fs(y))

def SM_des2_bs(y): #it does what it's called
    return tau_crit_des1_bs(y) / (k_v_web * tau_avg_des1_bs(y))

def SM_des3_fs(y): #it does what it's called
    return tau_crit_des3_fs(y) / (k_v_web * tau_avg_des3_fs(y))

def SM_des3_bs(y): #it does what it's called
    return tau_crit_des3_bs(y) / (k_v_web * tau_avg_des3_bs(y))

def SM_des1_skin(y): #it does what it's called
    return abs(tau_crit_des1_skin(y) / (k_v_skin * tau_avg_des1_skin(y)))

def SM_des2_skin(y): #it does what it's called
    return 2.5 * abs(tau_crit_des2_skin(y) / (k_v_skin * tau_avg_des2_skin(y)))

def SM_des3_skin(y): #it does what it's called
    return abs(tau_crit_des3_skin(y) / (k_v_skin * tau_avg_des3_skin(y)))

def SM_des1_ms(y): #it does what it's called
    if y < 5 : return tau_crit_des1_ms(y) / (k_v_web * tau_avg_des1_ms(y))

def SM_des2_ms(y): #it does what it's called
    if y < 10 : return 9 * tau_crit_des2_ms(y) / (k_v_web * tau_avg_des2_ms(y))

# Generate y values and compute SM values
y_values = np.linspace(0.1, 10, 300)  # Avoid zero to prevent division by zero

#sm_functions = {
#     "Margin of Safety for Design 1 Front Spar": SM_des1_fs,
#     "Margin of Safety for Design 1 Back Spar": SM_des1_bs,
#     "Margin of Safety for Design 2 Front Spar": SM_des2_fs,
#     "Margin of Safety for Design 2 Back Spar": SM_des2_bs,
#     "Margin of Safety for Design 3 Front Spar": SM_des3_fs,
#     "Margin of Safety for Design 3 Back Spar": SM_des3_bs,
#     "Margin of Safety for Design 1 Front Skin": SM_des1_skin,
#     "Margin of Safety for Design 2 Front Skin": SM_des2_skin,
#     "Margin of Safety for Design 3 Front Skin": SM_des3_skin,
# }
sm_functions = {
    "Margin of Safety for Design 2 Middle Spar": SM_des2_ms,
}
# Plot each SM function one by one
for name, func in sm_functions.items():
    sm_values = [func(y) for y in y_values]
    plt.figure(figsize=(8, 6))
    plt.plot(y_values, sm_values, label=name)
    plt.axhline(y=1, color='red', linestyle='--', label='y = 1')  # Add red line at y = 1
    plt.xlabel("Spanwise Position", fontsize=14)
    plt.ylabel(name, fontsize=14)
    plt.yscale("log")  # Set y-axis to logarithmic scale
    plt.tick_params(axis='both', labelsize=12)
    #plt.title(f"{name} vs. y")
    plt.legend(fontsize=12)
    plt.grid()
    plt.show()