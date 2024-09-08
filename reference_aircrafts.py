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

df = pd.read_excel("Reference_aircraft.xlsx", sheet_name="Sheet 1")

print(df.iloc[:, [1, 12, 13]])
