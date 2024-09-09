import numpy as np
import matplotlib.pyplot as plt
import matching_diagram as md
import aircraft_data as ad

mass_ratio = 0.95

CD0 = 0.018
density = 0.3803
v_cr = 251.6
AR = 8.31
e = 0.8
mach = 0.85
bypass = 11

def cruise_thrust_to_weight(wing_loading):
    p_t = 23800 * ((1 + 0.2 * mach ** 2) ** (1.4 / 0.4))

    delta_t = p_t / 101325

    lapse = delta_t * (1 - (0.43 + 0.014 * bypass) * np.sqrt(mach))

    for i in wing_loading:
        T_W.append(mass_ratio / lapse * ((CD0 * 0.5 * density * v_cr ** 2)/(mass_ratio * i) +
                                  (mass_ratio * i) / (np.pi * AR * e * density * v_cr ** 2)))

    return T_W

#calculate the thrust lapse
    """""""""
#def lapse ():
    p_t = 23800 * ((1 + 0.2 * mach ** 2) ** (1.4 / 0.4))

    delta_t = p_t / 101325 

    lapse = delta_t * (1- (0.43 + 0.014 * bypass) * np.sqrt(mach))
    
    return lapse

thrust_lapse = lapse()
print(thrust_lapse)

# The power loading function
def cruise_thrust_weight (loading):
    x = mass_ratio / thrust_lapse * ( (CD0 * 0.5 * density * v_cr ** 2)/(mass_ratio * loading) + 
    (mass_ratio * loading) / (np.pi * AR * e * density * v_cr ** 2) )

    return x

"""""

plt.plot(loading, cruise_thrust_to_weight(loading))

plt.show()