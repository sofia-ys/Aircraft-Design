import numpy as np
import matplotlib.pyplot as plt
from scipy.integrate import cumulative_trapezoid
from Ixx import Ixxfinal
from shear_bending_flight import getBendingMomentFlight
import constants as con

# Constants
E = 72.4 * 10**9
b = con.b
def bending_moment(y_vals):
    return np.array([getBendingMomentFlight(y, -1) for y in y_vals])

def Ixx(y_vals):
    return np.array([Ixxfinal(4, y) for y in y_vals])

def second_derivative_deflection(y_vals):
    return -bending_moment(y_vals) / (E * Ixx(y_vals))

def calculate_deflection_and_slope(y_vals, step):
    second_deriv = second_derivative_deflection(y_vals)
    slope = cumulative_trapezoid(second_deriv, y_vals, initial=0)
    deflection = cumulative_trapezoid(slope, y_vals, initial=0)
    return slope, deflection


step = 0.1
y_vals = np.arange(0, b / 2 + step, step)
slope, deflection = calculate_deflection_and_slope(y_vals, step)
plt.figure(figsize=(10, 6))
plt.plot(y_vals, slope, label="Slope", color="blue")
plt.plot(y_vals, deflection, label="Deflection", color="green")
plt.xlabel("Position along half-span (m)")
plt.ylabel("Deflection (m)")
plt.title("Slope and Deflection along the Wing Span")
plt.legend()
plt.grid()
plt.show()

print(deflection)