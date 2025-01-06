import numpy as np
import matplotlib.pyplot as plt

# ---------------------------------------------------
# 1) Wingbox geometry parameters
# ---------------------------------------------------

b = 17.74         # Wing semi-span [m]
x_break = 5.0     # The middle spar disappears after y > 5 m (example)

# Two-cell region: 
#   - Cell #1 area (A1) = 0.02 m^2
#   - Cell #2 area (A2) = 0.015 m^2
A1 = 0.02    # [m^2]
A2 = 0.015   # [m^2]

# We'll name the walls for "two-cell" region
cell1_segments = ["front_spar", "upper_skin_front", "middle_spar", "lower_skin_front"]
cell2_segments = ["middle_spar", "upper_skin_rear",  "rear_spar",   "lower_skin_rear"]
all_segments_2cell = list(set(cell1_segments + cell2_segments))

# After the middle spar disappears, we have a single cell with:
#   A_single = A1 + A2
# The set of walls is effectively front_spar, rear_spar, 
# and the combined top/bottom skins (front+rear).
# We'll define them as:
single_cell_segments = ["front_spar", "upper_skin", "rear_spar", "lower_skin"]

# ---------------------------------------------------
# 2) Define the torque distribution T(y)
# ---------------------------------------------------

T0 = 10e3  # torque [N*m] at the root, example
def T(y):
    """
    Example: linear decrease from T0 at y=0 
    down to 0 at y=b.
    Replace with real function/data as needed.
    """
    return T0 * (1 - y / b)

# ---------------------------------------------------
# 3) Shear flow solver with disappearing spar
# ---------------------------------------------------

def torque_shear_flow_discontinuous(torque, y, y_break):
    """
    Returns a dictionary of wall segment -> shear flow [N/m]
    due to 'torque' at station y, 
    with a 2-cell design for y <= y_break,
    and a 1-cell design (middle spar gone) for y > y_break.

    In both cases, we assume uniform, constant shear flow (q0) 
    around each cell (equal twist).
    """
    # 1) If y <= y_break => 2-cell approach
    if y <= y_break:
        # Use 2-cell formula:
        #   T = 2*q0*(A1 + A2) => q0 = T / [2*(A1 + A2)]
        q0 = torque / (2.0 * (A1 + A2)) if (A1 + A2) != 0.0 else 0.0
        q_values = {}
        for seg in all_segments_2cell:
            if seg in cell1_segments and seg in cell2_segments:
                # Middle spar: belongs to both cells
                # If q0 is same for both, net difference is 0
                q_values[seg] = q0
            elif seg in cell1_segments:
                q_values[seg] = q0
            elif seg in cell2_segments:
                q_values[seg] = q0
            else:
                q_values[seg] = 0.0
        return q_values

    # 2) If y > y_break => single-cell approach (middle spar gone)
    else:
        # Single cell area = A1 + A2
        #   T = 2*q0*(A1 + A2) => q0 = T / [2*(A1 + A2)]
        A_single = A1 + A2
        q0 = torque / (2.0 * A_single) if A_single != 0.0 else 0.0
        q_values = {}
        for seg in single_cell_segments:
            # Every wall in the single cell sees the same q0
            q_values[seg] = q0
        return q_values

# ---------------------------------------------------
# 4) Loop over the span and plot an example
# ---------------------------------------------------

if __name__ == "__main__":
    # We'll sample 50 points from y=0 to y=b
    n_points = 50
    y_array = np.linspace(0, b, n_points)

    # We'll store the shear flow in the "front_spar" to see how it changes
    front_spar_q = []

    for y_val in y_array:
        torque_val = T(y_val)
        q_dict = torque_shear_flow_discontinuous(torque_val, y_val, x_break)

        # Because the segments differ for y<=x_break vs. y>x_break,
        # we need to handle the two cases carefully when we access "front_spar".
        if y_val <= x_break:
            # 2-cell region => look for "front_spar" in q_dict
            q_front = q_dict.get("front_spar", 0.0)
        else:
            # single-cell region => the front spar is named "front_spar" as well
            q_front = q_dict.get("front_spar", 0.0)

        front_spar_q.append(q_front)

    # Plot
    plt.figure(figsize=(8,6))
    plt.plot(y_array, front_spar_q, label="Front Spar (Torque-Only) Shear Flow")
    plt.axvline(x=x_break, color='red', linestyle='--', label="Middle Spar Disappears")
    plt.xlabel("Spanwise location, y [m]")
    plt.ylabel("Shear Flow q [N/m]")
    plt.title("Torque-Induced Shear Flow in Front Spar with Disappearing Middle Spar")
    plt.grid(True)
    plt.legend()
    plt.show()
