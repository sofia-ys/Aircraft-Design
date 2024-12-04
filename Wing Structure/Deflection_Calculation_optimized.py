import numpy as np
import matplotlib.pyplot as plt
from scipy.integrate import cumulative_trapezoid
from Ixx import Ixxfinal
from shear_bending_flight import getBendingMomentFlight
import constants as con

# Constants
E = 72.4 * 10**9  # Young's modulus for the material (Pa)
b = con.b       # Wing span from constants

# Predefine functions for bending moment and moment of inertia
def bending_moment(y_vals):
    """Vectorized bending moment function."""
    return np.array([getBendingMomentFlight(y, -1) for y in y_vals])

def Ixx(y_vals):
    """Vectorized moment of inertia function."""
    return np.array([Ixxfinal(1, y) for y in y_vals])

def second_derivative_deflection(y_vals):
    """Calculate the second derivative of deflection."""
    return -bending_moment(y_vals) / (E * Ixx(y_vals))

def calculate_deflection_and_slope(y_vals, step):
    """Efficiently compute slope and deflection using cumulative integration."""
    second_deriv = second_derivative_deflection(y_vals)

    # Use cumulative trapezoidal integration for the first and second integrals
    slope = cumulative_trapezoid(second_deriv, y_vals, initial=0)
    deflection = cumulative_trapezoid(slope, y_vals, initial=0)
    return slope, deflection

# Main script
if __name__ == "__main__":
    step = 0.1  # Step size
    y_vals = np.arange(0, b / 2 + step, step)  # Define span positions

    # Calculate slope and deflection
    slope, deflection = calculate_deflection_and_slope(y_vals, step)

    # Plot results
    plt.figure(figsize=(10, 6))
    plt.plot(y_vals, slope, label="Slope", color="blue")
    plt.plot(y_vals, deflection, label="Deflection", color="green")
    plt.xlabel("Position along half-span (m)")
    plt.ylabel("Values")
    plt.title("Slope and Deflection along the Wing Span")
    plt.legend()
    plt.grid()
    plt.show()