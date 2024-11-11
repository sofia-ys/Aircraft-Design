from Drag import *
import math as m

b = 41
b_ref = 1.905   
sweep_half = Sweep_quater
n_ult = 1.5*2.5
kw = 6.67e-3
b_s = b/(m.cos(sweep_half))
t_r = Chord_root*t_c
ZFW = 90000


Wing_mass = (kw * (b_s ** 0.75)) * (1 + m.sqrt(b_ref / b_s) * (n_ult ** 0.55) * ((b_s / t_r) / (ZFW / S_wing)) ** 0.30) * ZFW

print(Wing_mass)


# VARIABLES
A_h = 4 # AR horizontal tail 
N_f = 7  # Number of flight control systems 
N_m = 0 # Number of mechanical functions 
N_fy = 15  # Number of hydraulic utility functions 
S_cs = 84+313  # Total area of control surfaces, ft^2 
I_y = 90000000  # Yawing moment of inertia, lb-ft^2 
W_APU_uninstalled = 164  # Weight of uninstalled APU, lbs
K_r = 1  # System reliability factor
K_tp = 1  # Mission completion factor
N_c = 3  # Number of crew
N_en = 2  # Number of engines
L_f = 120.5  # Total fuselage length, ft
B_w = 134.8  # Wing span, ft
R_kva = 180  # System electrical rating, kv*A 
L_a = 50/0.3048  # Electrical routing distance, generators to avionics to cockpit, ft 
N_gen = 2  # Number of generators
W_uav = 1800  # Uninstalled avionics weight, lb
W_c = 18960*2.2  # Maximum cargo weight, lb  
S_f = 367/(0.3048**2)  # Fuselage wetted area, ft^2
N_p = 140  # Number of personnel onboard (crew and passengers)
V_pr = 313.6/(0.3040**3)  # Volume of pressurized section, ft^3
W_dg = 137969.42042373677*2.2  # Design gross weight, lb: previously 113000
W_i = 1400  # Installed weight, lb
V_t = 56*264  # Total fuel volume, gal
V_i = 56*264  # Integral tanks volume, gal
N_i = 2.5  # Ultimate landing load factor
L_m = 100  # Length of main landing gear, in 
L_n = 83  # Nose gear length, in 
N_mw = 4  # Number of main wheels 
N_mss = 2  # Number of main gear shock struts 
L_t = 49.5  # Tail length, ft 
S_vt = 463  # Vertical tail area, ft^2 
A_v = 1.6  # Aspect ratio of vertical tail
Sweep_vt = 0.08
A = 9.7  # Aspect ratio
S_w = S_wing/0.3048  # Trapezoidal wing area, ft^2
t_c = 0.104 # Thickness to chord ratio at the root
lambda_w = 0.2453387369561506  # Wing taper ratio
S_csw = 81.4+131  # Control surface area (wing-mounted), ft^2
K_uht = 1  # Horizontal tail unit factor  
F_w = 7  # Fuselage width at horizontal tail intersection, ft
B_h = 49  # Horizontal tail span, ft 
N_z = 1.5*2.5  # Ultimate load factor
S_ht = 194  # Horizontal tail area, ft^2 
K_y = 27     # Vaircraft pitching radius of gyration, ft ( 0.3Lt)
H_t = 0  # Horizontal tail height above fuselage, ft 
H_v = 1  # Vertical tail height above fuselage, ft 
W_en = 3008*2.2  # Engine weight, lb
N_Lt = 4.1/0.3048  # Nacelle length, ft
W_fw = 27438*2.2  # Weight of fuel in wing, lb
K_door = 1.12 # Cargo door factor 
K_ws = 0.75*((1 + 2*lambda_w)/(1+lambda_w))*(b * m.tan(Sweep_quater/((l_fus-1)/0.3048))) # Wing sweep factor
L_D = 15.8  # Lift to drag ratio
K_mp = 1.126  # Main landing gear positioning factor
V_stall = 132  # Stall velocity, knots 
K_np = 1.15  # Nose landing gear positioning factor
K_ng = 1.017  # Nacelle group factor
L_ec = 15/0.3048  # Length from engine front to cockpit, ft
N_en = 2  # Number of engines
S_e = 128  # Elevator area, ft^2 
K_z = 49.2  # Fuselage yawing radius of gyration factor 
N_nw = 2  # Number of nose wheels 
S_n = 82  # Nacelle wetted area, ft^2 
N_w = 5.9 #Nacelle width, ft 
W_ec = 3008*2*2.2
V_p = 0 #Self-sealing tanks volume, ft^3
Sweep_ht = 0.1357478307
K_lg = 1 #Landing gear
W_seat = 50 #lbs
W_food = 2.5 #lbs per passanger
W_cart = 308 #lbs
N_carts = 3

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
W_wing = 0.0051 * (W_dg * N_z) ** 0.557 * S_w ** 0.649 * A ** 0.5 * t_c ** (-0.4) * (1 + lambda_w) ** 0.1 * (m.cos(Sweep_quater)) ** (-1.0) * S_csw ** 0.1
W_horizontal_tail = 0.0379 * K_uht * (1 + F_w / B_h) ** (-0.25) * W_dg ** 0.639 * N_z ** 0.10 * S_ht ** 0.75 * L_t ** (-1.0) * K_y ** 0.704 * (m.cos(Sweep_ht)) ** (-1.0) * A_h ** 0.166 * (1 + S_e / S_ht) ** 0.1
W_vertical_tail = 0.0026 * (1 + H_t / H_v) ** 0.225 * W_dg ** 0.556 * N_z ** 0.536 * L_t ** -0.5 * S_vt ** 0.5 * K_z ** 0.875 * (m.cos(Sweep_vt)) * A_v ** 0.35 * t_c ** -0.5
W_fuselage = 0.3280 * K_door * K_lg * (W_dg * N_z) ** 0.5 * L_f ** 0.25 * S_f ** 0.302 * (1 + K_ws) ** 0.04 * L_D ** 0.10
W_main_landing_gear = 0.0106 * K_mp * W_i ** 0.888 * N_i ** 0.25 * L_m ** 0.4 * N_mw ** 0.321 * N_mss ** -0.5 * V_stall ** 0.1 + W_i * 0.7
W_nose_landing_gear = 0.032 * K_np * W_i ** 0.646 * N_i ** 0.2 * L_n ** 0.5 * N_nw ** 0.45 + W_i * 0.3
W_nacelle_group = 0.6724 * K_ng * N_Lt ** 0.10 * N_z ** 0.294 * N_w ** 0.119 * W_ec ** 0.611 * N_en ** 0.984 * S_n ** 0.224
W_engine_controls = 5.0 * N_en + 0.80 * L_ec
W_starter_pneumatic = 49.19 * (N_en * W_en / 1000) ** 0.541
W_fuel_system = 2.405 * V_t ** 0.606 * (1 + V_i / V_t) ** -1.0 * (1 + V_p / V_t) * N_i ** 0.5
W_eci = 3008*2*2.2  # Weight of engine and contents, lb
W_seats = N_p * W_seat
W_food = N_carts * W_cart + W_food * N_p

W_total = (
    W_flight_controls + W_APU_installed + W_instruments + W_hydraulics + W_electrical + W_avionics + W_furnishings + W_air_conditioning + W_anti_ice + W_handling_gear + W_wing + W_horizontal_tail + 
    W_vertical_tail + W_fuselage +  W_main_landing_gear +  W_nose_landing_gear +  W_nacelle_group +  W_engine_controls +  W_starter_pneumatic + W_fuel_system + W_eci + W_fw + W_c + W_seats + W_food
)



print("W_flight_controls = ", W_flight_controls)
print("W_APU_installed = ", W_APU_installed)
print("W_instruments = ", W_instruments)
print("W_hydraulics = ", W_hydraulics)
print("W_electrical = ", W_electrical)
print("W_avionics = ", W_avionics)
print("W_furnishings = ", W_furnishings)
print("W_air_conditioning = ", W_air_conditioning)
print("W_anti_ice = ", W_anti_ice)
print("W_handling_gear = ", W_handling_gear)
print("W_wing = ", W_wing)
print("W_horizontal_tail = ", W_horizontal_tail)
print("W_vertical_tail = ", W_vertical_tail)
print("W_fuselage = ", W_fuselage)
print("W_main_landing_gear = ", W_main_landing_gear)
print("W_nose_landing_gear = ", W_nose_landing_gear)
print("W_nacelle_group = ", W_nacelle_group)
print("W_engine_controls = ", W_engine_controls)
print("W_starter_pneumatic = ", W_starter_pneumatic)
print("W_fuel_system = ", W_fuel_system)
print("W_eci = ", W_eci)
print("W_payload =", W_c)
print("W_seats =", W_seats)
print("W_food =", W_food)

print("Total Weight (W_total) = ", W_total/2.2, "\n\n\n")


print("W_flight_controls = {:.2f}%".format((W_flight_controls / W_total) * 100))
print("W_APU_installed = {:.2f}%".format((W_APU_installed / W_total) * 100))
print("W_instruments = {:.2f}%".format((W_instruments / W_total) * 100))
print("W_hydraulics = {:.2f}%".format((W_hydraulics / W_total) * 100))
print("W_electrical = {:.2f}%".format((W_electrical / W_total) * 100))
print("W_avionics = {:.2f}%".format((W_avionics / W_total) * 100))
print("W_furnishings = {:.2f}%".format((W_furnishings / W_total) * 100))
print("W_air_conditioning = {:.2f}%".format((W_air_conditioning / W_total) * 100))
print("W_anti_ice = {:.2f}%".format((W_anti_ice / W_total) * 100))
print("W_handling_gear = {:.2f}%".format((W_handling_gear / W_total) * 100))
print("W_wing = {:.2f}%".format((W_wing / W_total) * 100))
print("W_horizontal_tail = {:.2f}%".format((W_horizontal_tail / W_total) * 100))
print("W_vertical_tail = {:.2f}%".format((W_vertical_tail / W_total) * 100))
print("W_fuselage = {:.2f}%".format((W_fuselage / W_total) * 100))
print("W_main_landing_gear = {:.2f}%".format((W_main_landing_gear / W_total) * 100))
print("W_nose_landing_gear = {:.2f}%".format((W_nose_landing_gear / W_total) * 100))
print("W_nacelle_group = {:.2f}%".format((W_nacelle_group / W_total) * 100))
print("W_engine_controls = {:.2f}%".format((W_engine_controls / W_total) * 100))
print("W_starter_pneumatic = {:.2f}%".format((W_starter_pneumatic / W_total) * 100))
print("W_fuel_system = {:.2f}%".format((W_fuel_system / W_total) * 100))
print("W_eci = {:.2f}%".format((W_eci / W_total) * 100))
print("W_fuel = {:.2f}%".format((W_fw / W_total) * 100))
print("W_payload = {:.2f}%".format((W_c / W_total) * 100))
print("W_seats = {:.2f}%".format((W_seats / W_total) * 100))
print("W_food = {:.2f}%".format((W_food / W_total) * 100))
print("Total Weight (W_total) = {:.2f}".format((W_total / 2.2)))  # This will always be 100%