import math
import mac

clAlpha =  1.23 # airfoil lift
sRef = 173.77  # m2
b = 38  # m
deltaA =  0.084 # max aileron deflection
velocity = 0.85  # mach, find the m/s
tau =  0.67 # from literature
cd0 =  0.003 # airfoil cd0
length = 2 # length of aileron
Pideal = 32.14 # roll rate, 45 deg/ 1.4 s

def findCY(b1):
    yInter = mac.mLeading * b1 + mac.cLeading
    cy = abs(((-0.25*mac.cRoot - (b/2)*math.tan(mac.sweep) - 0.75*mac.cTip) + mac.cRoot)/(b/2) * b1 - mac.cRoot - yInter)
    return cy


intClDeltTab = []
for i in range(0, int(b/2)):
    intClDelt = findCY(i + length) * 0.5 * (i + length)**2 - findCY(i) * 0.5 * (i)**2
    intClDeltTab.append(intClDelt)

intClPTab = []
for i in range(0, int(b/2)):
    intClP = findCY(i + length) * (1/3) * (i + length)**3 - findCY(i) * (1/3) * (i)**3
    intClPTab.append(intClP)

Ptab = []
for i in range(len(intClDeltTab)):
    clDelta = (2 * clAlpha * tau)/(sRef * b) * intClDeltTab[i]
    clP = (-4 * (clAlpha + cd0))/(sRef * b**2) * intClPTab[i]
    P = -clDelta/clP * deltaA * (2 * velocity)/b
    Ptab.append(P)

difTab = []
for j in range(len(Ptab)):
    dif = Ptab[j] - Pideal
    difTab.append(dif)

bVal = difTab.index(min(difTab))