import math as m



K = 0 #𝐾 = 1 if both endsare pinned, 𝐾 = 4 if both ends are clamped; 𝐾 = 1/4 if one end is fixed and one end is free; 1/√𝐾 = 0.7 if one end is pinned and one end is free.
L = 0
E = 72.4 * 10**9
A = 0


def moments_of_inetria_L_stringer(): # The reference x coordinate is the left side of the L and the reference y coordinate is the bottom of the L
    height = 83
    width = 53.3
    thickness = 3
    y = ((((height - thickness)/2 + thickness)*(height - thickness)*thickness + thickness / 2 * width * thickness)
         / ((height - thickness)*thickness + width * thickness))
    x = ((thickness / 2 * (height - thickness) * thickness + width / 2 * width * thickness)
         / ((height - thickness)*thickness + width * thickness))
    I_xx = ((thickness * height ** 3) / 12 + ((width - thickness) * thickness ** 3) / 12 +
            (height / 2 - y) ** 2 * height * thickness + (thickness / 2 - y) ** 2 * (width - thickness) * thickness)
    return I_xx

print(moments_of_inetria_L_stringer())

def calc_crit_o(K,E,I,A,L):
    E = E*10**(-12)
    A = A*10^(-6)
    return (K*m.pi*E*I)/(A*L**2)

print("Tall = ", calc_crit_o(0, E, 125532, 300, ))