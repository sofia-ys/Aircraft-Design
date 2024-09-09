import matplotlib.pyplot as plt
import numpy as np
import aircraft_data as ad
import cruise_speed
import climb_gradient
import take_off_field_length
import climb_rate

# W/S [N/m^2] Generating the wing loading list 100 to 9000 with increment of 100
wing_loading = np.linspace(100, 9000, num=90)

# W/S [N/m^2] Calculating the maximum wing loading for the minimum speed requirement
min_speed = (1 / ad.m_fraq_landing * (1.225 / 2) * (ad.speed_stall_landing_field / 1.23) ** 2 * ad.cl_landing)

# W/S [N/m^2] Calculating the maximum wing loading for the landing field length requirement
landing_field_length = (1 / ad.m_fraq_landing) * (ad.l_fl / ad.c_lfl) * ((ad.rho_landing * ad.cl_landing) / 2)

cruise_speed = cruise_speed.cruise_thrust_to_weight(wing_loading)

climb_gradient_119 = climb_gradient.calcGradient119(wing_loading)

climb_gradient_121a = climb_gradient.calcGradient121a(wing_loading)

climb_gradient_121b = climb_gradient.calcGradient121b(wing_loading)

climb_gradient_121c = climb_gradient.calcGradient121c(wing_loading)

climb_gradient_121d = climb_gradient.calcGradient121d(wing_loading)

take_off_field_length = take_off_field_length.take_off_field_length(wing_loading)

climb_rate = climb_rate.climb_rate(wing_loading)

# Plot size
plt.figure(figsize=(12, 8))

plt.axvline(x = min_speed, color = 'b', label = 'Minimum speed')
plt.axvline(x = landing_field_length, color = 'orange' , label = 'Landing field length')
plt.plot(wing_loading, cruise_speed, color = 'purple', label = 'Cruise speed')
plt.plot(wing_loading, climb_gradient_119, color = 'red', label = 'Climb gradient 119')
plt.plot(wing_loading, climb_gradient_121a, color = 'magenta', label = 'Climb gradient 121a')
plt.plot(wing_loading, climb_gradient_121b, color = 'cyan', label = 'Climb gradient 121b')
plt.plot(wing_loading, climb_gradient_121c, color = 'green', label = 'Climb gradient 121c')
plt.plot(wing_loading, climb_gradient_121d, color = 'brown', label = 'Climb gradient 121d')
plt.plot(wing_loading, take_off_field_length, color = 'black' , label = 'Take off field length')
plt.plot(wing_loading, climb_rate, color = 'pink', label = 'Climb rate')

plt.xlim(0, 8000)
plt.ylim(0, 1)

plt.legend(loc = 'upper left')

plt.show()
