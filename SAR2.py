import math
S = 173.77  # wing area m^2
AR = 10# aspect ratio
b = math.sqrt(AR*S)  # wing span m
sweep_quarter = 0.537  # wing sweep rad
C_D0 = 0.01589727272
CL= 0.454
v_cruise = 256.4704663921364
B= 11
C_T= 22*(B**-0.19)*(1*(10**-6))

sweep_quarter = 0.537
sweep_LE = 0.5871613666551182
Cr = 2 * math.sqrt(AR * S) * (math.tan(sweep_LE) - math.tan(sweep_quarter)) + (S / (math.sqrt(AR * S)))
Taper_ratio = ((2 * S) / (Cr * math.sqrt(AR * S))) - 1
Ctip = Cr * Taper_ratio
Lambda_half = math.atan(math.tan(sweep_LE) - (0.5 * (2 * cRoot / b) * (1 - taper)))
#Lambda_05c = 0.48689
e = 2 / (2 - AR + math.sqrt(4 + AR**2 * (1 + math.tan(Lambda_half)**2)))
L= 117604*0.9*9.80665
D_cruise = (4 * L) / (3 * math.sqrt((math.pi * AR * e) / (3 * C_D0)))
SAR= v_cruise/(D_cruise*C_T)
print(D_cruise)
print(C_T)
print(SAR)

print(cTip)
