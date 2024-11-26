import math
import scipy as sp
from scipy import interpolate
import matplotlib as plt
import draft


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

def
f = sp.interpolate.interp1d(span_n1,n1,kind="previous",fill_value="extrapolate")
g = sp.interpolate.interp1d(span_n2,n2,kind="previous",fill_value="extrapolate")
b = 40 #wingspan
Ixx_tab=[]
y_tab = []
step = 0.01
for i in range (0,b / (step*2)):
    Ixx_tab.append(Ixx)