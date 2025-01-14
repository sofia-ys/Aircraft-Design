import math as m

def moments_of_inetria_L_stringer(height, width, thickness): # The reference x coordinate is the left side of the L and the reference y coordinate is the bottom of the L
    y = ((((height - thickness)/2 + thickness)*(height - thickness)*thickness + thickness / 2 * width * thickness)
         / ((height - thickness)*thickness + width * thickness))
    x = ((thickness / 2 * (height - thickness) * thickness + width / 2 * width * thickness)
         / ((height - thickness)*thickness + width * thickness))
    I_xx = ((thickness * height ** 3) / 12 + ((width - thickness) * thickness ** 3) / 12 +
            (height / 2 - y) ** 2 * height * thickness + (thickness / 2 - y) ** 2 * (width - thickness) * thickness)
    return I_xx

def A (height, width, thickness):
    return width * thickness + (height - thickness) * thickness

def calc_crit_sigma(K,E,I,A,L):
    I = I*10**(-12)
    A = A*10**(-6)
    return (K * m.pi**(2) * E * I)/(A * L**2)

print("Design 2 =", round(calc_crit_sigma(4, 72.4 * 10**9, moments_of_inetria_L_stringer(83,53.3,3), A(83,53.3,3), 2)/1000000,2), "MPa") # 2m is the shortest stinger
print("Design 1,3 =", round(calc_crit_sigma(4, 72.4 * 10**9, moments_of_inetria_L_stringer(63,40.3,3), A(63,40.3,3), 2)/1000000,2), "MPa") # 2m is the shortest stringer