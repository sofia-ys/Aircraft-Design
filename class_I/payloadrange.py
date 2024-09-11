import matplotlib.pyplot as plt

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
designRange = rangeMTOW + (rangeHarmonic - rangeMTOW)/2
designPayload = payloadMax - (payloadMax - payloadMTOW)/2
designPoint = (designRange, designPayload)  # mission design point: range, payload

# graph plotting
def plotSegments(segments, designx, designy):
    for x, y in segments:
        plt.plot(x, y, color="#8ace00")
    plt.scatter(designx, designy, color="black")
    plt.xlabel("Range [km]")
    plt.ylabel("Payload weight [kg]")
    plt.title("Payload-Range Diagram")
    plt.show()

plotSegments(segments, designRange, designPayload)
print(designPoint)