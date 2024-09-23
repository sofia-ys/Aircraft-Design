import math
import mac as mac
import numpy as np

clAlpha =  1.23 # airfoil lift
sRef = 173.77  # m2
b = 38  # m
deltaA =  0.084 # max aileron deflection
velocity = 0.85  # mach, find the m/s
tau =  0.67 # from literature
cd0 =  0.003 # airfoil cd0
delX = 0.1 # step size for b range
Pideal = 32.14 # roll rate, 45 deg/ 1.4 s

def findCY(xPos):
    yInter = mac.mLeading * xPos + mac.cLeading
    cy = abs(((-0.25*mac.cRoot - (b/2)*math.tan(mac.sweep) - 0.75*mac.cTip) + mac.cRoot)/(b/2) * xPos - mac.cRoot - yInter)
    return cy


intClDeltTab = []
for i1 in np.arange(0, b/2, delX):
    for i2 in np.arange(i1, b/2, delX):
        intClDelt = findCY(i2) * 0.5 * (i2)**2 - findCY(i1) * 0.5 * (i1)**2
        intClDeltTab.append(intClDelt)

print(intClDeltTab)

intClPTab = []
for j1 in np.arange(0, b/2, delX):
    for j2 in np.arange(j1, b/2, delX):
        intClP = findCY(j2) * (1/3) * (j2)**3 - findCY(j1) * (1/3) * (j1)**3
        intClPTab.append(intClP)

Ptab = []
for k in range(len(intClDeltTab)):
    clDelta = (2 * clAlpha * tau)/(sRef * b) * intClDeltTab[k]
    clP = (-4 * (clAlpha + cd0))/(sRef * b**2) * intClPTab[k]
    P = -clDelta/clP * deltaA * (2 * velocity)/b
    Ptab.append(P)

difTab = []
for j in range(len(Ptab)):
    dif = Ptab[j] - Pideal
    difTab.append(dif)

bInd = difTab.index(min(difTab))