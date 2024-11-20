import input_xflr_data as func
import matplotlib.pyplot as plt
import numpy as np
from scipy.integrate import quad

shear0 = list(range(32))
shear10 = list(range(32))
shear0[0] = 0
shear10[0] = 0
#yaxis=list(range(32))
xaxis = [i * 0.59 for i in range(len(shear0))]
x2axis = [j * 0.59 for j in range(len(shear0))]
print(func.get_cl(-15.226, 10))

for i in range(31):
    L_sec = 0.5*1.225 * 0.3589*(256**2)*func.get_cl(-17.7097+i*0.59, 0)*func.get_chord(-17.7097+i*0.59, 0)
    shear0[i+1]= shear0[i]+ L_sec*0.59

for j in range(31):
    L_sec_1 = 0.5*1.225 * 0.3589*(256**2)*func.get_cl(-17.7097+j*0.59, 10)*func.get_chord(-17.7097+j*0.59, 10)
    shear10[j+1]= shear10[j]+ L_sec_1*0.59

shear_reversed0 = shear0[::-1]
shear_reversed10 = shear10[::-1]
print(shear_reversed0)

plt.plot(xaxis, shear_reversed0, marker='o', linestyle='-', color='b')
plt.plot(x2axis, shear_reversed10,marker='o', linestyle='-', color='b')
plt.grid(True)
plt.show()

def L_sectional(x):
    # Constants used in the equation
    term1 = 0.5 * 1.225 * 0.3589 * (256**2)
    
    # Using x instead of j in the function
    cl = func.get_cl(x, 0)
    chord = func.get_chord(x, 0)
    
    return term1 * cl * chord

x_start = -17.7097
x_end = -17.7097 + 30 * 0.59 

result, error = quad(L_sectional, x_start, x_end)

# Print the result
print(f"Integral of L_sec(x) from {x_start} to {x_end} is: {result}")
print(f"Estimated error in the integral: {error}")