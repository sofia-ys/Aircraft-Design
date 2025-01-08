from Ixx import Ixxfinal
from shear_bending_flight import getBendingMomentFlight
import scipy
import matplotlib.pyplot as plt
import constants as con


b = con.b-20 #-10 is so I can see the problematic begining of the wing


y = 0
step = 0.1


y_axis = []
design_choic1 = 1

critical_s = 2.18*10**6
def bending_moment(y):
    return getBendingMomentFlight(y, 2.5)
stresses = []
while y<=b/2:
    stress = (bending_moment(y)*(0.2-0.01*y))/Ixxfinal(design_choic1,y)
    stresses.append(critical_s/stress)
    y_axis.append(y)
    y += step
plt.figure()

plt.plot(y_axis, stresses, label="stress_column", color='blue')
plt.xlabel('wingspan')
plt.ylabel('safety margin')
plt.title('Column Buckling')
plt.legend()
plt.show()
