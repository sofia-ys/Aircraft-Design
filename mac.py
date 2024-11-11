import matplotlib.pyplot as plt
import math

# wing parameters
S = 173.77  # wing area m^2
b = 37.98  # wing span m
AR = 8.3  # aspect ratio
taper = 0.292  # taper ratio
cRoot = 7.08  # root chord m
cTip = 2.07  # tip chord m
sweep = 0.537  # wing sweep rad

def graph(line, colour):
    x, y = line
    plt.plot(x, y, color=colour)

def lineEq(x1, y1, x2, y2):
    m = (y2 - y1) / (x2 - x1)
    c = y1 - m * x1
    return m, c

# graph segments
root = ([0, 0], [(0.25*cRoot), (-0.75*cRoot)])
rootEx = ([0, 0], [(-0.75*cRoot), (-0.75*cRoot - cTip)])
quarterC = ([0, b/2], [0, (-(b/2)*math.tan(sweep))])
halfC = ([0, b/2], [(-0.25*cRoot), (-(b/2)*math.tan(sweep) - 0.25*cTip)])
tip = ([b/2, b/2], [(-(b/2)*math.tan(sweep) + 0.25*cTip), (-(b/2)*math.tan(sweep) - 0.75*cTip)])
tipEx = ([b/2, b/2], [(-(b/2)*math.tan(sweep) + 0.25*cTip), (-(b/2)*math.tan(sweep) + 0.25*cTip + cRoot)])
leadingE = ([0, b/2], [(0.25*cRoot), (-(b/2)*math.tan(sweep) + 0.25*cTip)])
trailingE = ([0, b/2], [(-0.75*cRoot), (-(b/2)*math.tan(sweep) - 0.75*cTip)])
diagonal = ([0, b/2], [(-cTip - 0.75*cRoot), (-(b/2)*math.tan(sweep) + 0.25*cTip + cRoot)])

# graphing wing planform
graph(root, "black")
graph(rootEx, "#8ace00")
graph(quarterC, "#8ace00")
graph(tip, "black")
graph(tipEx, "#8ace00")
graph(leadingE, "black")
graph(trailingE, "black")
graph(diagonal, "#8ace00")
graph(halfC, "#8ace00")

# finding MAC
mHalf, cHalf = lineEq(halfC[0][0], halfC[1][0], halfC[0][1], halfC[1][1])
mDiagonal, cDiagonal = lineEq(diagonal[0][0], diagonal[1][0], diagonal[0][1], diagonal[1][1])
xInter = (cDiagonal - cHalf) / (mHalf - mDiagonal)
yInter = mHalf * xInter + cHalf

MAC = ([xInter, xInter], [(yInter + 0.5 * cRoot), (yInter - 0.5 * cRoot)])

graph(MAC, "#8ace00")

print(f"MAC: ({xInter:.2f}, {yInter:.2f})")
plt.show()