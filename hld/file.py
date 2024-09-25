<<<<<<< HEAD
import math
from matplotlib import pyplot
import numpy as np

deltaC_L = 0.52 # how much do we need to increase the C_L with HLDs

LE_sweep = 2

fowlerDeflection = math.radians(40)
slottedDeflection = math.radians(40)

deltac_cf_fowler = 0.62
deltac_cf_slotted = 0.31

cf_over_c = 0.1 #this value will be iterated - range from 0.1 to 0.4

#Fowler
delta_c_c_fowler = cf_over_c * deltac_cf_fowler
cdash_c_fowler = 1 + delta_c_c_fowler
#Slotted
delta_c_c_slotted = cf_over_c * deltac_cf_slotted
cdash_c_slotted = 1 + delta_c_c_slotted

delta_Clmax_fowler = 1.3 * cdash_c_fowler
delta_Clmax_slotted = 1.3

=======
test
>>>>>>> db7651c07f14a57bf2a2025727087ea31b418f80
