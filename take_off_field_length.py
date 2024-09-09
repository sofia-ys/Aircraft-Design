from math import sqrt, pow, pi
import matplotlib.pyplot as plt

w_s = [0]
takeoff_dist = 3048
T = 288.15
p = 101325
rho = 1.225
Cl = 2
Cl2 = Cl/1.13/1.13
e = 0.8116
v = []
T_t = []
p_t = []
delta_t = []
alpha_t = []
theta_t = []
t_w = []
a = 340.3
m = []
gamma = 1.4
B = 11
k_t = 0.85
theta_t_break = 1.08
g = 9.80665
h2 = 11
AR = 8
for i in range(1,101) :
    w_s.append(w_s[i-1] + 100)
for i in range(0,101) :
    v.append(sqrt(w_s[i] * 2 / rho / Cl2))
    m.append(v[i] / a)
    T_t.append(T * (1 + (gamma - 1) / 2 * m[i] * m[i]))
    p_t.append(p* pow( (1 + (gamma - 1) / 2 * m[i] * m[i]), gamma / (gamma - 1)))
    delta_t.append(p_t[i]/p)
    theta_t.append(T_t[i]/T)
    if theta_t[i] <= theta_t_break:
        alpha_t.append(delta_t[i] * (1 - (0.43 + 0.014 * B) * sqrt(m[i])))
    else :
        alpha_t.append(delta_t[i] * (1 - (0.43 + 0.014 * B) * sqrt(m[i]) - 3 * (theta_t[i] - theta_t_break) / (1.5 + m[i])))
    t_w.append(1.15 * alpha_t[i] * sqrt(2 * w_s[i] / takeoff_dist / k_t / rho / g / pi / AR / e) + 2 * 4 * h2 / takeoff_dist)
plt.plot(w_s, t_w, color='blue')
plt.title('Takeoff Field Length WP1')
plt.show()



