import math as mt
MTOW= 117604
LW = 0.85*MTOW
f= LW/MTOW
LCN= 62 # from adsee
#number of wheels
Number_of_wheels = f*MTOW*9.80665/210000
print("Number of wheels", Number_of_wheels)

#tire pressure

p= 430*mt.log(LCN, mt.e)-680


#static loads
P_mw = 0.92*MTOW/4
P_nw = 0.08*MTOW/2

print("Main wheel Static load (in kg)",P_mw)
print("Main nose wheel static load (in kg)",P_nw)
print(p)
#british
#diamter = 20.5
#width = 6

#american
#diameter =18
#width = 5.5
