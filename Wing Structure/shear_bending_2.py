import numpy as np
import matplotlib.pyplot as plt
import input_xflr_data as inp
import constants as ct


def lift_distribution(density, airspeed, alpha, span, num_points=100):
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
    plt.plot(x_vals, lift_vals, label='Lift Distribution')
    plt.xlabel('Spanwise Position (m)')
    plt.ylabel('Lift per Unit Length (N/m)')
    plt.title('Lift Distribution along the Wing')
    plt.legend()
    plt.grid(True)
    plt.show()

# Given parameters
density = ct.densi  # kg/m^3 (air density at sea level)
airspeed = 10  # m/s (airspeed)
alpha = 0  # degrees (angle of attack)
span = 17.7  # meters (wing span)
engine_position = 9  # meters from the center (location of the engine)
engine_weight = 3008  # kg (weight of the engine)

# Get lift distribution
x_vals, lift_vals = lift_distribution(density, airspeed, alpha, span)

# Plot the lift distribution
#plot_lift_distribution(x_vals, lift_vals)


def shear_force_distribution(x_vals, lift_vals, engine_position, engine_weight):
    # Convert engine weight from kg to Newtons (multiply by gravitational acceleration)
    engine_force = engine_weight * 9.81

    # Initialize shear force array
    shear_force_vals = np.zeros(len(x_vals))

    # Calculate shear force at each spanwise point
    total_lift = 0.0
    for i in range(len(x_vals)):
        total_lift += lift_vals[i] * (x_vals[1] - x_vals[0])  # Accumulate lift contributions
        if x_vals[i] >= engine_position:
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