import math
import scipy as sp
from scipy import interpolate
import Ixx


#Design 1
span_n1 = [18,21,25,30,36,44,51,59,68]
n1 = [18,21,25,30,36,44,51,59,68]
span_n2 = [18,21,25,30,36,44,51,59,68]
n2 = [27,33,38,45,55,65,80,100,120]
span_t1 = [18,21,25,30,36,44,51,59,68]
t1 = [18,21,25,30,36,44,51,59,68]
span_t2 = [18,21,25,30,36,44,51,59,68]
t2 = [18,21,25,30,36,44,51,59,68]
span_An = [18,21,25,30,36,44,51,59,68]
An = [18,21,25,30,36,44,51,59,68]

#Design 2

#Design 3

n1_inter = sp.interpolate.interp1d(span_n1,n1,kind="previous",fill_value="extrapolate")
n2_inter = sp.interpolate.interp1d(span_n2,n2,kind="previous",fill_value="extrapolate")
t1_inter = sp.interpolate.interp1d(span_t1,t1,kind="previous",fill_value="extrapolate")
t2_inter = sp.interpolate.interp1d(span_t2,t2,kind="previous",fill_value="extrapolate")
An_inter = sp.interpolate.interp1d(span_An,An,kind="previous",fill_value="extrapolate")