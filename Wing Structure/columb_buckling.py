from Ixx import Ixxfinal
from shear_bending_flight import getBendingMomentFlight
import matplotlib.pyplot as plt
import constants as con

b = con.b-8 #-8 is so I can see the problematic begining of the wing
y = 0
step = 0.1
y_axis = []
design_choic1 = 4

critical_s = 524.25*10**6 # For designs 2 & 4
#critical_s = 298.87*10**6 # For Designs 1 & 3


def bending_moment(y):
    return getBendingMomentFlight(y, 2.5)

stresses = []
while y<=b/2:
    stress = (bending_moment(y)*(0.19-0.01*y))/Ixxfinal(design_choic1,y)
    stresses.append(critical_s/stress)
    y_axis.append(y)
    y += step
plt.figure()
print(min(stresses))
min_y = min(stresses)
plt.axhline(min_y, color='red', linestyle='--', label=f"Min y: {min_y:.2f}")
plt.text(stresses[0] + 10, min_y, f"Min y: {min_y:.2f}", color="red", verticalalignment='bottom')

plt.plot(y_axis, stresses, label="stress_column", color='blue')
plt.xlabel('Wingspan [m]')
plt.ylabel('Safety Margin [-]')
plt.title('Stringer Column Buckling')
plt.legend()
plt.show()
