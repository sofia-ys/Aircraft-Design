import matplotlib.pyplot as plt
import numpy as np
import pandas as pd
import aircraft_data as ad
import cruise_speed

# W/S [N/m^2] Generating the wing loading list 100 to 9000 with increment of 100
wing_loading = np.linspace(100, 9000, num=90)

# W/S [N/m^2] Calculating the maximum wing loading for the minimum speed requirement
min_speed = (1 / ad.m_fraq_landing * (1.225 / 2) * (ad.speed_stall_landing_field / 1.23) ** 2 * ad.cl_landing)

# W/S [N/m^2] Calculating the maximum wing loading for the landing field length requirement
landing_field_length = (1 / ad.m_fraq_landing) * (ad.l_fl / ad.c_lfl) * ((ad.rho_landing * ad.cl_landing) / 2)

cruise_speed = cruise_speed.cruise_thrust_to_weight(wing_loading)

# Plot size
plt.figure(figsize=(12, 8))

plt.axvline(x = min_speed, color = 'b', label = 'Minimum speed')
plt.axvline(x = landing_field_length, color = 'orange' , label = 'Landing field length')
plt.plot(wing_loading, cruise_speed, color = 'purple', label = 'Cruise speed')

plt.legend(loc = 'upper left')

plt.show()
