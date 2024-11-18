import numpy as np
import aircraft_data as ad


def climb_rate(wing_loading):
    alpha_t = ((ad.P_cruise * (1 + 0.2 * ad.M) ** (1.4/0.4)) / ad.P_sl) * (1 - (0.43 + 0.014 * ad.bypass) * ad.M ** 0.5)
    w_t = (ad.m_fraq_cruise / alpha_t) * (((ad.climb_rate_requirement ** 2 * ad.rho_cruise) /
                                           (2 * ad.m_fraq_cruise * wing_loading) *
                                           (ad.c_d0 * np.pi * ad.AR * ad.oswald) ** 0.5) ** 0.5 +
           2 * (ad.c_d0 / (np.pi * ad.AR * ad.oswald)))
    return w_t
