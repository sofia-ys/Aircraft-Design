import numpy as np
import aircraft_data as ad

density = 0.3803
v_cr = 251.6

def cruise_thrust_to_weight(wing_loading):
    t_w = []
    p_t = 23800 * ((1 + 0.2 * ad.M ** 2) ** (1.4 / 0.4))

    delta_t = p_t / 101325

    lapse = delta_t * (1 - (0.43 + 0.014 * ad.bypass) * np.sqrt(ad.M))

    for i in wing_loading:
        t_w.append(ad.m_fraq_cruise / lapse * ((ad.c_d0 * 0.5 * density * v_cr ** 2)/(ad.m_fraq_cruise * i) +
                                  (ad.m_fraq_cruise * i) / (np.pi * ad.AR * ad.oswald * density * v_cr ** 2)))

    return t_w
