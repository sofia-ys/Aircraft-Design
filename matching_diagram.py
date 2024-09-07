import matplotlib.pyplot as plt
import numpy as np
import pandas as pd
import aircraft_data as ad

# W/S [N/m^2] Generating the wing loading list 0 to 9000 with increment of 100
wing_loading = np.linspace(0, 9000, num=91)

# W/S [N/m^2] Calculating the maximum wing loading for the minimum speed requirement
min_speed = (1 / ad.m_fraq_landing * (1.225 / 2) * (ad.speed_approach / 1.23) ** 2 * ad.cl_landing)

# W/S [N/m^2] Calculating the maximum wing loading for the landing field length requirement
landing_field_length = (1 / ad.m_fraq_landing) * (ad.l_fl / ad.c_lfl) * ((ad.rho_landing * ad.cl_landing) / 2)

# Plot size
plt.figure(figsize=(12, 8))

plt.axvline(x = min_speed, color = 'b', label = 'Minimum speed')
plt.axvline(x = landing_field_length, color = 'orange' , label = 'Landing field length')

plt.legend(loc = 'upper left')

plt.show()
