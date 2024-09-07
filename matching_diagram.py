import matplotlib.pyplot as plt
import numpy as np
import pandas as pd
import aircraft_data as ad

# W/S [N/m^2] Generating the wing loading list 0 to 9000 with increment of 100
wing_loading = np.linspace(0, 9000, num=91)

# W/S [N/m^2] Calculating the maximum wing loading for the minimum speed requirement
min_speed = (1 / ad.m_fraq_min_speed * (1.225 / 2) * (ad.speed_approach / 1.23) ** 2 * ad.cl_landing)

# Plot size
plt.figure(figsize=(12, 8))

plt.axvline(x = min_speed, color = 'b', label = 'Minimum speed')

plt.legend(loc = 'upper left')

plt.show()
