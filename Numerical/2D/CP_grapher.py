import pandas as pd
import matplotlib.pyplot as plt

# Load the data from the provided text file
file_path = 'XFLR5textfiles/CP_data/CP -4.txt'
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
plt.figure(figsize=(10, 6))

# Plot the upper surface without dots
plt.plot(upper_surface['x'], upper_surface['Cpv'], '-', color='blue', label=r'C_p (Upper Surface)')
#plt.plot(upper_surface['x'], upper_surface['Cpi'], '-', color='purple', label=r'C_p (Upper Surface)')
# Plot the lower surface without dots
plt.plot(lower_surface['x'], lower_surface['Cpv'], '-', color='red', label=r'C_p (Lower Surface)')
#plt.plot(lower_surface['x'], lower_surface['Cpi'], '-', color='orange', label=r'C_p (Lower Surface)')
# Connect the trailing edges of the upper and lower surfaces
#plt.plot([upper_surface['x'].iloc[-1], lower_surface['x'].iloc[-1]],
#         [upper_surface['Cpv'].iloc[-1], lower_surface['Cpv'].iloc[-1]],
#         '-', color='black', label='Trailing Edge Connection')

# Formatting the graph
plt.gca().invert_yaxis()  # Invert y-axis for proper visualization
plt.xlabel('Position (x/c)', fontsize=12)
plt.ylabel('Pressure Coefficient (C_p)', fontsize=12)
plt.title('Pressure Coefficient Distribution', fontsize=14)
plt.grid(True)
plt.legend(fontsize=10)
plt.tight_layout()

# Display the plot
plt.show()
