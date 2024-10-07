import matplotlib.pyplot as plt
import numpy as np
import math
import cd
import payloadrange
# Combined engine efficiencies
n_eng_times_n_p = 0.4275727
# Calculate the R_eq

R_lost = (1/0.7) * (cd.l_d_cruise) * (cd.altitude_cruise + (pow(cd.velocity_cruise, 2) / (2 * 9.81)))
R_eq = (payloadrange.designRange + R_lost / 1000) * (1 + 0.05) + 1.2 * 250 + (30 * 60) * (cd.velocity_cruise / 1000)
# Fuel mass fraction
m_ff = 1 - math.exp((-R_eq * 1000)/(n_eng_times_n_p*(43 * pow(10,6)/9.81) * cd.l_d_cruise))
# Calculate maximum takeoff mass
M_mto = (1556.2 + cd.payload_max)/(1-0.4874-m_ff)

print('R_lost' + str(R_lost))
print('R_eq (equivalent range): ' + str(R_eq))
print('Fuel mass fraction: ' + str(m_ff))
print('\n')
print('Maximum takeoff mass: ' + str(M_mto))