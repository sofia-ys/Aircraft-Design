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
root = ([0, 0], [(0), (-cRoot)])
rootEx = ([0, 0], [(-cRoot), (-cRoot - cTip)])
quarterC = ([0, b/2], [(-0.25*cRoot), (-(b/2)*math.tan(sweep) - 0.25*cRoot)])
halfC = ([0, b/2], [(-0.5*cRoot), (-(b/2)*math.tan(sweep) - 0.25*cTip - 0.25*cRoot)])
tip = ([b/2, b/2], [(-(b/2)*math.tan(sweep) + 0.25*cTip - 0.25*cRoot), (-(b/2)*math.tan(sweep) - 0.75*cTip - 0.25*cRoot)])
tipEx = ([b/2, b/2], [(-(b/2)*math.tan(sweep) + 0.25*cTip - 0.25*cRoot), (-(b/2)*math.tan(sweep) + 0.25*cTip + 0.75*cRoot)])
leadingE = ([0, b/2], [(0), (-(b/2)*math.tan(sweep) + 0.25*cTip - 0.25*cRoot)])
trailingE = ([0, b/2], [(-cRoot), (-(b/2)*math.tan(sweep) - 0.75*cTip - 0.25*cRoot)])
diagonal = ([0, b/2], [(-cTip -cRoot), (-(b/2)*math.tan(sweep) + 0.25*cTip + 0.75*cRoot)])

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
mHalf, cHalf = lineEq(halfC[0][0], halfC[1][0], halfC[0][1], halfC[1][1])  # finding the m and c values for the 1/2 chord line using the points
mDiagonal, cDiagonal = lineEq(diagonal[0][0], diagonal[1][0], diagonal[0][1], diagonal[1][1])  # finding m and c for diagonal
xMAC = (cDiagonal - cHalf) / (mHalf - mDiagonal)  # finding intersection x coordinate of the two lines

# getting the chord length of the MAC
mLE, cLE = lineEq(leadingE[0][0], leadingE[1][0], leadingE[0][1], leadingE[1][1]) 
mTE, cTE = lineEq(trailingE[0][0], trailingE[1][0], trailingE[0][1], trailingE[1][1]) 
yLE = mLE * xMAC + cLE  # finding the y coordinate of the MAC on the leading edge
yTE = mTE * xMAC + cTE  # y coord of MAC on TE

MAC = ([xMAC, xMAC], [(yLE), (yTE)])
graph(MAC, "#8ace00")

print(f"MAC: ({xMAC:.2f}, {(yLE):.2f})")
plt.show()
