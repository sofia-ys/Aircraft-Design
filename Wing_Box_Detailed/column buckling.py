import math as m



K = 0 #𝐾 = 1 if both endsare pinned, 𝐾 = 4 if both ends are clamped; 𝐾 = 1/4 if one end is fixed and one end is free; 1/√𝐾 = 0.7 if one end is pinned and one end is free.

crit_o = (K*m.pi*E*I)/(A*L**2)
