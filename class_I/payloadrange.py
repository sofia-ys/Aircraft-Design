import matplotlib.pyplot as plt
import sys
import os

# Add the parent directory to sys.path
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

# importing aircraft data file
import aircraft_data as ad

# graph segments
segments = [
    ([0, ad.range_harmonic], [ad.payload_max, ad.payload_max]),
    ([ad.range_harmonic, ad.range_MTOW_full_fuel], [ad.payload_max, ad.payload_MTOW]),
    ([ad.range_MTOW_full_fuel, ad.range_ferry], [ad.payload_MTOW, 0])
    ]

# design mission selection point
designRange = ad.range_MTOW_full_fuel + (ad.range_harmonic - ad.range_MTOW_full_fuel)/2
designPayload = ad.payload_max - (ad.payload_max - ad.payload_MTOW)/2
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