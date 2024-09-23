import math
import mac as mac
import numpy as np

clAlpha =  1.23 # airfoil lift NEED THE ACTUAL VALUE !!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!
sRef = 173.77  # m2
b = 38  # m
deltaA =  0.084 # max aileron deflection NEED THE ACTUAL VALUE !!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!
velocity = 256.555  # cruise velocity in m/s
tau =  0.67 # from literature NEED THE ACTUAL VALUE !!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!
cd0 =  0.003 # airfoil cd0 NEED THE ACTUAL VALUE !!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!
delX = 0.1 # step size for b range
Pideal = 32.14 # roll rate, 45 deg/ 1.4 s NEED THE ACTUAL VALUE !!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!

# getting the chord length at a certain x position
def findCY(xPos):
    yInter = mac.mLeading * xPos + mac.cLeading 
    cy = abs(((-0.25*mac.cRoot - (b/2)*math.tan(mac.sweep) - 0.75*mac.cTip) + mac.cRoot)/(b/2) * xPos - mac.cRoot - yInter)
    return cy

intClDeltTab = np.zeros((int((b/2)/delX), int((b/2)/delX)))  # making an array for this integral
for i1idx, i1 in enumerate(np.arange(0, b/2, delX)):
    for i2idx, i2 in enumerate(np.arange(i1, b/2, delX)):
        intClDeltTab[i1idx, i2idx] = findCY(i2) * 0.5 * (i2)**2 - findCY(i1) * 0.5 * (i1)**2                                                                                                                                                                                                                 

intClPTab = np.zeros((int((b/2)/delX), int((b/2)/delX)))  # making an array for this integral
for j1idx, j1 in enumerate(np.arange(0, b/2, delX)):
    for j2idx, j2 in enumerate(np.arange(i1, b/2, delX)):
        intClDeltTab[j1idx, j2idx] = findCY(j2) * (1/3) * (j2)**3 - findCY(j1) * (1/3) * (j1)**3  # at the index according to the iteration number, insert evaluated integral

Ptab = np.zeros((int((b/2)/delX), int((b/2)/delX)))  # making an array for this integral
rP, cP = Ptab.shape
for k in range(rP):
    for m in range(cP):
        clDelta = (2 * clAlpha * tau)/(sRef * b) * intClDeltTab[k, m]
        clP = (-4 * (clAlpha + cd0))/(sRef * b**2) * intClPTab[k, m]

        if clP == 0:  # making sure no divide by zero
            continue
        else:
            P = -clDelta/clP * deltaA * (2 * velocity)/b
            Ptab[k, m] = P

difTab = np.zeros((int((b/2)/delX), int((b/2)/delX)))  # making an array for this integral
rD, cD = difTab.shape
for n in range(rD):
    for p in range(cD):
        dif = Ptab[n, p] - Pideal
        difTab[n, p] = dif

idx1, idx2 = np.where(difTab == np.min(difTab))

b1 = idx1 * delX
b2 = idx1 * delX + idx2 * delX

print(b1, b2)