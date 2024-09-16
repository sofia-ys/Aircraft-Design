import matplotlib.pyplot as plt
import numpy as np
import aircraft_data as ad
import cruise_speed
import climb_gradient
import take_off_field_length
import climb_rate
import reference_aircrafts

# W/S [N/m^2] Generating the wing loading list 100 to 9000 with increment of 100
wing_loading = np.linspace(1, 9000, num=9000)

# W/S [N/m^2] Calculating the maximum wing loading for the minimum speed requirement
min_speed = (1 / ad.m_fraq_landing * (ad.rho_landing / 2) * ad.speed_stall_lf ** 2 * ad.cl_landing)

# W/S [N/m^2] Calculating the maximum wing loading for the landing field length requirement
landing_field_length = (1 / ad.m_fraq_landing) * (ad.l_fl / ad.c_lfl) * ((ad.rho_lfl_hot * ad.cl_landing) / 2)

cruise_speed = cruise_speed.cruise_thrust_to_weight(wing_loading)

climb_gradient_119 = climb_gradient.calcGradient119(wing_loading)

climb_gradient_121a = climb_gradient.calcGradient121a(wing_loading)

climb_gradient_121b = climb_gradient.calcGradient121b(wing_loading)

climb_gradient_121c = climb_gradient.calcGradient121c(wing_loading)

climb_gradient_121d = climb_gradient.calcGradient121d(wing_loading)

take_off_field_length = take_off_field_length.take_off_field_length(wing_loading)

climb_rate = climb_rate.climb_rate(wing_loading)

# Plot size
plt.figure(figsize=(15, 11))

plt.title('Matching Diagram', fontsize = 20)
plt.xlabel('W/S - [N/m2]', fontsize = 15)
plt.ylabel('T/W - [N/N]', fontsize = 15)

plt.axvline(x = min_speed, color = 'royalblue', label = 'Minimum speed')
plt.axvline(x = landing_field_length, color = 'orangered' , label = 'Landing field length')
plt.plot(wing_loading, cruise_speed, color = 'indigo', label = 'Cruise speed')
plt.plot(wing_loading, climb_gradient_119, color = 'red', label = 'Climb gradient 119')
plt.plot(wing_loading, climb_gradient_121a, color = 'deepskyblue', label = 'Climb gradient 121a')
plt.plot(wing_loading, climb_gradient_121b, color = 'darkgoldenrod', label = 'Climb gradient 121b')
plt.plot(wing_loading, climb_gradient_121c, color = 'forestgreen', label = 'Climb gradient 121c')
plt.plot(wing_loading, climb_gradient_121d, color = 'brown', label = 'Climb gradient 121d')
plt.plot(wing_loading, take_off_field_length, color = 'darkslategray' , label = 'Take off field length')
plt.plot(wing_loading, climb_rate, color = 'deeppink', label = 'Climb rate')
plt.plot(landing_field_length, climb_gradient_121b[int(np.floor(landing_field_length))], marker = 'D', color = 'crimson', markersize = '6', label = 'Design point')
plt.scatter(reference_aircrafts.W / reference_aircrafts.S, reference_aircrafts.T / reference_aircrafts.W, label = 'Reference aircrafts')

plt.xlim(0, 8000)
plt.ylim(0, 1)

plt.legend(loc = 'upper left')
print(landing_field_length, climb_gradient_121b[int(np.floor(landing_field_length))])
plt.show()
