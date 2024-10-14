from Drag import *
import math as m

b = 41
b_ref = 1.905
sweep_half = Sweep_quater
n_ult = 1.5*2.5
kw = 6.67e-3
b_s = b/(m.cos(sweep_half))
t_r = Chord_root*t_c
ZFW = 130000


Wing_mass = (kw * (b_s ** 0.75)) * (1 + m.sqrt(b_ref / b_s) * (n_ult ** 0.55) * ((b_s / t_r) / (ZFW / S_wing)) ** 0.30) * ZFW
print(Wing_mass)



# VARIABLES
A_h = 1 # AR horizontal tail
N_f = 5  # Number of flight control systems
N_m = 1 # Number of mechanical functions
N_fy = 1  # Number of hydraulic utility functions
S_cs = 1  # Total area of control surfaces, ft^2
I_y = 1  # Yawing moment of inertia, lb-ft^2
W_APU_uninstalled = 1  # Weight of uninstalled APU
K_r = 1  # System reliability factor
K_tp = 1  # Mission completion factor
N_c = 1  # Number of crew
N_en = 1  # Number of engines
L_f = 1  # Total fuselage length, ft
B_w = 1  # Wing span, ft
R_kva = 1  # System electrical rating, kv*A
L_a = 1  # Electrical routing distance, generators to avionics to cockpit, ft
N_gen = 1  # Number of generators
W_uav = 1  # Uninstalled avionics weight, lb
N_c = 1  # Number of crew
W_c = 1  # Maximum cargo weight, lb
S_f = 1  # Fuselage wetted area, ft^2
N_p = 1  # Number of personnel onboard (crew and passengers)
V_pr = 1  # Volume of pressurized section, ft^3
W_dg = 1  # Design gross weight, lb
W_eci = 1  # Weight of engine and contents, lb
W_i = 1  # Installed weight, lb
V_t = 1  # Total fuel volume, gal
V_i = 1  # Integral tanks volume, gal
V_p = 1  # Self-sealing "protected" tanks volume, gal
N_i = 1  # Ultimate landing load factor
L_m = 1  # Length of main landing gear, in
L_n = 1  # Nose gear length, in
N_mw = 1  # Number of main wheels
N_mss = 1  # Number of main gear shock struts
L_t = 1  # Tail length, ft
S_vt = 1  # Vertical tail area, ft^2
A_v = 1  # Aspect ratio of vertical tail
A = 1  # Aspect ratio
S_w = 1  # Trapezoidal wing area, ft^2
(t_c)_root = 1  # Thickness to chord ratio at the root
lambda_w = 1  # Wing taper ratio
S_csw = 1  # surface area (wing-mounted), ft^2
K_uht = 1  # Horizontal tail unit factor
F_w = 1  # Fuselage width at horizontal tail intersection, ft
B_h = 1  # Horizontal tail span, ft
N_z = 1  # Ultimate load factor
S_ht = 1  # Horizontal tail area, ft^2
K_y = 1  # Vertical tail height above fuselage, ft
H_t = 1  # Horizontal tail height above fuselage, ft
H_v = 1  # Vertical tail height above fuselage, ft
L_sh = 1  # Length of engine shroud, ft
W_en = 1  # Engine weight, lb
N_Lt = 1  # Nacelle length, ft
W_fw = 1  # Weight of fuel in wing, lb
K_door = 1  # Cargo door factor
K_ws = 1  # Wing sweep factor
L_D = 1  # Lift to drag ratio
K_mp = 1  # Main landing gear positioning factor
V_stall = 1  # Stall velocity, knots
K_np = 1  # Nose landing gear positioning factor
K_ng = 1  # Nacelle group factor
K_ent = 1  # Includes air induction
L_ec = 1  # Length from engine front to cockpit, ft
N_en = 1  # Number of engines
K_ng = 1  # Pylon-mounted nacelle factor
K_htt = 1  # Horizontal tail height above fuselage factor
K_ah = 1  # Horizontal tail area factor
A_h = 1  # Horizontal tail aspect ratio
S_e = 1  # Elevator area, ft^2
K_z = 1  # Vertical tail height above fuselage factor
K_inp = 1  # Main landing gear positioning factor
N_i = 1  # Ultimate landing load factor
N_nw = 1  # Number of nose wheels
S_n = 1  # Nacelle wetted area, ft^2
W_ec = 1  # Engine and contents weight per nacelle, lb
S_cargo_floor  = 1

# EQUATIONS
W_flight_controls = 145.9 * N_f ** 0.554 * (1 + N_m / N_f) ** -1.0 * S_cs ** 0.20 * (I_y * 10 ** -6) ** 0.07
W_APU_installed = 2.2 * W_APU_uninstalled
W_instruments = 4.509 * K_r * K_tp * N_c ** 0.541 * N_en * (L_f + B_w) ** 0.5
W_hydraulics = 0.2673 * N_f * (L_f + B_w) ** 0.937
W_electrical = 7.291 * R_kva ** 0.782 * L_a ** 0.346 * N_gen ** 0.10
W_avionics = 1.73 * W_uav ** 0.983
W_furnishings = 0.0577 * N_c ** 0.1 * W_c ** 0.393 * S_f ** 0.75
W_air_conditioning = 62.36 * N_p ** 0.25 * (V_pr / 1000) ** 0.604 * W_uav ** 0.10
W_anti_ice = 0.002 * W_dg
W_handling_gear = 3.0e-4 * W_dg
W_military_cargo_handling = 2.4 * (S_cargo_floor)  # Cargo floor area assumed as 1 ft^2
W_wing = 0.0051 * (W_dg * N_z) ** 0.557 * S_w ** 0.649 * A ** 0.5 * (t_c)_root ** -0.4 * (1 + lambda_w) ** 0.1 * (m.cos(Sweep_quater)) ** -1.0 * S_csw ** 0.1
W_horizontal_tail = 0.0379 * K_uht * (1 + F_w / B_h) ** -0.25 * W_dg ** 0.639 * N_z ** 0.10 * S_ht ** 0.75 * L_t ** -1.0 * K_y ** 0.704 * (m.cos(A_h))) ** -1.0 * A_h ** 0.166 * (1 + S_e / S_ht) ** 0.1
W_vertical_tail = 0.0026 * (1 + H_t / H_v) ** 0.225 * W_dg ** 0.556 * L_t ** 0.536 * S_vt ** 0.5 * K_z ** 0.875 * (m.cos(A_v)) * A_v ** 0.35 * (t_c)_root ** -0.5
W_fuselage = 0.3280 * K_door * K_y * (W_dg * N_z) ** 0.5 * L_f ** 0.25 * S_f ** 0.302 * (1 + K_ws) ** 0.04 * (L_D) ** 0.10
W_main_landing_gear = 0.0106 * K_mp * W_i ** 0.888 * N_i ** 0.25 * L_m ** 0.4 * N_mw ** 0.321 * N_mss ** 0.5 * V_stall ** 0.1
W_nose_landing_gear = 0.032 * K_np * W_i ** 0.646 * N_i ** 0.2 * L_n ** 0.5 * N_nw ** 0.45
W_nacelle_group = 0.6724 * K_ng * N_Lt ** 0.10 * N_z ** 0.294 * N_w ** 0.119 * W_ec ** 0.611 * N_en ** 0.984 * S_n ** 0.224
W_engine_controls = 5.0 * N_en + 0.80 * L_ec
W_starter_pneumatic = 49.19 * (N_en * W_en / 1000) ** 0.541
W_fuel_system = 2.405 * V_t ** 0.606 * (1 + V_i / V_t) ** -1.0 * (1 + V_p / V_t) * N_i ** 0.5

# More equations could be implemented similarly based on the available terminology and equations.