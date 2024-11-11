import math as mt

#Change these depending on airfoil
alpha_0 = -3.68  # deg
Cl_max = 2.2

# other constant numbers
MTOW = 117604 # kg
OEW = 58876 #kg
W_Fuel = 8832 #kg
b = 38  #m
S = 174.8 #m^2
QC_sweep = 30.7678336 #deg
tr = 0.292
V_app = 79.827 #m/s
h_app =	0 #m
V_cr=256.47	 #m/s
h_cr= 9448.8	 #m
t_to_c= 0.12
rho_cr =0.44
n = 0.95
SL_sound = 343 #m/s

root_chord = 7.08
tip_chord = root_chord*tr

#Variables
Mach_approach = V_app/SL_sound
AR = b**2/S #
Beta_approach = mt.sqrt(1 - Mach_approach**2)
Lambda_0_5C = mt.radians(QC_sweep)


#Clean wing configuration linear part
dCL_dalpha_clean = (2 * mt.pi * AR) / (2 + mt.sqrt(4 + (AR * Beta_approach / n)*2 * (1 + mt.tan(Lambda_0_5C)*2)))

#Clean wing configuration curved part
Delta_alpha_Clmax = 2.2 #update
delta_y = 1.5
CLmax_to_Clmax = 0.9 #from scuffed adsee graph
delta_CL_max = 0 #update
CL_max = CLmax_to_Clmax * Cl_max + delta_CL_max

alpha_stall = (CL_max/dCL_dalpha_clean)+ mt.radians(alpha_0) + mt.radians(Delta_alpha_Clmax) # in rad

print(f'Gradient of clean config curve is {dCL_dalpha_clean}')
print(f'Alpha_stall for clean config is {alpha_stall}')
print(f'CL_max for clean config is {CL_max}')
