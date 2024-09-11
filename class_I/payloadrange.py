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
segments = [
    ([0, rangeHarmonic], [payloadMax, payloadMax]),
    ([rangeHarmonic, rangeMTOW], [payloadMax, payloadMTOW]),
    ([rangeMTOW, rangeFerry], [payloadMTOW, 0])
    ]

# design mission selection point
designx = rangeMTOW + (rangeHarmonic - rangeMTOW)/2
designy = payloadMax - (payloadMax - payloadMTOW)/2
designPoint = (designx, designy)

# graph plotting
def plotSegments(segments, designx, designy):
    for x, y in segments:
        plt.plot(x, y, color="#8ace00")
    plt.scatter(designx, designy, color="black")
    plt.xlabel("Range [km]")
    plt.ylabel("Payload weight [kg]")
    plt.show()

plotSegments(segments, designx, designy)