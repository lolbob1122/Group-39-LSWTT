import numpy as np
import scipy as sp
import math
from Experimental import ambient_results_q_inf
import matplotlib.pyplot as plt

S = 2*0.16*0.4169
A = (2*0.4169)**2/S
Qinfty = ambient_results_q_inf.q_inf
# CL_min = 0.00
# CL_max = 0.00

# Cm_min = 0.00
# Cm_max = 0.00

# CD_min = 0.000
# CD_max = 0.000
# CLd_test = 0.5  # Change val
# Cmd_test = 0.5  # Change val
# Cdd_test = 0.5  # Change val

# Read the text file and extract data from the "Freestream speed" section
with open("Numerical\\3D\\XFLR5textfiles\\Inviscid21ms\\Test_T1-21_0m_s-Panel-Inviscid.txt", "r") as file:
    lines = file.readlines()

# Print the first few lines to confirm file is being read correctly
# print("First few lines of the file:")
# print("".join(lines[:10]))  # Print the first 10 lines for verification

# Find the start of the "Freestream speed" data
start_idx = None
for i, line in enumerate(lines):
    if "Freestream speed" in line.strip():  # Search for the "Freestream speed" line
        start_idx = (
            i + 3
        )  # Skip the header and start with the data (2 lines after "Freestream speed")
        break

# Check if we found the "Freestream speed" section
if start_idx is None:
    print("Error: 'Freestream speed' section not found!")
else:
    # print(f"Data starts from line {start_idx}")
    pass

# Extract the rows under the "Freestream speed" section
data_lines = lines[start_idx:]

# Initialize lists to store the extracted columns
(
    alpha,
    beta,
    CL,
    CDi,
    CDv,
    CD,
    CY,
    Cl,
    Cm,
    Cn,
    Cni,
    Qinf,
    Xcp,
) = ([], [], [], [], [], [], [], [], [], [], [], [], [])

# Process each line to extract the values
for line in data_lines:
    # Strip leading/trailing spaces and split by any whitespace (tabs, spaces, etc.)
    line = line.replace(',', '')
    columns = line.strip().split()

    # Ensure there are enough columns in each line (12 columns)
    if len(columns) == 13:
        try:
            # Append the values to the respective lists
            alpha.append(float(columns[0]))
            beta.append(float(columns[1]))
            CL.append(float(columns[2]))
            CDi.append(float(columns[3]))
            CDv.append(float(columns[4]))
            CD.append(float(columns[5]))
            CY.append(float(columns[6]))
            Cl.append(float(columns[7]))
            Cm.append(float(columns[8]))
            Cn.append(float(columns[9]))
            Cni.append(float(columns[10]))
            Qinf.append(float(columns[11]))
            Xcp.append(float(columns[12]))
        except ValueError as e:
            print(f"Error converting data: {e} in line: {line}")
            continue

alpha_lst = alpha[:43]
CL_lst = CL[:43]
Lift_lst = []
CDi_lst = CDi[:43]
InducedDrag = []
CD_lst = CD[:43]
Qinf_lst = Qinf[:43]
#print(alpha_lst)

for i in range(len(CL_lst)):
    Lift = CL_lst[i]*Qinfty*S
    Di = CDi_lst[i]*Qinfty*S
    Lift_lst.append(Lift)
    InducedDrag.append(Di)

delta_lst = []
for i in range(len(alpha_lst)):
    delta = abs(CDi_lst[i]/CL_lst[i]**2*math.pi*A - 1)
    delta_lst.append(delta)

#print(delta_lst)

def remove_outliers_z_score(data, threshold=3):
    mean = np.mean(data)
    std = np.std(data)
    return [x for x in data if (abs(x - mean) / std) < threshold]

# clean delta data
delta_clean_data = remove_outliers_z_score(delta_lst)
#print(delta_clean_data)
Delta = sum(delta_clean_data)/(len(delta_clean_data))
#print(Delta)

def interpolate_CL(alpha, alpha_lst, CL_lst):
    return np.interp(alpha, alpha_lst, CL_lst)

# Example usage:
alpha = 3.75
CL = interpolate_CL(alpha, alpha_lst, CL_lst)
print(f"Interpolated CL value at alpha {alpha}: {CL}")

# Read the text file and extract data from the "Main Wing" section
with open("Numerical\\3D\\XFLR5textfiles\\Viscous21ms\\Test_T1-21_0m_s-Panel.txt", "r") as file:
    lines = file.readlines()

# Print the first few lines to confirm file is being read correctly
# print("First few lines of the file:")
# print("".join(lines[:10]))  # Print the first 10 lines for verification

# Find the start of the "Freestream speed" data
start_idx = None
for i, line in enumerate(lines):
    if "Freestream speed" in line.strip():  # Search for the "Freestream speed" line
        start_idx = (
            i + 3
        )  # Skip the header and start with the data (2 lines after "Freestream speed")
        break

# Check if we found the "Freestream speed" section
if start_idx is None:
    print("Error: 'Freestream speed' section not found!")
else:
    # print(f"Data starts from line {start_idx}")
    pass

# Extract the rows under the "Freestream speed" section
data_lines = lines[start_idx:]

# Initialize lists to store the extracted columns
(
    alpha,
    beta,
    CL,
    CDi,
    CDv,
    CD,
    CY,
    Cl,
    Cm,
    Cn,
    Cni,
    Qinf,
    Xcp,
) = ([], [], [], [], [], [], [], [], [], [], [], [], [])

# Process each line to extract the values
for line in data_lines:
    # Strip leading/trailing spaces and split by any whitespace (tabs, spaces, etc.)
    line = line.replace(',', '')
    columns = line.strip().split()

    # Ensure there are enough columns in each line (12 columns)
    if len(columns) == 13:
        try:
            # Append the values to the respective lists
            alpha.append(float(columns[0]))
            beta.append(float(columns[1]))
            CL.append(float(columns[2]))
            CDi.append(float(columns[3]))
            CDv.append(float(columns[4]))
            CD.append(float(columns[5]))
            CY.append(float(columns[6]))
            Cl.append(float(columns[7]))
            Cm.append(float(columns[8]))
            Cn.append(float(columns[9]))
            Cni.append(float(columns[10]))
            Qinf.append(float(columns[11]))
            Xcp.append(float(columns[12]))
        except ValueError as e:
            print(f"Error converting data: {e} in line: {line}")
            continue

alpha_lstV = alpha[:35]
CL_lstV = CL[:35]
CDi_lstV = CDi[:35]
CD_lstV = CD[:35]
Qinf_lstV = Qinf[:35]
print(alpha_lstV)

# Read the text file and extract data from the "Freestream speed" section
with open("Numerical\\3D\\XFLR5textfiles\\Inviscid21ms\\Test_T1-21_0m_s-Panel-Inviscid.txt", "r") as file:
    lines = file.readlines()

# Print the first few lines to confirm file is being read correctly
# print("First few lines of the file:")
# print("".join(lines[:10]))  # Print the first 10 lines for verification

# Find the start of the "Freestream speed" data
start_idx = None
for i, line in enumerate(lines):
    if "Freestream speed" in line.strip():  # Search for the "Freestream speed" line
        start_idx = (
            i + 3
        )  # Skip the header and start with the data (2 lines after "Freestream speed")
        break




# Real results

# Read the text file and extract data from the "Freestream speed" section
with open("Experimental\\3D\\raw_3D.txt", "r") as file:
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

# Initialize lists to store the extracted columns
(
    nr,
    time,
    alpha_real,
    deltaPb,
    P_bar,
    T,
    D_real,
    L_real,
    Fz,
    RPM,
    rho,
) = ([], [], [], [], [], [], [], [], [], [], [])

# Process each line to extract the values
for line in data_lines:
    # Strip leading/trailing spaces and split by any whitespace (tabs, spaces, etc.)
    columns = line.strip().split()

    # Ensure there are enough columns in each line (12 columns)
    if len(columns) == 11:
        try:
            # Append the values to the respective lists
            nr.append(float(columns[0]))
            time.append(float(columns[1]))
            alpha_real.append(float(columns[2]))
            deltaPb.append(float(columns[3]))
            P_bar.append(float(columns[4]))
            T.append(float(columns[5]))
            D_real.append(float(columns[6]))
            L_real.append(float(columns[7]))
            Fz.append(float(columns[8]))
            RPM.append(float(columns[9]))
            rho.append(float(columns[10]))
        except ValueError as e:
            print(f"Error converting data: {e} in line: {line}")
            continue

alpha_real_lst = alpha[:54]
L_real_lst = 2*L_real[:54]
CL_real_lst = []
D_real_lst = 2*D_real[:54]
CD_real_lst = []
for i in range(len(L_real_lst)):
    CL = L_real_lst[i]/(0.5*S*Qinfty)
    CD = D_real_lst[i]/(0.5*S*Qinfty)
    CL_real_lst.append(CL)
    CD_real_lst.append(CD)

a = (CL_real_lst[30]-CL_real_lst[2])/(alpha_real_lst[30]-alpha_real_lst[2])*180/(math.pi)
a0 = 0.09483333333  # change val to misha's val later
print('a0', a0)
tau = a0/(a*(1+a0/math.pi/A))-1
CDi_real_lst = []
CDi_percentOfCD = []
D_ind_real_lst = []
for i in range(len(CD_real_lst)):
    CDi = CL_real_lst[i]**2*(tau+1)/(math.pi*A)
    Di = CDi*S*Qinfty
    Percent = CDi/CD_real_lst[i]*100
    CDi_real_lst.append(CDi)
    CDi_percentOfCD.append(Percent)
    D_ind_real_lst.append(Di)

print(Percent)

# for i, j in enumerate(alpha_lst):

#     for m, n in enumerate(alpha_real_lst):
#         def interpolate_CL(alpha, alpha_lst, CL_lst):
#             return np.interp(alpha, alpha_lst, CL_lst)

#         # Example usage:
#         alpha = 3.75
#         CL = interpolate_CL(alpha, alpha_lst, CL_lst)
#         print(f"Interpolated CL value at alpha {alpha}: {CL}")

plt.plot(alpha_lst, CL_lst, color='green', label='XFLR5 Results')
plt.plot(alpha_real_lst, CL_real_lst, color='purple', label='Wind Tunnel Results')
plt.xlabel("$\alpha$ [$\deg$]")
plt.ylabel("$C_L$ [-]")
plt.legend()
plt.title("Comparison of lift curves of experimental data and XFLR5 data")
plt.show()

plt.plot(alpha_lst, CDi_lst, color='green', label='XFLR5 Results')
plt.plot(alpha_real_lst, CDi_real_lst, color='purple', label='Wind Tunnel Results')
plt.xlabel("$\alpha$ [$\deg$]")
plt.ylabel("$C_{D_i}$ [-]")
plt.legend()
plt.title("Comparison of induced drag of experimental data and XFLR5 data")
plt.show()
#print(alpha_lst)