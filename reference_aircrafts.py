import pandas as pd
import numpy as np

# Column names:
# Company                                   0
# Model                                     1
# Max Payload [kg]                          2
# MTOM [kg]	OEM [kg]                        3
# Range [km]                                4
# Ferry range [km]                          5
# Take-off Dist [m]                         6
# Landing Dist [m]                          7
# Thrust per engine [N]                     8
# Number fo engines                         9
# Total Thrust [N]                          10
# Wing Surface Area [m²]                    11
# Aspect Ratio                              12
# Taper ratio                               13
# Sweep at 1/4 chord [deg]                  14
# Vertical Tail Surface Area [m²]           15
# Horizontal Tail Surface Area [m²]         16
# Cruise [Mach]                             17
# At alt. [m]                               18
# Span[m]                                   19

df = pd.read_excel("Reference_aircraft.xlsx", sheet_name="Sheet 1")

print(df.iloc[0:5, 1:3])
