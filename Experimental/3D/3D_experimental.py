import pandas as pd
import matplotlib.pyplot as plt
import numpy as np
import math 

# Define the file path
file_path = "Experimental/3D/raw_3D.txt"

# Read the file into a DataFrame, inferring column names from the first row of data
data = pd.read_csv(file_path, delim_whitespace=True, header=1)

# Extract column names dynamically
column_names = data.columns

# Create individual lists for each parameter based on the dynamic column names
parameter_lists = {name: data[name].tolist() for name in column_names}

# Calculate the C_l
# C_l = Fy / 0.5*rho*V^2*S

Fy = parameter_lists['N.1']
Alpha = parameter_lists['degrees']

C_l = []

for i in range(0,73, 1): 
    C_l.append(Fy[i] / (0.5 * 1.190 * 20.63985**2 * 0.4169 * 0.16))

# print('C_L:',C_l)
# print('Alpha:',Alpha)
# Plot Fy against Alpha if both columns exist
# Plot Alpha vs C_l
plt.figure(figsize=(8,6))
plt.plot(Alpha, C_l, marker='o', linestyle='-', color='b')
plt.title('Lift Coefficient (C_l) vs Angle of Attack (Alpha)')
plt.xlabel('Angle of Attack (Alpha) [degrees]')
plt.ylabel('Lift Coefficient (C_l)')
plt.grid(True)
plt.show()

# Calculate the slope of the linear section
# Define a range for the linear section (e.g., where Alpha is between 5 and 15)

slope = (C_l[35] - C_l[0])/(Alpha[35] - Alpha[0])

# Perform a linear fit (least squares method)

print(f"Slope of the linear section: {slope}")

# Now calculate the efficiency factor 
a_0 = 0.0948333 *180 / math.pi
a = slope *180 / math.pi
AR = 5.21125

efficiency_factor = (a_0/a - 1)*(math.pi * AR / a_0) - 1

print(efficiency_factor)
# # Print each parameter list with its name (example)
# for parameter, values in parameter_lists.items():
#     print(f"{parameter}: {values[:5]} ...")  # Print the first 5 values as a preview