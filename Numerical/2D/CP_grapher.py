#import pandas as pd
#import matplotlib.pyplot as plt
#import CP_experimental_data as CPe
#
## 0 = -4 AOA, 1 = not sure, 2 = 4 AOA, 3 = 10 AOA, 4 = 16 AOA
#CPe_index = 3
#
## Load the data from the provided text file
#file_path = 'XFLR5textfiles/CP_data/CP 10.txt'
#data = pd.read_csv(file_path, skiprows=4, delim_whitespace=True, names=["x", "Cpi", "Cpv", "Qi", "Qv"])
#
## Convert all columns to numeric, coercing errors to NaN
#data = data.apply(pd.to_numeric, errors='coerce')
#
## Drop any rows with NaN values resulting from type conversion
#data = data.dropna()
#
## Separate the upper and lower surfaces based on the specified line ranges
#upper_surface = data.iloc[:90]
#lower_surface = data.iloc[90:]
#
## Reverse the lower surface data to go from leading edge to trailing edge
#lower_surface = lower_surface[::-1]
#
## Plot the corrected data with additional formatting changes
#plt.figure(figsize=(10, 6))
#
## Plot the upper surface without dots
#plt.plot(upper_surface['x'], upper_surface['Cpv'], '-', color='blue', label=r'CP numerical (Upper Surface)')
#plt.plot(CPe.x_upper, CPe.CP_upper[CPe_index], marker = "x", color='darkorange', label=r'CP experimental (Upper Surface)')
## Plot the lower surface without dots
#plt.plot(lower_surface['x'], lower_surface['Cpv'], '-', color='red', label=r'CP numerical (Lower Surface)')
#plt.plot(CPe.x_lower, CPe.CP_lower[CPe_index], marker = "x", color='g', label=r'CP experimental (Upper Surface)')
##plt.plot(lower_surface['x'], lower_surface['Cpi'], '-', color='orange', label=r'C_p (Lower Surface)')
## Connect the trailing edges of the upper and lower surfaces
##plt.plot([upper_surface['x'].iloc[-1], lower_surface['x'].iloc[-1]],
##         [upper_surface['Cpv'].iloc[-1], lower_surface['Cpv'].iloc[-1]],
##         '-', color='black', label='Trailing Edge Connection')
#
## Formatting the graph
#plt.gca().invert_yaxis()  # Invert y-axis for proper visualization
#plt.xlabel('Position (x/c)', fontsize=12)
#plt.ylabel('Pressure Coefficient (CP)', fontsize=12)
##plt.title('Pressure Coefficient Distribution', fontsize=14)
#plt.grid(True)
#plt.legend(fontsize=10)
#plt.tight_layout()
#
## Display the plot
#plt.show()


import pandas as pd
import matplotlib.pyplot as plt
import matplotlib.ticker as ticker
import CP_experimental_data as CPe

# 0 = -4 AOA, 1 = not sure, 2 = 4 AOA, 3 = 10 AOA, 4 = 16 AOA
CPe_index = 3

# Load the data from the provided text file
file_path = 'XFLR5textfiles/CP_data/CP 10.txt'
data = pd.read_csv(file_path, skiprows=4, delim_whitespace=True, names=["x", "Cpi", "Cpv", "Qi", "Qv"])

# Convert all columns to numeric, coercing errors to NaN
data = data.apply(pd.to_numeric, errors='coerce')

# Drop any rows with NaN values resulting from type conversion
data = data.dropna()

# Separate the upper and lower surfaces based on the specified line ranges
upper_surface = data.iloc[:90]
lower_surface = data.iloc[90:]

# Reverse the lower surface data to go from leading edge to trailing edge
lower_surface = lower_surface[::-1]

# Plot the corrected data with additional formatting changes
plt.figure(figsize=(8, 5))

# Plot the upper and lower surfaces
plt.plot(upper_surface['x'], upper_surface['Cpv'], '-', color='blue', label='Cp numerical (Upper Surface)', linewidth=1)
plt.plot(CPe.x_upper, CPe.CP_upper[CPe_index], marker='x', color='darkorange', label='Cp experimental (Upper Surface)', linewidth=1)
plt.plot(lower_surface['x'], lower_surface['Cpv'], '-', color='red', label='Cp numerical (Lower Surface)', linewidth=1)
plt.plot(CPe.x_lower, CPe.CP_lower[CPe_index], marker='x', color='green', label='Cp experimental (Lower Surface)', linewidth=1)

# Formatting the graph
plt.gca().invert_yaxis()  # Invert y-axis for proper visualization
plt.xlabel('Position (x/c)', fontsize=12)
plt.ylabel('Pressure Coefficient (Cp)', fontsize=12)

# Adjust grid line frequency
ax = plt.gca()
ax.xaxis.set_major_locator(ticker.MultipleLocator(0.1))  # Major ticks every 0.1
ax.xaxis.set_minor_locator(ticker.MultipleLocator(0.02))  # Minor ticks every 0.02
ax.yaxis.set_major_locator(ticker.MultipleLocator(1))  # Major ticks every 1
ax.yaxis.set_minor_locator(ticker.MultipleLocator(0.2))  # Minor ticks every 0.2

# Simplify grid lines
plt.grid(visible=True, which='major', color='black', linestyle='-', alpha=0.3)
plt.grid(visible=False, which='minor')  # Hide minor grid lines

# Add a legend inside the plot area
plt.legend(fontsize=12, loc='upper right', frameon=True)


# Adjust layout for readability
plt.tight_layout()

# Display the plot
plt.show()
