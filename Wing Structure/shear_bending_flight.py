import numpy as np
import matplotlib.pyplot as plt
import input_xflr_data as inp
import constants as ct
from scipy.interpolate import interp1d
from scipy.optimize import fsolve

def lift_distribution(density, airspeed, alpha, span, M, num_points=1000):
    # Create an array of spanwise positions from root (0) to tip (span)
    x_vals = np.linspace(0, span, num_points)
    lift_vals = np.zeros(num_points)

    # Calculate the lift per unit length at each spanwise point
    for i, x in enumerate(x_vals):
        c = inp.get_chord(x,alpha)  # Local chord length
        cl_local = inp.get_cl(x,alpha)/((1-M**2)**(0.5))  # Local coefficient of lift
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
density = 0.4416  # kg/m^3 (air density at sea level)
airspeed = 256 # m/s (airspeed)
M = 0.85
alpha = 2 # degrees (angle of attack)
span = 17.7  # meters (wing span)
engine_position = 6.2  # meters from the center (location of the engine) 35% of b/2
engine_weight = 3008  # kg (weight of the engine)
g = 9.81 # m/s^2 gravitational acceleration
n = -1 # load factor
f_fuel = 0.8 # fraction of max fuel (between 0-1)
f_structure = 0.165 # (weight of structure)/(weight of max loaded fuel)

# Get lift distribution
x_vals, lift_vals = lift_distribution(density, airspeed, alpha, span, M)
# Plot the lift distribution
#plot_lift_distribution(x_vals, lift_vals)

def shear_force_distribution(x_vals, lift_vals, engine_position, engine_weight, load_factor, no_fuel_contribution = 0):
    # Convert engine weight from kg to Newtons (multiply by gravitational acceleration)
    engine_force = engine_weight * g * load_factor
    
    fuel_frac = f_fuel
    if(no_fuel_contribution > 1e-3): #for avoiding memory bugs with pure 0 or 1
        fuel_frac = 0
        print('no fuel:')
    # Initialize shear force array
    shear_force_vals = np.zeros(len(x_vals))
    
    # Calculate shear force at each spanwise point, starting from the tip towards the root
    total_lift = 0.0
    total_distributed_load = 0.0
    for i in reversed(range(len(x_vals))):
        # Calculate distributed load at current point
        distributed_load = - (-87.186 * x_vals[i] + 1546.67) *  g * load_factor * (fuel_frac + f_structure)
        total_distributed_load += distributed_load * (x_vals[1] - x_vals[0])
        
        # Accumulate lift contributions, account for the load factor!
        total_lift += lift_vals[i] * (x_vals[1] - x_vals[0]) * load_factor
        
        # Calculate shear force including engine force and distributed load
        if x_vals[i] <= engine_position:
            shear_force_vals[i] = total_lift + total_distributed_load - engine_force
        else:
            shear_force_vals[i] = total_lift + total_distributed_load
    return shear_force_vals

def plot_shear_force_distribution(x_vals, shear_force_vals, load_factor = 1):
    plt.figure()
    plt.plot(x_vals, shear_force_vals, label='Shear Force Distribution', color='r')
    plt.xlabel('Spanwise Position (m)')
    plt.ylabel('Shear Force (N)')
    plt.title('Shear Force Distribution along the Wing')
    plt.legend()
    plt.grid(which='major', linestyle='-', linewidth=0.7)
    plt.xticks(np.arange(0, 18.5, 1))  # Denser x-axis ticks
    if(load_factor < 0):
        plt.yticks(np.arange(round(min(shear_force_vals),-5), round(max(shear_force_vals) + max(shear_force_vals)/10,-4), -round(min(shear_force_vals)/10,-4)))  # Denser y-axis ticks
    else:
        plt.yticks(np.arange(0, round(max(shear_force_vals) + max(shear_force_vals)/10,-4), round(max(shear_force_vals)/10,-4)))  # Denser y-axis ticks
    plt.show()

# Calculate shear force distribution
shear_force_vals = shear_force_distribution(x_vals, lift_vals, engine_position, engine_weight, n)
# Plot the shear force distribution
plot_shear_force_distribution(x_vals, shear_force_vals, n)

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

# A function to get the bending moment in flight at any span location and any loading factor
def getBendingMomentFlight(y, load_factor):
    s_f_values = shear_force_distribution(x_vals, lift_vals, engine_position, engine_weight, load_factor)
    b_m_values = bending_moment_distribution(x_vals, s_f_values)

    moment_function = interp1d(x_vals, b_m_values, kind='linear', fill_value="extrapolate")
    return moment_function(y)

def plot_bending_moment_distribution(x_vals, bending_moment_vals, load_factor = 1):
    plt.figure()
    plt.plot(x_vals, bending_moment_vals, label='Bending Moment Distribution', color='b')
    plt.xlabel('Spanwise Position (m)')
    plt.ylabel('Bending Moment (Nm)')
    plt.title('Bending Moment Distribution along the Wing at n = ' + str(load_factor))
    plt.legend()
    plt.grid(which='major', linestyle='-', linewidth=0.7)
    plt.xticks(np.arange(0, 18.5, 1))  # Denser x-axis ticks
    if(load_factor < 0):
        plt.yticks(np.arange(round(min(bending_moment_vals),-5), round(max(bending_moment_vals) + max(bending_moment_vals)/10,-5), -round(min(bending_moment_vals)/10,-5)))  # Denser y-axis ticks
    else:
        plt.yticks(np.arange(0, round(max(bending_moment_vals) + max(bending_moment_vals)/10,-5), round(max(bending_moment_vals)/10,-5)))  # Denser y-axis ticks
    plt.show()

# Calculate bending moment distribution
bending_moment_vals = bending_moment_distribution(x_vals, shear_force_vals)
# Plot the bending moment distribution
plot_bending_moment_distribution(x_vals, bending_moment_vals, n)

# Calculate total lift by integrating the lift distribution
total_lift = np.trapz(lift_vals, x_vals)

# Print the total lift
print(f"Total Lift: {total_lift:.2f} N")

# Function to calculate the difference between calculated and target lift
def lift_error(alpha, density, airspeed, span, M, target_lift, num_points=1000):
    # Get lift distribution
    x_vals, lift_vals = lift_distribution(density, airspeed, alpha, span, M, num_points)

    # Calculate total lift by integrating the lift distribution
    total_lift = np.trapz(lift_vals, x_vals)

    # Calculate the difference between target lift and calculated lift
    return total_lift - target_lift

# Function to find angle of attack for a given target lift
def find_angle_of_attack(density, airspeed, target_lift, span, M, alpha_guess=2):
    # Use fsolve to find the alpha that gives the target lift
    alpha_solution = fsolve(
        lift_error, alpha_guess, args=(density, airspeed, span, M, target_lift)
    )
    return alpha_solution[0]

# Example usage
if __name__ == "__main__":
    # Given parameters
    density = 0.4416  # kg/m^3 (air density)
    airspeed = 256  # m/s (airspeed)
    span = 17.7  # meters (wing span)
    M = 0.85  # Mach number
    target_lift = 848260.89 # Desired total lift in Newtons (modify as needed)S

    # Find the angle of attack for the given target lift
    alpha = find_angle_of_attack(density, airspeed, target_lift, span, M)

    # Print the result
    print(f"Required angle of attack: {alpha:.2f} degrees")