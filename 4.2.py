#Calculation of Ixx
def Ixxcalculator (d1, d2, d3, d4, t1, t2, h):
    I = 1/12*d1**3*t1 + d1*t1*(d1/2-h) + 1*12*d3**3*t1