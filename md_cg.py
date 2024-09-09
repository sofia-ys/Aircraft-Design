import numpy as np
import math as ma
import matplotlib.pyplot as plt
import pandas as pd
import aircraft_data as ad

wing_loading = np.linspace(0, 9000, num=91)
T_W = []
V = []
M = []
theta_t = []
delta_t = []
alpha_t = []
c_v = 0.032
beta = 1
B = 12

for i in wing_loading:
    V.append(ma.sqrt((2*i)/ (1.225 * ad.cl_landing /1.1)))

for i in V:
    M.append(i / (ma.sqrt(1.4*287*28815)))

for i in M:
    theta_t.append((ad.T_sl * (1 + 0.2 * i **2))/ad.T_sl)

for i in M:
    delta_t.append(((ad.P_sl * (1 + 0.2 * i **2)) **(1.4/0.4))/ad.P_sl)

for i in range(91):
    alpha_t.append(delta_t[i]*(1-(0.43+0.01)))

print(theta_t)
print(delta_t)

