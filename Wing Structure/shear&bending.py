import input_xflr_data as func
import matplotlib.pyplot as plt
import numpy as np

shear = list(range(32))
shear[0] = 0
#yaxis=list(range(32))
xaxis = [i * 0.59 for i in range(len(shear))]

for i in range(31):
    L_sec = 0.5*1.225*100*func.get_cl(-17.7097+i*0.59, 0)*func.get_chord(-17.7097+i*0.59, 0)
    shear[i+1]= shear[i]+ L_sec*0.59

shear_reversed = shear[::-1]
print(shear_reversed)

plt.plot(xaxis, shear_reversed, marker='o', linestyle='-', color='b')
plt.grid(True)
plt.show()