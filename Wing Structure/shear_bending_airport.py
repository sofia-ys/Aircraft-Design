import numpy as np
import matplotlib.pyplot as plt

def distributed_load(x):
    # Distributed load function f(x) = 15172.8 - 855.3 * x
    return 15172.8 - 855.3 * x

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

def plot_shear_force_distribution(x_vals, shear_force_vals):
    plt.figure()
    plt.plot(x_vals, shear_force_vals, label='Shear Force Distribution', color='r')
    plt.xlabel('Spanwise Position (m)')
    plt.ylabel('Shear Force (N)')
    plt.title('Shear Force Distribution along the Wing')
    plt.legend()
    plt.grid(True)
    plt.show()

# Given parameters
span = 17.7  # meters (wing span)
engine_position = 9  # meters from the center (location of the engine)
engine_weight = 3008  # kg (weight of the engine)
landing_gear_position = 4.07
landing_gear_force = 358139
# Create an array of spanwise positions from root (0) to tip (span)
x_vals = np.linspace(0, span, 1000)

# Calculate the distributed load at each spanwise point
load_vals = distributed_load(x_vals)

# Calculate shear force distribution
shear_force_vals = shear_force_distribution(x_vals, load_vals, engine_position, engine_weight)

# Plot the shear force distribution
plot_shear_force_distribution(x_vals, shear_force_vals)
