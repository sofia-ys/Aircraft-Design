import numpy as np
import aircraft_data as ad


def cruise_thrust_to_weight(wing_loading):
    t_w = []
    p_t = 23800 * ((1 + 0.2 * ad.M ** 2) ** (1.4 / 0.4))

    delta_t = p_t / 101325

    lapse = delta_t * (1 - (0.43 + 0.014 * ad.bypass) * np.sqrt(ad.M))

    for i in wing_loading:
        t_w.append(ad.m_fraq_cruise / lapse * ((ad.c_d0 * 0.5 * ad.rho_cruise * ad.velocity_cruise ** 2) /
                                               (ad.m_fraq_cruise * i) + (ad.m_fraq_cruise * i) /
                                               (np.pi * ad.AR * ad.oswald * ad.rho_cruise * ad.velocity_cruise ** 2)))

    return t_w
