import math as m



K = 0 #𝐾 = 1 if both endsare pinned, 𝐾 = 4 if both ends are clamped; 𝐾 = 1/4 if one end is fixed and one end is free; 1/√𝐾 = 0.7 if one end is pinned and one end is free.
L = 0
E = 72.4 * 10**9
A = 0


def calc_crit_o(K,E,I,A,L):
    E = E*10**(-12)
    A = A*10^(-6)
    return (K*m.pi*E*I)/(A*L**2)

print("Tall = ", calc_crit_o(0, E, 125532, 300, ))