from Drag import *
import math as m

b = 41
b_ref = 1.905
sweep_half = Sweep_quater
n_ult = 1.5*2.5
kw = 6.67e-3
b_s = b/(m.cos(sweep_half))
t_r = Chord_root*t_c
ZFW = 130000


Wing_mass = (kw * (b_s ** 0.75)) * (1 + m.sqrt(b_ref / b_s) * (n_ult ** 0.55) * ((b_s / t_r) / (ZFW / S_wing)) ** 0.30) * ZFW
print(Wing_mass)