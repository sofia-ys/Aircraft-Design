import math
import scipy as sp
from scipy import interpolate
import Ixx

age = [18,21,25,30,36,44,51,59,68]
pay = [27,33,38,45,55,65,80,100,120]

f = sp.interpolate.interp1d(age,pay,kind="previous",fill_value="extrapolate")
g = sp.interpolate.interp1d(age,pay,kind="next",fill_value="extrapolate")