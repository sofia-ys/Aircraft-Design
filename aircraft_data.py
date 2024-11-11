import reference_aircrafts as ra
import numpy as np
import pandas as pd
import math
# Data file for aircraft parameters and constants

g = 9.80665
R = 287
T_sl = 288 # [K] temp at sea level isa
P_sl = 101325 # [Pa] pressure at sea level isa
a = -0.0065 # [K/m] temperature lapse rate with altitude

MTOM = 86000 # [kg]
payload_max = 18960 # [kg]
payload_MTOW = 8531 # [kg]
M = 0.85 # cruise mach number at 31000 [ft]
dist_take_off = 3048 # [m]
l_fl = 1981.2 # [m] landing field length
c_lfl = 0.45 # [s^2/m] landing field length coefficient suggested in adsee book p.133
range_harmonic = 9545 # [km] at 18960 [kg]
range_MTOW_full_fuel = 11716 # [km] at a payload of 8531 [kg]
range_ferry = 12697 # [km]
speed_stall_landing_field = (l_fl/0.45)**0.5 # [m/s]
m_fraq_cruise = 0.95
m_fraq_landing = 0.85
#cl_cruise = 1.5
cl_landing = 2.2
cl_take_off = 1.8
s_wing = np.mean(ra.df["Wing Surface Area [m²]"]) # [m]
speed_stall_cl_max = ((m_fraq_landing * MTOM * 9.80665) / (cl_landing * 0.5 * 1.225 * s_wing)) ** 0.5 # [m/s]
speed_stall_lf = (l_fl / c_lfl) ** 0.5 # approximation of stall speed based on the length of the landing field
altitude_cruise = 9448.8 # [m]
altitude_landing = 0 # [m] landing altitude suggested in the book, maybe should be changed
altitude_lfl = 0
altitude_take_off = 0
T_delta = 15 # [K] hot day conditions
AR = 9.7 # previously 9.7 Average aspect ratio of reference aircrafts
S_wet_to_S = np.mean(ra.df["Swet/S"])
S_wet = np.median(ra.df["Swet"]) # Wetted area of our aircraft
bypass = 11 # Bypass ratio
taper = 0.246  # from WP2 iteration
cr = 6.79  # from WP2 iteration
b = 41 # from WP2 iteration
sweepQC = 0.537 # rad, from WP2
sweepLE = math.atan(math.tan(sweepQC) + 0.25 * (2*cr/b)*(1 - taper))  # leading edge sweep using WP2 values
sweepHC = math.atan(math.tan(sweepLE) - 0.5*(2*cr/b)*(1 - taper))  # half chord sweep using WP2 values
oswald = 2 / (2 - AR + math.sqrt(4 + AR**2 * (1 + (math.tan(sweepHC))**2)))  # new oswald using WP2, previously 1/(0.042*math.pi*AR) #From fig 6.4
c_f = 0.0029 # From fig 6.3
c_d0 = 0.023728434483470374 # value from Class II drag, previously: c_f * S_wet_to_S
Ne = 2 # number of engines
climb_rate_requirement = 12.75  # [m/s]
T_lfl_hot = T_sl + T_delta + a * altitude_landing
T_landing = T_sl + a * altitude_landing
T_cruise = T_sl + a * altitude_cruise
T_take_off_hot = T_sl + T_delta + a * altitude_take_off
T_take_off = T_sl + a * altitude_take_off
P_cruise = P_sl * (1 + (a * altitude_cruise) / T_sl) ** (-g / (a * R))
P_landing = P_sl * (1 + (a * altitude_landing) / T_sl) ** (-g / (a * R))
P_lfl = P_sl * (1 + (a * altitude_lfl) / T_sl) ** (-g / (a * R))
P_take_off = P_sl * (1 + (a * altitude_take_off) / T_sl) ** (-g / (a * R))
rho_cruise = P_cruise / (R * T_cruise)
rho_landing = P_landing / (R * T_landing)
rho_lfl_hot = P_landing / (R * T_lfl_hot)
rho_take_off = P_take_off / (R * T_take_off)
rho_take_off_hot = P_take_off / (R * T_take_off_hot)
theta_t_break = 1.08

velocity_cruise = M * (1.4 * R * T_cruise) ** 0.5
cl_cruise = (MTOM*m_fraq_cruise*9.80665)/(0.5*rho_cruise*s_wing*velocity_cruise**2)
velocity_stall = ((MTOM * 9.80665) / (cl_take_off * 0.5 * 1.225 * s_wing)) ** 0.5
