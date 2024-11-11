import math
from matplotlib import pyplot
import numpy as np
import scipy.integrate as integrate

deltaC_L = 0.57 # how much do we need to increase the C_L with HLDs
root_chord = 7.08
b = 38
tr = 0.292
LE_sweep = 2
S = 174.8

fowlerDeflection = math.radians(40)
slottedDeflection = math.radians(40)

deltac_cf_fowler = 0.62
deltac_cf_slotted = 0.31

cf_over_c = 0.4 #this value will be iterated - range from 0.1 to 0.4

#Fowler
delta_c_c_fowler = cf_over_c * deltac_cf_fowler
cdash_c_fowler = 1 + delta_c_c_fowler
#Slotted
delta_c_c_slotted = cf_over_c * deltac_cf_slotted
cdash_c_slotted = 1 + delta_c_c_slotted

delta_Clmax_fowler = 1.3 * cdash_c_fowler
delta_Clmax_slotted = 1.3

def sweep(x_c):
    return(math.atan( math.tan(0.537) + ((2*root_chord)/b) * (1-tr) * ((1/4)-x_c) ) )
print(sweep(0))
sweep_hinge_fowler = sweep(1 - cf_over_c)

# Defining the function to integrate
def function_to_integrate(x, LE_sweep, TE_sweep, c_r):
    return (-np.tan(LE_sweep) * x + c_r) - (-np.tan(TE_sweep) * x)

# Define the integration bounds and parameters
LE_sweep = sweep(0)  # Example angle in radians
TE_sweep = sweep(1)  # Example angle in radians
c_r = 7.08  # Example value for c_r
b = 38   # Upper bound for integration

#result, error = integrate.quad(function_to_integrate, 0, b/2, args=(LE_sweep, TE_sweep, c_r)) #to test the integration

#Fowler
S_wf_fowler = (deltaC_L * S)/(2*(0.9 * delta_Clmax_fowler * math.cos(sweep(1 - cf_over_c)) - deltaC_L * (cdash_c_fowler - 1)))

areaHLD_fowler = 0
step = 0.01
upperBound_fowler = 0

while(areaHLD_fowler < S_wf_fowler):
    upperBound_fowler = upperBound_fowler + step
    areaHLD_fowler = integrate.quad(function_to_integrate, 0, upperBound_fowler, args=(LE_sweep, TE_sweep, c_r))[0]

#Slotted flap
S_wf_slotted = (deltaC_L * S/2)/(0.9 * delta_Clmax_slotted * math.cos(sweep(1 - cf_over_c)))

areaHLD_slotted = 0
upperBound_slotted = 0

while(areaHLD_slotted < S_wf_slotted):
    upperBound_slotted = upperBound_slotted + step
    areaHLD_slotted = integrate.quad(function_to_integrate, 0, upperBound_slotted, args=(LE_sweep, TE_sweep, c_r))[0]

print('S:')
print(upperBound_slotted, areaHLD_slotted, cf_over_c)
print('F:')
print(upperBound_fowler, areaHLD_fowler, cf_over_c)