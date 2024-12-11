import numpy as np
import wing_box_constants as wb

def criticalShear(k_s, E, poisson, t, b):
    tau_cr = np.pi**2 * k_s * E / (12 * (1 - poisson**2)) * (t/b)**2 
    return tau_cr

