import matplotlib.pyplot as plt
import numpy as np
import sys

# caution: path[0] is reserved for script path (or '' in REPL)
sys.path.insert(1, 'Experimental')

import Ambient_Results.ambient_results_rho as ar

####################################################################
############## ONLY CHANGE VARIABLES IN THIS BOX ###################
runNumber = 15                                                   ####
#                                                               ####
#                                                               ####
####################################################################
######### DO NOT CHANGE ANYTHING AFTER THIS POINT ##################


Data2D = []

# Read the text file and extract data from the "Freestream speed" section
with open("Experimental/2D/raw_2D.txt", "r") as file:
    lines = file.readlines()

# Find the start of the "Freestream speed" data
start_idx = None
for i, line in enumerate(lines):
    if "Run_nr" in line.strip():  # Search for the "Freestream speed" line
        start_idx = (
            i + 2
        )  # Skip the header and start with the data (2 lines after "Freestream speed")
        break

# Check if we found the "Freestream speed" section
if start_idx is None:
    print("Error: 'Run_nr' section not found!")
else:
    # print(f"Data starts from line {start_idx}")
    pass

# Extract the rows under the "Freestream speed" section
data_lines = lines[start_idx:]


# Process each line to extract the values
for line in data_lines:
    # Strip leading/trailing spaces and split by any whitespace (tabs, spaces, etc.)
    columns = line.strip().split() #columns = one row of data starting from row 3
    Data2D.append(columns)
    
runXdata = Data2D[runNumber-6] #select only one run
# print(runXdata)
pValues = runXdata[8:57]
name = "Experimental\\Ambient_Results\\converted_2D.csv"
q_inf = ar.get_ambient_results_new(name, runNumber)[1]
# print(q_inf)
Cp = []
for i in range(len(pValues)):
    Cp.append((float(pValues[i]) - float(runXdata[4]))/ q_inf )

# print(Cp)
PosList = []
with open("Experimental\\2D\\Airfoil_Tap_Positions.txt", "r") as file:
    for line in file.readlines():
        columns = line.strip().split()
        PosList.append(columns)

# print(PosList)
# Extract the second column from PosList and convert it to floats
x_values = [float(row[1]) for row in PosList[:49]]  # Only take the first 49 entries

# # Ensure Cp and x_values are the same length
# if len(Cp) != len(x_values):
#     print("Error: Mismatch in lengths of Cp and x_values")
# else:
#     # Plot Cp vs x_values
#     plt.figure(figsize=(10, 6))
#     plt.plot(x_values, Cp, marker='o', linestyle='-', color='b', label='Cp vs Position')
#     plt.title(f'Pressure Coefficient (Cp) vs Airfoil Tap Positions (Run {runNumber})')
#     plt.xlabel('Tap Position (x-axis)')
#     plt.ylabel('Pressure Coefficient (Cp)')
#     plt.grid(True)
#     plt.legend()
#     plt.show()

# Split x_values and Cp into two segments
x_values_first = x_values[:25]
Cp_first = Cp[:25]

x_values_second = x_values[25:]
Cp_second = Cp[25:]

# Plot the two segments separately
plt.figure(figsize=(10, 6))
plt.plot(x_values_first, Cp_first, marker='o', linestyle='-', color='b', label='Cp (Segment 1)')
plt.plot(x_values_second, Cp_second, marker='o', linestyle='-', color='r', label='Cp (Segment 2)')
plt.title(f'Pressure Coefficient (Cp) vs Airfoil Tap Positions (Run {runNumber})')
plt.xlabel('Tap Position (x-axis)')
plt.ylabel('Pressure Coefficient (Cp)')
plt.grid(True)
plt.legend()
plt.show()
