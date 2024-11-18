import numpy as np

# Define the file path
file_path_alpha0 = r"Wing Structure\\XFLR5_files\\MainWing_a=0.00_v=10.00ms.txt"
file_path_alpha10 = r"Wing Structure\\XFLR5_files\\MainWing_a=10.00_v=10.00ms.txt"

def xflr(file_path):
    # Initialize lists to store the relevant data
    y_span = []
    chord = []
    ai = []
    cl = []
    icd = []
    cm_at_chord_4 = []

    # Open the file and manually parse the lines
    with open(file_path, 'r') as file:
        main_wing_section = False

        for line in file:
            # Identify the beginning of the "Main Wing" section
            if "Main Wing1" in line:
                main_wing_section = True
                continue

            # Break the loop if we reach another section or the end of the main wing section
            if "Main Wing Cp Coefficients" in line:
                break

            # If we are in the main wing section, parse the data
            if main_wing_section:
                try:
                    # Split the line into values
                    values = line.split()

                    # Skip lines that do not have enough columns
                    if len(values) < 8:
                        continue

                    # Extract relevant columns
                    y_span.append(float(values[0]))
                    chord.append(float(values[1]))
                    ai.append(float(values[2]))
                    cl.append(float(values[3]))
                    icd.append(float(values[5]))
                    cm_at_chord_4.append(float(values[7]))
                except ValueError:
                    # Skip lines that cannot be parsed
                    continue

    # Convert lists to numpy arrays for easier manipulation
    y_span = np.array(y_span)
    chord = np.array(chord)
    ai = np.array(ai)
    cl = np.array(cl)
    icd = np.array(icd)
    cm_at_chord_4 = np.array(cm_at_chord_4)

    # Stack the columns together if needed
    main_wing_data = np.column_stack((y_span, chord, ai, cl, icd, cm_at_chord_4))
    return y_span, chord, ai, cl, icd, cm_at_chord_4, main_wing_data

y_span_alpha0, chord_alpha0, ai_alpha0, cl_alpha0, icd_alpha0, cm_at_chord_4_alpha0, main_wing_data_alpha0 = xflr(file_path_alpha0)
y_span_alpha10, chord_alpha10, ai_alpha10, cl_alpha10, icd_alpha10, cm_at_chord_4_alpha10, main_wing_data_alpha10 = xflr(file_path_alpha10)

# Display the extracted data
print("Cl at 0 deg angle of attack: ", cl_alpha0)
print("Cl at 10 deg angle of attack:", cl_alpha10)