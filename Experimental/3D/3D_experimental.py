import pandas as pd

# Define the file path
file_path = 'Experimental/3D/raw_3D.txt'

# Read the file into a DataFrame, skipping the first two rows to handle headers
data = pd.read_csv(file_path, delim_whitespace=True, skiprows=2)

# Create individual lists for each parameter
alpha = data['Alpha'].tolist()
delta_Pb = data['Delta_Pb'].tolist()
p_bar = data['P_bar'].tolist()
temperature = data['T'].tolist()
fx = data['Fx'].tolist()
fy = data['Fy'].tolist()
fz = data['Fz'].tolist()
rpm = data['rpm'].tolist()
rho = data['Rho'].tolist()


# Print the lists (example)
print(f"Alpha: {alpha[:5]} ...")
print(f"Delta_Pb: {delta_Pb[:5]} ...")
print(f"P_bar: {p_bar[:5]} ...")
print(f"Temperature: {temperature[:5]} ...")
print(f"Fx: {fx[:5]} ...")
print(f"Fy: {fy[:5]} ...")
print(f"Fz: {fz[:5]} ...")
print(f"RPM: {rpm[:5]} ...")
print(f"Rho: {rho[:5]} ...")

