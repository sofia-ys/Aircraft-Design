import math as m
import scipy as sp
from scipy import integrate
from extra_constants import *
from input_xflr_data import get_cm_airf, get_chord, get_cl
from input_xflr_data import *

angl = 0
# Input data
y = y_new # Placeholder for spanwise locations
cm = get_cm_airf(y_new, angl)  # Pitching moment coefficient
c = get_chord(y_new, angl)  # Placeholder for chord distribution
cl = get_cl(y_new, angl)  # Placeholder for lift coefficient distribution

rho = 0.4
v = 100

q = 0.5*rho*v**2

L = cl*c*q


