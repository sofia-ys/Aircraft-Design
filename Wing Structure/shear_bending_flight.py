import numpy as np
import matplotlib.pyplot as plt
import input_xflr_data as inp
import constants as ct

def lift_distribution(density, airspeed, alpha, span, num_points=1000):
    # Create an array of spanwise positions from root (0) to tip (span)
    x_vals = np.linspace(0, span, num_points)
    lift_vals = np.zeros(num_points)

    # Calculate the lift per unit length at each spanwise point
    for i, x in enumerate(x_vals):
        c = inp.get_chord(x,alpha)  # Local chord length
        cl_local = inp.get_cl(x,alpha)  # Local coefficient of lift
        lift_vals[i] = 0.5 * density * airspeed**2 * c * cl_local

    return x_vals, lift_vals

def plot_lift_distribution(x_vals, lift_vals):
    plt.figure()
    plt.plot(x_vals, lift_vals, label='Lift Distribution', color='g')
    plt.xlabel('Spanwise Position (m)')
    plt.ylabel('Lift per Unit Length (N/m)')
    plt.title('Lift Distribution along the Wing')
    plt.legend()
    plt.grid(True)
    plt.show()

# Given parameters
density = 0.4436  # kg/m^3 (air density at sea level)
airspeed = 256 # m/s (airspeed)
alpha = 2 # degrees (angle of attack)
span = 17.7  # meters (wing span)
engine_position = 6.21  # meters from the center (location of the engine) 35% of b/2
engine_weight = 3008  # kg (weight of the engine)

# Get lift distribution
x_vals, lift_vals = lift_distribution(density, airspeed, alpha, span)

# Plot the lift distribution
plot_lift_distribution(x_vals, lift_vals)

def shear_force_distribution(x_vals, lift_vals, engine_position, engine_weight):
    # Convert engine weight from kg to Newtons (multiply by gravitational acceleration)
    engine_force = engine_weight * 9.81
    
    # Initialize shear force array
    shear_force_vals = np.zeros(len(x_vals))
    
    # Calculate shear force at each spanwise point, starting from the tip towards the root
    total_lift = 0.0
    for i in reversed(range(len(x_vals))):
        total_lift += lift_vals[i] * (x_vals[1] - x_vals[0])  # Accumulate lift contributions
        if x_vals[i] <= engine_position:
            shear_force_vals[i] = total_lift - engine_force
        else:
            shear_force_vals[i] = total_lift
    
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

# Calculate shear force distribution
shear_force_vals = shear_force_distribution(x_vals, lift_vals, engine_position, engine_weight)
# Plot the shear force distribution
plot_shear_force_distribution(x_vals, shear_force_vals)

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

def plot_bending_moment_distribution(x_vals, bending_moment_vals):
    plt.figure()
    plt.plot(x_vals, bending_moment_vals, label='Bending Moment Distribution', color='b')
    plt.xlabel('Spanwise Position (m)')
    plt.ylabel('Bending Moment (Nm)')
    plt.title('Bending Moment Distribution along the Wing')
    plt.legend()
    plt.grid(True)
    plt.show()

# Calculate bending moment distribution
bending_moment_vals = bending_moment_distribution(x_vals, shear_force_vals)
# Plot the bending moment distribution
plot_bending_moment_distribution(x_vals, bending_moment_vals)
