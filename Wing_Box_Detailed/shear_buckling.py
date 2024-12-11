import numpy as np
import wing_box_constants as wb
from Wing Structure import Ixx

def getSparHeight(spar_id, y):
    d1, d2, d3, d4 = Wingbox_lengths(wb.d_1, wb.d_2, wb.d_3, wb.d_4, wb.b, y)
    return d1

def criticalShear(k_s, E, poisson, t, b):
    tau_cr = np.pi**2 * k_s * E / (12 * (1 - poisson**2)) * (t/b)**2 
    return tau_cr

#insert a shear force value V (needs to be integrated from the distribution at a particular span y
def avgShear(V, y, h_1, h_2, h_3, t_1, t_2, t_3):
    #compute the shear force at a particular span y by integrating
    avg_shear = V/(h_1 * t_1 + h_2 * t_2 + h_3 * t_3)
    return avg_shear

tau_cr = criticalShear(wb.k_s1, wb.E, wb.poisson, wb.spar_t1, wb.spar_b1)