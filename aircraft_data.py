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

payload_max = 18960 # [kg]
M = 0.85 # cruise mach number at 31000 [ft]
dist_take_off = 10000 # [ft]
l_fl = 1980 # [m] landing field length
range_harmonic = 9545 # [km] at 18960 [kg]
range_MTOW_full_fuel = 11716 # [km] at a payload of 8531 [kg]
range_ferry = 12697 # [km]
speed_approach = (l_fl/0.45)**0.5 # [m/s]
altitude_landing = 0 # [m] landing altitude suggested in the book, maybe should be changed
T_delta = 15 # [K] hot day conditions
AR = np.mean(ra.df["Aspect Ratio"]) # Average aspect ratio of reference aircrafts
S_wet_to_S = np.mean(ra.df["Swet/S"])
S_wet = np.median(ra.df["Swet"]) # Wetted area of our aircraft
bypass = 11 # Bypass ratio
oswald = 1/(0.0472*math.pi*AR)

cl_cruise = 1.5
cl_landing = 2.5
cl_take_off = 2

m_fraq_landing = 0.85

c_lfl = 0.45 # [s^2/m] landing field length coefficient suggested in adsee book p.133
P_landing = P_sl * (1 + (a * altitude_landing) / T_sl) ** (-g / (a * R))
T_landing = T_sl + T_delta + a * altitude_landing
rho_landing = P_landing / (R * T_landing)
theta_t_break = 1.08
