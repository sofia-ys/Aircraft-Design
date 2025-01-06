import sys
sys.path.append('Wing Structure')
sys.path.append('Wing_Box_Detailed')
import shear_bending_flight as sbf
import wing_box_constants as wb
import shear_buckling as sb
import numpy as np
import matplotlib.pyplot as plt
import Ixx

k_v = 1

def example_shear_force_distribution(y_values):
    """
    Dummy example that returns a plausible shear force distribution
    (highest at root, decreasing toward tip). Replace with real data.
    """
    # Let's just do a parabola from root to tip:
    V_root = 4e5  # 400 kN near the root
    V_tip  = 0
    shear_vals = V_root - (V_root - V_tip)*(y_values/(y_values[-1]))**2
    return shear_vals

# -------------------------------------------------------------------------
# 2. A FUNCTION TO COMPUTE AVERAGE SHEAR STRESS AT EACH Y FOR A GIVEN DESIGN
# -------------------------------------------------------------------------
def calc_average_shear_stress_for_design(y_values, shear_force_vals, design_id, k_v=1):
    """
    Computes the average shear stress distribution for the given design,
    summing the cross-sectional area (h_i * t_i) of each spar web that design uses.

    :param y_values:          array of spanwise stations (0 to b/2)
    :param shear_force_vals:  array of shear force V(y) at each station
    :param design_id:         0, 1, or 2 => design #1, #2, #3
    :param k_v:               optional factor for “max shear” approximation
    :return:                  np.array of tau_ave(y) for each station
    """
    if k_v is None:
        k_v = wb.k_v  # default to the global k_v if none provided

    tau_array = np.zeros_like(y_values, dtype=float)

    # design_id is 0-based internally:
    #   design_id=0 => actual_design_number=1 => middle spar only up to y<=5
    #   design_id=1 => actual_design_number=2 => middle spar only up to y<=10
    #   design_id=2 => actual_design_number=3 => always 2 spars
    actual_design_number = design_id + 1

    # Pick the correct thickness distribution
    if actual_design_number == 1:
        span_t1 = wb.span_t1_1
        t1_vals = wb.t1_1
    elif actual_design_number == 2:
        span_t1 = wb.span_t1_2
        t1_vals = wb.t1_2
    else:  # actual_design_number == 3
        span_t1 = wb.span_t1_3
        t1_vals = wb.t1_3

    # For each station along y_values:
    for i, y in enumerate(y_values):
        V_y = shear_force_vals[i]  # local shear force

        # ---------------------------------------------------------------
        # Decide how many spars are present at this spanwise location y
        # ---------------------------------------------------------------
        if actual_design_number == 1:
            # Design #1 => middle spar up to y=5 m
            if y <= 5:
                spar_ids = [1, 2, 3]  # front, rear, middle
            else:
                spar_ids = [1, 2]     # front, rear only
        elif actual_design_number == 2:
            # Design #2 => middle spar up to y=10 m
            if y <= 10:
                spar_ids = [1, 2, 3]
            else:
                spar_ids = [1, 2]
        else:
            # Design #3 => always 2 spars
            spar_ids = [1, 2]

        # Sum cross-sectional area of the active spar webs
        total_area = 0.0
        for s_id in spar_ids:
            # local height
            h_spar = sb.getSparHeight(design_id, s_id, y)
            # local thickness
            t_spar = sb.getSparThickness(span_t1, t1_vals, y)
            total_area += h_spar * t_spar

        # ---------------------------------------------------------------
        # Compute average shear stress (times k_v for “max” estimate)
        # ---------------------------------------------------------------
        if total_area > 1e-12:
            tau_ave = V_y / total_area
        else:
            tau_ave = 0.0

        tau_array[i] = k_v * tau_ave

    return tau_array

# -------------------------------------------------------------------------
# 3. A FUNCTION TO PLOT THE AVERAGE SHEAR DISTRIBUTION FOR ALL 3 DESIGNS
# -------------------------------------------------------------------------
def plot_average_shear_distribution(y_values, shear_force_vals):
    """
    Plots the average shear (scaled by k_v) vs. y for each of the 3 designs.
    """
    plt.figure(figsize=(8,6))

    for d_id in range(3):  # d_id=0->Design1, 1->Design2, 2->Design3
        tau_dist = calc_average_shear_stress_for_design(
            y_values, 
            shear_force_vals, 
            design_id=d_id, 
            k_v=k_v
        )
        plt.plot(y_values, tau_dist, label=f"Design {d_id+1}")
    
    plt.xlabel("Spanwise Position y (m)")
    plt.ylabel(r"Shear Stress $\tau_{\mathrm{ave}}\times k_v$ (Pa)")
    plt.title("Average Shear Distribution (All Designs)")
    plt.legend()
    plt.grid(True)
    plt.show()

# -------------------------------------------------------------------------
# 4. DEMO / EXAMPLE OF USAGE
# -------------------------------------------------------------------------
if __name__ == "__main__":
    # Let’s create a 100-point y-array from 0 to half-span:
    y_values = np.linspace(0, wb.b/2, 100)

    # For demonstration, we create a sample shear-force distribution:
    sbf.shear_force_vals = example_shear_force_distribution(y_values)

    # Plot the average shear distribution for all 3 designs:
    plot_average_shear_distribution(y_values, sbf.shear_force_vals)
