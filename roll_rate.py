import math
import mac as mac
import numpy as np

clAlpha =  0.117 # airfoil lift
sRef = 173.77  # m2
b = 38  # m
deltaA =  8.75 # max aileron deflection NEED THE ACTUAL VALUE !!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!
velocity = 256.555  # cruise velocity in m/s
tau =  0.67 # from literature NEED THE ACTUAL VALUE !!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!
cd0 =  0.0064 # airfoil cd0 
delX = 0.01 # step size for b range
Pideal = 32.14 # roll rate, 45 deg/ 1.4 s 

# getting the chord length at a certain x position
def findCY(xPos):
    y1 = mac.mLE * xPos + mac.cLE  # get the y coordinate of the leading edge at a certain x
    y2 = mac.mTE * xPos + mac.cTE  # y coord of trailing edge
    cy = y1 - y2  # chord length is y of LE - y of TE
    return cy

# iterating through every b1 and b2 possible for the cldelt value
intClDeltTab = np.zeros((int((b/2)/delX), int((b/2)/delX)))  # making an array for this integral
for i1idx, i1 in enumerate(np.arange(0, b/2, delX)):  # using ennumerate to assign an integer to every number we use to use for the indices
    for i2idx, i2 in enumerate(np.arange(i1, b/2, delX)):
        intClDeltTab[i1idx, i2idx] = findCY(i2) * 0.5 * (i2)**2 - findCY(i1) * 0.5 * (i1)**2  # applying integral at point b2 - b1                                                                                                                                                                                                          

# finding the clp value (constant)
clP = (-4 * (clAlpha + cd0))/(sRef * b**2) * (findCY(b/2) * (1/3) * (b/2)**3 - findCY(0) * (0) * (0)**3) 

# finding all possible roll rates (P)
Ptab = np.zeros((int((b/2)/delX), int((b/2)/delX)))  # making an array for this integral
rP, cP = Ptab.shape  # finding the number of rows and columns in the ptab
for k in range(rP):
    for m in range(cP):
        clDelta = (2 * clAlpha * tau)/(sRef * b) * intClDeltTab[k, m]  # calculating the clDelta for each value of our cldelt 

        if clP == 0:  # making sure no divide by zero
            continue
        else:
            P = -clDelta/clP * deltaA * (2 * velocity)/b  # calculating the P value for each cldelta 
            Ptab[k, m] = P  # putting this P value in our table at the exact position

difTab = np.zeros((int((b/2)/delX), int((b/2)/delX)))  # making an array for this integral
rD, cD = difTab.shape  
for n in range(rD):
    for p in range(cD):
        dif = abs(Ptab[n, p] - Pideal)  # finding difference between the P we want and all the Ps we calculated
        difTab[n, p] = dif  # putting this difference into the table at the same position

min = 99999  # high number that the values in dif table will definitely be less than
for i in range(rD):
    for j in range(cD):
            if (min > difTab[i,j] and difTab[i,j]!= 32.14):  # making sure our min isn't zero
                min = difTab[i,j]
                idx1 = i
                idx2 = j

b1 = idx1 * delX  # calculating b1
b2 = idx1 * delX + idx2 * delX  # b2

print(min, b1, b2)