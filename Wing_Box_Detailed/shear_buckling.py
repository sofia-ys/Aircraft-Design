import numpy as np
import wing_box_constants as wb
from Ixx import Wingbox_lengths

def getSparHeight(spar_id, y):
    d1, d2, d3, d4 = Wingbox_lengths(wb.d_1, wb.d_2, wb.d_3, wb.d_4, wb.b, y)
    return d1

def criticalShear(k_s, E, poisson, t, b):
    tau_cr = np.pi**2 * k_s * E / (12 * (1 - poisson**2)) * (t/b)**2 
    return tau_cr

tau_cr = criticalShear(wb.k_s1, wb.E, wb.poisson, wb.spar_t1, wb.spar_b1)