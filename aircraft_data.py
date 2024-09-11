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

MTOM = 113051 # [kg]
payload_max = 18960 # [kg]
M = 0.85 # cruise mach number at 31000 [ft]
dist_take_off = 3048 # [m]
l_fl = 1981.2 # [m] landing field length
range_harmonic = 9545 # [km] at 18960 [kg]
range_MTOW_full_fuel = 11716 # [km] at a payload of 8531 [kg]
range_ferry = 12697 # [km]
speed_stall_landing_field = (l_fl/0.45)**0.5 # [m/s]
m_fraq_cruise = 0.95
m_fraq_landing = 0.85
c_l_max_landing = 2.3
s_wing = np.mean(ra.df["Wing Surface Area [m²]"]) # [m]
speed_stall_cl_max = ((m_fraq_landing*MTOM*9.80665)/(c_l_max_landing*0.5*1.225*s_wing))**0.5 # [m/s]
altitude_cruise = 9448.8 # [m]
altitude_landing = 0 # [m] landing altitude suggested in the book, maybe should be changed
altitude_take_off = 0
T_delta = 15 # [K] hot day conditions
AR = np.mean(ra.df["Aspect Ratio"]) # Average aspect ratio of reference aircrafts
S_wet_to_S = np.mean(ra.df["Swet/S"])
S_wet = np.median(ra.df["Swet"]) # Wetted area of our aircraft
bypass = 11 # Bypass ratio
oswald = 1/(0.0472*math.pi*AR) #From fig 6.4
c_f = 0.0029 # From fig 6.3
c_d0 = c_f * S_wet_to_S
Ne = 2 # number of engines

#cl_cruise = 1.5
cl_landing = 2.5
cl_take_off = 2

c_lfl = 0.45 # [s^2/m] landing field length coefficient suggested in adsee book p.133
T_landing = T_sl + T_delta + a * altitude_landing
T_cruise = T_sl + a * altitude_cruise
T_take_off = T_sl + T_delta + a * altitude_take_off
P_cruise = P_sl * (1 + (a * altitude_cruise) / T_sl) ** (-g / (a * R))
P_landing = P_sl * (1 + (a * altitude_landing) / T_sl) ** (-g / (a * R))
P_take_off = P_sl * (T_take_off/T_sl) ** (g / a / R)
rho_cruise = P_cruise / (R * T_cruise)
rho_landing = P_landing / (R * T_landing)
rho_take_off = P_take_off / (R * T_take_off)
theta_t_break = 1.08

velocity_cruise = M * (1.4 * R * T_cruise) ** 0.5
cl_cruise = (MTOM*m_fraq_cruise*9.80665)/(0.5*rho_cruise*s_wing*velocity_cruise**2)