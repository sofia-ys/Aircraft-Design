import math as m


#INPUTS
S_ref = 173.54
S_wing = 173.5 
S_htail = 1 ####################################################
S_vtail = 1 ####################################################
L1 = 8.561    
L2 = 18.787   
L3 = 9.305   

taper_ratio = 0.2453387369561506
Chord_root = 6.797418854384913
k_surface = (0.3*0.152 + 0.7*0.634)*10**-5

upsweep_fus = 0.1047197551
A_max_fus = (3.722/2)**2*m.pi   ##############################################
A_base = 116       


x_c_m = 0.35
t_c = 0.1096
Sweep_quater = 0.537
l_fus = 36.653
d_fus = 3.722
l_nacc = 1 #####################################################
d_nacc = 1 #####################################################



V = 256
M = 0.85
M_dd = 0.89
#ATMOSPHERE
dynamic_visc = 3.355 * 10**-5
rho  = 1.225 * 0.3589

kinematic_visc = dynamic_visc*rho



#CALCULATIONS
Re = 36249291
MAC = C_MGC = (2 / 3) * Chord_root * ((1 + taper_ratio + taper_ratio**2) / (1 + taper_ratio))

#S_WET
S_wet_wing = 1.07*2*S_wing
S_wet_htail = 1.05*2*S_htail
S_wet_vtail = 1.05*2*S_vtail
S_wet_fus = (m.pi * d_fus / 4) * ((1 / (3 * L1**2)) * ((4 * L1**2 + (d_fus**2 / 4)) ** 1.5 - (d_fus**3 / 8)) - d_fus + 4 * L2 + 2 * m.sqrt(L3**2 + (d_fus**2 / 4)))


#CF_C
Fus_lam_frac = 0.05
Wing_lam_frac = 0.10
Re_trans = min( (rho*V*MAC)/(kinematic_visc), (44.62*(MAC/k_surface)**1.053)*M**1.16 )
C_f_lam = (1.382)/(m.sqrt(Re_trans))
C_f_turb = (0.455)/((m.log10(Re_trans))**2.58*(1+0.144*M**2)*0.65)



C_F_wing = Wing_lam_frac*C_f_lam + (1-Wing_lam_frac)*C_f_turb
C_F_fus = Fus_lam_frac*C_f_lam + (1-Fus_lam_frac)*C_f_turb


#FF_C
FF_wing = (1 + (0.6/x_c_m) * (t_c) + 100*(t_c)** 4) * (1.34*M**0.18 * (m.cos(Sweep_quater))**0.28)
f_fus = l_fus / d_fus
FF_fus = 1 + (60 / f_fus ** 3) + (f_fus / 400)
f_nacc = l_nacc * d_nacc
FF_nacc = 1 + (0.35 / f_nacc)


#IF_C
IF_wing = 1 ####################################################
IF_fus = 1  ####################################################
IF_nacc = 1 ####################################################
IF_tail = 1 ####################################################

Wave_drag =  0.002*(1+2.5*(M_dd-M)/(0.05))**(-1)
Fus_upsweep_drag = 3.83*upsweep_fus**2.5*A_max_fus * (0.5*rho*V**2)
Fus_base_drag = (0.139+0.419*(M-0.161)**2)*A_base * (0.5*rho*V**2)

Lanfing_gear_drag = 0 ########################################## SLIDE 57
Excrescence_and_leakage_drag = 1.035

D_misc = Fus_upsweep_drag + Fus_base_drag

CD_0 = ((1/S_ref)*((C_F_fus * FF_fus * IF_fus * S_wet_fus) + (C_F_wing * FF_wing * IF_wing * S_wet_wing))) * Excrescence_and_leakage_drag

CL=0.43
AR = 9.7
A = 10
Sweep_LE = 0.5871613666551182-0.0053
e = 4.61*(1-0.045*AR**0.68)*(m.cos(Sweep_LE)**0.15)-3.1
twist_tip = 3 ################################
twist_MGC = 1 ################################
twist_drag = 0.00004*(twist_tip-twist_MGC)

AR_effective = 0 #############################

CD = CD_0 + (CL**2)/(m.pi*A*e) + twist_drag