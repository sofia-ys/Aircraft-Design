import pandas as pd
import numpy as np

# Column names:
# Company                                   0
# Model                                     1
# Max Payload [kg]                          2
# MTOM [kg]	                                3
# OEM [kg]                                  4
# Range [km]                                5
# Ferry range [km]                          6
# Take-off Dist [m]                         7
# Landing Dist [m]                          8
# Thrust per engine [N]                     9
# Number fo engines                         10
# Total Thrust [N]                          11
# Wing Surface Area [m²]                    12
# Aspect Ratio                              13
# Taper ratio                               14
# Sweep at 1/4 chord [deg]                  15
# Vertical Tail Surface Area [m²]           16
# Horizontal Tail Surface Area [m²]         17
# Cruise [Mach]                             18
# At alt. [m]                               19
# Span[m]                                   20
# Swet/S                                    21
# Bypass ratio                              22
# Swet                                      23
#comment
df = pd.read_excel("Reference_aircraft.xlsx", sheet_name="Sheet 1")

#print(df.iloc[:, [15]])
array = df.to_numpy()
MTOM = array[:, 3]
W = []
for i in MTOM:
    W.append(i * 9.80665)
T = array[:, 11]
S = array[:, 12]
