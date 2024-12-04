from shear_bending_flight import *
case_airspeeds = [
    73.00, 73.00,
    122.89, 122.89,
    49.2, 49.2,
    81.92, 81.92,
    57, 57,
    95, 95,
    115.42, 115.42,
    194.3, 194.3,
    77.7, 77.7,
    129.5, 129.5,
    90.125, 90.125,
    150.13, 150.13,
    256.6, 256.6, 256.6, 256.6, 256.6, 256.6,
    256.5, 256.5,
    256.6, 256.6, 256.6, 256.6,
    313, 277.7, 313, 277.7, 313, 277.7
]

case_weights = [
    86469, 86469, 86469, 86469,  # MTOW
    38424, 38424, 38424, 38424,  # OEW
    52169, 52169, 52169, 52169,  # No Fuel
    86469, 86469, 86469, 86469,  # MTOW
    38424, 38424, 38424, 38424,  # OEW
    52169, 52169, 52169, 52169,  # No Fuel
    86469, 86469, 86469, 86469,  # MTOW
    38424, 38424, 38424, 38424,  # OEW
    52169, 52169, 52169, 52169,  # No Fuel
    86469, 86469,                # MTOW
    38424, 38424,                # OEW
    52169, 52169                 # No Fuel
]

case_n = [
    1, -1, 1, -1,  # Repeated values
    1, -1, 1, -1,  # Repeated values
    1, -1, 1, -1,  # Repeated values
    2.5, -1, 2.5, -1,  # Alternating values
    2.5, -1, 2.5, -1,  # Alternating values
    2.5, -1, 2.5, -1,  # Alternating values
    2.5, -1, 2.5, -1,  # Alternating values
    2.5, -1, 2.5, -1,  # Alternating values
    2.5, -1, 2.5, -1,  # Alternating values
    2.5, 2.5, 2.5, 2.5,  # Repeated 2.5 values
    2.5, 2.5
]

case_altitude_densities = [
    1.225, 1.225,  # 0 m
    0.4416, 0.4416,  # 31000 ft
    1.225, 1.225,  # 0 m
    0.4416, 0.4416,  # 31000 ft
    1.225, 1.225,  # 0 m
    0.4416, 0.4416,  # 31000 ft
    1.225, 1.225,  # 0 m
    0.4416, 0.4416,  # 31000 ft
    1.225, 1.225,  # 0 m
    0.4416, 0.4416,  # 31000 ft
    1.225, 1.225,  # 0 m
    0.4416, 0.4416,  # 31000 ft
    1.225, 1.225,  # 0 m
    0.4416, 0.4416,  # 31000 ft
    1.225, 1.225,  # 0 m
    0.4416, 0.4416,  # 31000 ft
    1.225, 1.225,  # 0 m
    0.4416, 0.4416,  # 31000 ft
    0.4416, 0.4416,  # Alternating 0 m and 31000 ft
    1.225, 0.4416,  # Alternating 0 m and 31000 ft
    1.225, 0.4416,  # Alternating 0 m and 31000 ft
    1.225, 0.4416   # Alternating 0 m and 31000 ft
]

case_M = [
    0.21, 0.21,  # Repeated 0.21
    0.41, 0.41,  # Repeated 0.41
    0.14, 0.14,  # Repeated 0.14
    0.27, 0.27,  # Repeated 0.27
    0.17, 0.17,  # Repeated 0.17
    0.31, 0.31,  # Repeated 0.31
    0.34, 0.34,  # Repeated 0.34
    0.64, 0.64,  # Repeated 0.64
    0.23, 0.23,  # Repeated 0.23
    0.43, 0.43,  # Repeated 0.43
    0.26, 0.26,  # Repeated 0.26
    0.5, 0.5,    # Repeated 0.5
    0.76, 0.76,  # Repeated 0.76
    0.85, 0.85,  # Repeated 0.85
    0.76, 0.76,  # Repeated 0.76
    0.85, 0.85,  # Repeated 0.85
    0.76, 0.76,  # Repeated 0.76
    0.85, 0.85,  # Repeated 0.85
    0.92, 0.92,  # Repeated 0.92
    0.92, 0.92,  # Repeated 0.92
    0.92, 0.92   # Repeated 0.92
]

# Lists for storing maximum and minimum values
max_shear_forces = []
min_shear_forces = []
max_bending_moments = []
min_bending_moments = []

# Iterate through all cases
for i in range(len(case_airspeeds)):
    # Retrieve parameters for the current case
    airspeed = case_airspeeds[i]
    weight = case_weights[i] * g  # Convert to Newtons
    load_factor = case_n[i]
    density = case_altitude_densities[i]
    M = case_M[i]
    
    # Calculate the angle of attack for the given weight
    alpha = find_angle_of_attack(density, airspeed, weight, span, M)
    
    # Calculate the lift distribution
    x_vals, lift_vals = lift_distribution(density, airspeed, alpha, span, M)
    
    # Calculate the shear force distribution, if the weight is lower than 80 000 kg, there is always a no-fuel condition
    if(case_weights[i] < 80000):
        shear_force_vals = shear_force_distribution(x_vals, lift_vals, engine_position, engine_weight, load_factor, 1)
    else:
        shear_force_vals = shear_force_distribution(x_vals, lift_vals, engine_position, engine_weight, load_factor, 0)
    
    # Calculate the bending moment distribution
    bending_moment_vals = bending_moment_distribution(x_vals, shear_force_vals)
    
    # Find the maximum and minimum values
    max_shear = np.max(shear_force_vals)
    min_shear = np.min(shear_force_vals)
    max_bending = np.max(bending_moment_vals)
    min_bending = np.min(bending_moment_vals)
    
    # Store the results
    max_shear_forces.append(max_shear)
    min_shear_forces.append(min_shear)
    max_bending_moments.append(max_bending)
    min_bending_moments.append(min_bending)
    
    # Print results for the current case
    print(f"Case {i + 1}:")
    print(f"Ideal angle of attack: {alpha:.2f}")
    print(f"  Max Shear Force: {max_shear:.2f} N")
    print(f"  Min Shear Force: {min_shear:.2f} N")
    print(f"  Max Bending Moment: {max_bending:.2f} Nm")
    print(f"  Min Bending Moment: {min_bending:.2f} Nm")
    print()

total_max_shear = max(max_shear_forces)
total_min_shear = min(min_shear_forces)
total_max_bm = max(max_bending_moments)
total_min_bm = min(min_bending_moments)

i = max_shear_forces.index(total_max_shear)
print(f"Maximum total shear: {total_max_shear}, Index: {i}")
i = min_shear_forces.index(total_min_shear)
print(f"Minimum total shear: {total_min_shear}, Index: {i}")
i = max_bending_moments.index(total_max_bm)
print(f"Maximum bending moment: {total_max_bm}, Index: {i}")
i = min_bending_moments.index(total_min_bm)
print(f"Minimum bending moment: {total_min_bm}, Index: {i}")