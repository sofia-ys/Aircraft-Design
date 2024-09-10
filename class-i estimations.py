import matplotlib.pyplot as plt
import pandas as pd
import numpy as np

ra = pd.read_excel("Reference_aircraft.xlsx", sheet_name="Sheet 1")

''' 1. finding the MTOM - OEM relationship '''
MTOM = ra.iloc[:, 3]
OEM = ra.iloc[:, 4]

plt.scatter(MTOM, OEM, color="black", label="Data points")  # scatter plot

# finding line of best fit
coefficients = np.polyfit(MTOM, OEM, 1)  # fits a polynomial of first degree to the relationship between MTOM and OEM
linearReg = np.polyval(coefficients, MTOM)  # generates a y value according to the linear reg derived for every x value MTOM
a = coefficients[0]  # coefficients to determine the MTOM-OEM relation, SLIDE 15
b = coefficients[1]

# finding R**2
res = np.sum((OEM - linearReg)**2)
tot = np.sum((OEM - np.mean(OEM))**2)
rSqr = 1 - (res/tot)

plt.plot(MTOM, linearReg, color="#8ace00", label=f"Linear regression (R² = {rSqr:.2f})")  # plotting line of best fit

plt.xlabel("Maximum Take-Off Mass (MTOM) [kg]")
plt.ylabel("Operating Empty Mass (OEM) [kg]")

plt.legend()
plt.show()


''' 2. estimate drag polar and specific fuel consumption'''

# drag polar slides 29 - 36


''' 3. estimate/calculate fuel fractions'''

# fuel weight estimation slide 16 - 28

# fuel estimation slides 37 - 44


'''4. compute MTOW, OEW and W_fuel'''

# calculate empty weight from W_TO slide 15

# examples on procedure slides 45 - 54