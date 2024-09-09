import numpy as np
import math as ma
import matplotlib.pyplot as plt
import pandas as pd
import aircraft_data as ad

wing_loading = np.linspace(0, 9000, num=91)
T_W = []
V = []
M = []
theta_t
c_v = 0.032
beta = 1

for i in wing_loading:
    V.append(ma.sqrt((2*i)/ (1.225 * ad.cl_landing /1.1)))

for i in V:
    M.append(i / (ma.sqrt(1.4*287*28815)))

for i in M:


