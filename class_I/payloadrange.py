import matplotlib.pyplot as plt
import pandas as pd
import numpy as np

# values
rangeHarmonic = 9545 # [km] at 18960 [kg]
rangeMTOW = 11716 # [km] at a payload of 8531 [kg]
rangeFerry = 12697 # [km]
payloadMax = 18960 # [kg]
payloadMTOW = 8531 # [kg]
payloadMin = 0 # [kg]

# graph segments
x1 = [0, rangeHarmonic]
y1 = [payloadMax, payloadMax]
x2 = [rangeHarmonic, rangeMTOW]
y2 = [payloadMax, payloadMTOW]
x3 = [rangeMTOW, rangeFerry]
y3 = [payloadMTOW, 0]

# graph plotting
plt.plot(x1, y1, color="blue")
plt.plot(x2, y2, color="blue")
plt.plot(x3, y3, color="blue")
plt.xlabel("Range [km]")
plt.ylabel("Payload weight [kg]")
plt.show()

# design mission selection point