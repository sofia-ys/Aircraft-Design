# Data file for aircraft parameters and constants

payload_max = 18960 # [kg]
M = 0.85 # cruise mach number at 31000 [ft]
dist_take_off = 10000 # [ft]
dist_landing = 6500 # [ft]
range_harmonic = 9545 # [km] at 18960 [kg]
range_MTOW_full_fuel = 11716 # [km] at a payload of 8531 [kg]
range_ferry = 12697 # [km]
speed_approach = 74.6 # [m/s]
cl_cruise = 1.5
cl_landing = 2.5
cl_take_off = 2
m_fraq_min_speed = 0.85
c_lfl = 0.45 # [s^2/m] landing field length coefficient suggested in adsee book p.133
l_lf = c_lfl * speed_approach ** 2 # landing field length
