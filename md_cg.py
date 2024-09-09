import numpy as np
import math as ma
import matplotlib.pyplot as plt
import pandas as pd
import aircraft_data as ad

T_W = []
V = []
M = []
theta_t = []
delta_t = []
alpha_t = []
c_v = 0.032
beta = 1
B = 11
#create a function to calculate all flight gradient requirements
def calcClimbGradient(wing_loading, cl_req):
    climb_gradient = []
    for i in wing_loading:
        V.append(ma.sqrt((2*i)/ (1.225 * cl_req /1.1)))

    for i in V:
        M.append(i / (ma.sqrt(1.4*287*288.15))) #using sea level values, since all the flight gradient requirements use it

    print(M)
    print('\n')

    for i in M:
        theta_t.append((ad.T_sl * (1 + 0.2 * i **2))/ad.T_sl)

    print(theta_t)
    print('\n')

    for i in M:
        delta_t.append((ad.P_sl * pow((1 + 0.2 * pow(i, 2)), (1.4/0.4)))/ad.P_sl)

    print(delta_t)
    print('\n')

    for i in range(90):
        alpha_t.append(delta_t[i]*(1-(0.43+0.014*B)* ma.sqrt(M[i])))
    
    print(alpha_t)
    print('\n')

    for i in alpha_t:
        climb_gradient.append((1/i)*(c_v + 2*ma.sqrt(0.011/(ma.pi * ad.AR * 0.8))))   #0.011 shall be replaced with cd_0 and 0.8 with e (oswald)!!
    
    print(climb_gradient)

calcClimbGradient(np.linspace(100, 9000, num=90), 2.09) #just a dummy lift coeff for now
