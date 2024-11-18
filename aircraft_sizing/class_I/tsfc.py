import numpy as np

B = 11 #from aircraft data
TSFC_reader = 22*(B**(-0.19)) # [g/kN/s], Eq. 6.23 in ADSEE reader
V_Cr = 256.47 #from aircraft data
e_f = 43    #MJ/kg
prop_efficiency_eng_efficiency = V_Cr/(TSFC_reader*e_f) #Eq. 6.21 in ADSEE reader

print(prop_efficiency_eng_efficiency)