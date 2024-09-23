import math
import mac as mac
import numpy as np

clAlpha =  1.23 # airfoil lift NEED THE ACTUAL VALUE !!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!
sRef = 173.77  # m2
b = 38  # m
deltaA =  8.75 # max aileron deflection NEED THE ACTUAL VALUE !!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!
velocity = 256.555  # cruise velocity in m/s
tau =  0.67 # from literature NEED THE ACTUAL VALUE !!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!
cd0 =  0.003 # airfoil cd0 NEED THE ACTUAL VALUE !!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!
delX = 0.01 # step size for b range
Pideal = 32.14 # roll rate, 45 deg/ 1.4 s NEED THE ACTUAL VALUE !!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!
lst = []

# getting the chord length at a certain x position
def findCY(xPos):
    yInter = mac.mHalf * xPos + mac.cHalf 
    cy = abs(((-0.25*mac.cRoot - (b/2)*math.tan(mac.sweep) - 0.75*mac.cTip) + mac.cRoot)/(b/2) * xPos - mac.cRoot - yInter)
    return cy

intClDeltTab = np.zeros((int((b/2)/delX), int((b/2)/delX)))  # making an array for this integral
for i1idx, i1 in enumerate(np.arange(0, b/2, delX)):
    for i2idx, i2 in enumerate(np.arange(i1, b/2, delX)):
        intClDeltTab[i1idx, i2idx] = findCY(i2) * 0.5 * (i2)**2 - findCY(i1) * 0.5 * (i1)**2                                                                                                                                                                                                              

intClp = findCY(b/2) * (1/3) * (b/2)**3 - findCY(0) * (0) * (0)**3  # finding the integral of the clp value

Ptab = np.zeros((int((b/2)/delX), int((b/2)/delX)))  # making an array for this integral
rP, cP = Ptab.shape
for k in range(rP):
    for m in range(cP):
        clDelta = (2 * clAlpha * tau)/(sRef * b) * intClDeltTab[k, m]
        clP = (-4 * (clAlpha + cd0))/(sRef * b**2) * intClp

        if clP == 0:  # making sure no divide by zero
            continue
        else:
            P = -clDelta/clP * deltaA * (2 * velocity)/b
            Ptab[k, m] = P

difTab = np.zeros((int((b/2)/delX), int((b/2)/delX)))  # making an array for this integral
rD, cD = difTab.shape
for n in range(rD):
    for p in range(cD):
        dif = abs(Ptab[n, p] - Pideal)
        difTab[n, p] = dif

mini = 99999
for i in range(rD):
    for j in range(cD):
            if (mini > difTab[i,j] and difTab[i,j]!= 32.14):
                mini = difTab[i,j]
                idx1 = i
                idx2 = j

b1 = idx1 * delX
b2 = idx1 * delX + idx2 * delX

print(mini, b1, b2)