import numpy as np
import matplotlib.pyplot as plt

# Distributed load function
def distributed_load(x):
    # Distributed load function f(x) = 15172.8 - 855.3 * x
    return 15172.8 - 855.3 * x

# Shear force distribution function
def shear_force_distribution(x_vals, load_vals, engine_position, engine_weight):
    # Convert engine weight from kg to Newtons (multiply by gravitational acceleration)
    engine_force = engine_weight * 9.81
    
    # Initialize shear force array
    shear_force_vals = np.zeros(len(x_vals))
    
    # Calculate shear force at each spanwise point, starting from the tip towards the root
    total_load = 0.0
    for i in reversed(range(len(x_vals))):
        total_load += load_vals[i] * (x_vals[1] - x_vals[0])  # Accumulate load contributions
        if x_vals[i] <= landing_gear_position:
            shear_force_vals[i] = - total_load + landing_gear_force - engine_force
        elif x_vals[i] <= engine_position:
            shear_force_vals[i] = - total_load - engine_force    
        else:
            shear_force_vals[i] = - total_load
    
    return shear_force_vals

# Bending moment distribution function
def bending_moment_distribution(x_vals, shear_force_vals):
    # Initialize bending moment array
    bending_moment_vals = np.zeros(len(x_vals))
    
    # Integrate shear force to calculate bending moment, starting from the tip towards the root
    total_moment = 0.0
    for i in reversed(range(len(x_vals) - 1)):
        dx = x_vals[i+1] - x_vals[i]
        total_moment += shear_force_vals[i] * dx
        bending_moment_vals[i] = total_moment
    
    return bending_moment_vals

# Plotting shear force distribution
def plot_shear_force_distribution(x_vals, shear_force_vals):
    plt.figure()
    plt.plot(x_vals, shear_force_vals, label='Shear Force Distribution', color='r')
    plt.xlabel('Spanwise Position (m)')
    plt.ylabel('Shear Force (N)')
    plt.title('Shear Force Distribution along the Wing')
    plt.legend()
    plt.grid(True)
    plt.show()

# Plotting bending moment distribution
def plot_bending_moment_distribution(x_vals, bending_moment_vals):
    plt.figure()
    plt.plot(x_vals, bending_moment_vals, label='Bending Moment Distribution', color='b')
    plt.xlabel('Spanwise Position (m)')
    plt.ylabel('Bending Moment (Nm)')
    plt.title('Bending Moment Distribution along the Wing')
    plt.legend()
    plt.grid(True)
    plt.show()

# Given parameters
span = 17.7  # meters (wing span)
engine_position = 6.2  # meters from the center (location of the engine)
engine_weight = 3008  # kg (weight of the engine)
landing_gear_position = 4.07  # meters from the center
landing_gear_force = 358139  # Newtons

# Create an array of spanwise positions from root (0) to tip (span)
x_vals = np.linspace(0, span, 1000)

# Calculate the distributed load at each spanwise point
load_vals = distributed_load(x_vals)

# Calculate shear force distribution
shear_force_vals = shear_force_distribution(x_vals, load_vals, engine_position, engine_weight)

# Calculate bending moment distribution
bending_moment_vals = bending_moment_distribution(x_vals, shear_force_vals)

# Plot the shear force distribution
plot_shear_force_distribution(x_vals, shear_force_vals)

# Plot the bending moment distribution
plot_bending_moment_distribution(x_vals, bending_moment_vals)
