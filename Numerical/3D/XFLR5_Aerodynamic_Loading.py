import numpy as np
import scipy as sp
import math
# from Experimental.Ambient_Results.ambient_results_rho import q_inf
# from ambient_results_rho import q_inf
import matplotlib.pyplot as plt

S = 2*0.16*0.4169
A = (2*0.4169)**2/S
print('A', A)
Qinfty = 253.92576892582358
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
CDi_lst = CDi[:43]
CD_lst = CD[:43]
Qinf_lst = Qinf[:43]
#print(alpha_lst)

Lift_lst = []
InducedDrag = []
Drag_lst = []

for i in range(len(CL_lst)):
    Lift = CL_lst[i]*Qinfty*S
    Di = CDi_lst[i]*Qinfty*S
    Lift_lst.append(Lift)
    InducedDrag.append(Di)
    Drag_lst.append(Di)

delta_lst = []
for i in range(len(alpha_lst)):
    delta = abs(CDi_lst[i]/(CL_lst[i]**2)*math.pi*A - 1)
    delta_lst.append(delta)

print(delta_lst)

def remove_outliers_z_score(data, threshold=3):
    mean = np.mean(data)
    std = np.std(data)
    return [x for x in data if (abs(x - mean) / std) < threshold]

# clean delta data

delta_clean_data = remove_outliers_z_score(delta_lst)
print(delta_clean_data)
print('SSD delta', np.std(delta_clean_data))
Delta = sum(delta_clean_data)/(len(delta_clean_data))
print('delta', Delta)

def interpolate_CL(alpha, alpha_lst, CL_lst):
    return np.interp(alpha, alpha_lst, CL_lst)

# Example usage:
# alpha = 3.75
# CL = interpolate_CL(alpha, alpha_lst, CL_lst)
# print(f"Interpolated CL value at alpha {alpha}: {CL}")

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
CDv_lstV = CDv[:35]
CD_lstV = CD[:35]
Qinf_lstV = Qinf[:35]
print(alpha_lstV)

Lift_lstV = []
InducedDrag_V = []
ZeroLiftDrag_V = []
Drag_lstV = []
for i in range(len(CL_lstV)):
    Lift = CL_lstV[i]*Qinfty*S
    Di = CDi_lstV[i]*Qinfty*S
    Dv = CDv_lstV[i]*Qinfty*S
    D = Di+Dv
    Lift_lst.append(Lift)
    InducedDrag.append(Di)
    ZeroLiftDrag_V.append(Dv)
    Drag_lstV.append(D)

delta_lstV = []
for i in range(len(alpha_lstV)):
    delta = abs(CDi_lstV[i]/(CL_lstV[i]**2)*math.pi*A - 1)
    delta_lstV.append(delta)

print('Delta viscous', delta_lstV)

def remove_outliers_z_score(data, threshold=3):
    mean = np.mean(data)
    std = np.std(data)
    return [x for x in data if (abs(x - mean) / std) < threshold]

# clean delta data
delta_clean_dataV = remove_outliers_z_score(delta_lstV)
print(delta_clean_data)
print("SSD for delta", np.std(delta_clean_dataV))
DeltaV = sum(delta_clean_dataV)/(len(delta_clean_dataV))
print('deltaV', DeltaV)

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
with open("Numerical\\3D\\XFLR5textfiles\\Inviscid21ms\\raw_3DNew.txt", "r") as file:
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
    alpha_real,
    deltaPb,
    P_bar,
    T,
    D_real,
    L_real,
    Fz,
    RPM,
    rho,
) = ([], [], [], [], [], [], [], [], [], [])

# Process each line to extract the values
for line in data_lines:
    # Strip leading/trailing spaces and split by any whitespace (tabs, spaces, etc.)
    columns = line.strip().split()

    # Ensure there are enough columns in each line (12 columns)
    if len(columns) == 10:
        try:
            # Append the values to the respective lists
            nr.append(float(columns[0]))
            alpha_real.append(float(columns[1]))
            deltaPb.append(float(columns[2]))
            P_bar.append(float(columns[3]))
            T.append(float(columns[4]))
            D_real.append(float(columns[5]))
            L_real.append(float(columns[6]))
            Fz.append(float(columns[7]))
            RPM.append(float(columns[8]))
            rho.append(float(columns[9]))
        except ValueError as e:
            print(f"Error converting data: {e} in line: {line}")
            continue

alpha_real_lst = alpha_real[:56]
print('alpha real', alpha_real_lst)
L_reallst = L_real[:56]
L_real_lst = []
for i in range(len(L_reallst)):
    L = 2*L_reallst[i]
    L_real_lst.append(L)
CL_real_lst = []
D_real_lst = D_real[:56]
CD_real_lst = []
for i in range(len(L_real_lst)):
    CL = L_real_lst[i]/(S*Qinfty)
    CD = 2*D_real_lst[i]/(S*Qinfty)
    CL_real_lst.append(CL)
    CD_real_lst.append(CD)

a = 0.06714*180/math.pi
a0 = 0.09483333333*180/math.pi  
print('a0', a0)
tau = (a0/a-1)/(a0/(math.pi*A))-1

# plt.plot(alpha_lstV, delta_lstV, color='red', label='$\\delta$ from XFLR5')
# plt.axhline(y=tau, xmin=alpha_lstV[0], xmax=alpha_lstV[-1], color='blue', linestyle='--', label='$\\tau$ from experimental data')
# plt.xlabel('Angle of attack $\\alpha$ [$\\deg$]', fontsize=12)
# plt.ylabel('Induced drag efficiency $\\delta$ [-]', fontsize=12)
# plt.legend(fontsize=12)
# plt.grid(True)
# plt.title('Induced drag efficiency as a function of angle of attack')
# plt.show()

print('tau', tau)
print('A', A)
CDi_real_lst = []
CDi_percentOfCD = []
D_ind_real_lst = []
CDv_real_lst = []
for i in range(len(CD_real_lst)):
    CDi = (CL_real_lst[i])**2*(tau+1)/(math.pi*A)
    CDv = CD_real_lst[i]-CDi
    Di = CDi*S*Qinfty
    Percent = CDi/CD_real_lst[i]*100
    if Percent>89.00:
        print(i)
    CDi_real_lst.append(CDi)
    CDi_percentOfCD.append(Percent)
    D_ind_real_lst.append(Di)
    CDv_real_lst.append(CDv)

#print('CDi percent', CDi_percentOfCD)

print(len(alpha_real_lst))
print(len(CL_real_lst))
print(len(CDi_real_lst))

Fake_CDi_XFLR5 = []
Fake_CDv_XFLR5 = []
for i in range(len(alpha_lstV)):
    CDi = CL_lstV[i]**2/(A*math.pi)*(1+tau)
    Fake_CDi_XFLR5.append(CDi)
    CDv = CD_lstV[i]-CDi
    Fake_CDv_XFLR5.append(CDv)

# plt.plot(alpha_lst, CL_lst, color='green',linewidth=1, marker='x', markerfacecolor='none', markersize=5, markeredgecolor='green', markeredgewidth=0.5, label='XFLR5 Results')
# plt.plot(alpha_real_lst, CL_real_lst, color='purple', linewidth=1, marker='v', markerfacecolor='none', markersize=5, markeredgecolor='purple', markeredgewidth=0.5,label='Wind Tunnel Results')
# plt.xlabel("$\\alpha$ [$\\deg$]", fontsize=12)
# plt.ylabel("$C_L$ [-]", fontsize=12)
# plt.grid(True)
# plt.legend(fontsize=12)
# plt.title("Comparison of lift curves of experimental data and XFLR5 data")
# plt.show()

# plt.subplot(1, 2, 1)
# plt.plot(alpha_lst, CD_lst, color='green', linewidth=1, marker='x', markerfacecolor='none', markersize=5, markeredgecolor='green', markeredgewidth=0.5,label='XFLR5, inviscid')
# plt.plot(alpha_lstV, CD_lstV, color='blue', linewidth=1, marker='+', markerfacecolor='none', markersize=5, markeredgecolor='blue', markeredgewidth=0.5,label='XFLR5, viscous')
# plt.plot(alpha_real_lst, CD_real_lst, color='purple', linewidth=1, marker='v', markerfacecolor='none', markersize=5, markeredgecolor='purple', markeredgewidth=0.5,label='Wind Tunnel Results')
# plt.xlabel("$\\alpha$ [$\\deg$]", fontsize=12)
# plt.ylabel("$C_D$ [-]", fontsize=12)
# plt.grid(True)
# plt.legend(fontsize=12)
# plt.title("Comparison of drag curves of experimental data and XFLR5 data")

# plt.subplot(1, 2, 2)
# plt.plot(CL_lst, CD_lst, color='green', linewidth=1, marker='x', markerfacecolor='none', markersize=5, markeredgecolor='green', markeredgewidth=0.5,label='XFLR5, inviscid')
# plt.plot(CL_lstV, CD_lstV, color='blue', linewidth=1, marker='+', markerfacecolor='none', markersize=5, markeredgecolor='blue', markeredgewidth=0.5,label='XFLR5, viscous')
# plt.plot(CL_real_lst, CD_real_lst, color='purple', linewidth=1, marker='v', markerfacecolor='none', markersize=5, markeredgecolor='purple', markeredgewidth=0.5,label='Wind Tunnel Results')
# plt.xlabel("$C_L$ [-]", fontsize=12)
# plt.ylabel("$C_D$ [-]", fontsize=12)
# plt.grid(True)
# plt.legend(fontsize=12)
# plt.title("Comparison of drag curves of experimental data and XFLR5 data")
# plt.tight_layout()
# plt.show()

plt.plot(alpha_lst, CDi_lst, color='green', linewidth=1, marker='x', markerfacecolor='none', markersize=5, markeredgecolor='green', markeredgewidth=0.5,label='XFLR5 Results')
plt.plot(alpha_lstV, Fake_CDi_XFLR5, color='blue', linewidth=1, marker='+', markerfacecolor='none', markersize=5, markeredgecolor='blue', markeredgewidth=0.5,label='XFLR5 Results with $\\delta$ from experimental data')
plt.plot(alpha_real_lst, CDi_real_lst, color='purple', linewidth=1, marker='v', markerfacecolor='none', markersize=5, markeredgecolor='purple', markeredgewidth=0.5,label='Wind Tunnel Results')
plt.xlabel("$\\alpha$ [$\\deg$]", fontsize=12)
plt.ylabel("$C_{D_i}$ [-]", fontsize=12)
plt.grid(True)
plt.legend(fontsize=11)
plt.title("Comparison of induced drag of experimental data and XFLR5 data")
plt.show()

plt.plot(alpha_real_lst, CDv_real_lst, color='green', linewidth=1, marker='x', markerfacecolor='none', markersize=5, markeredgecolor='green', markeredgewidth=0.5,label='$C_{D_0}$')
plt.plot(alpha_real_lst, CD_real_lst, color='blue', linewidth=1, marker='+', markerfacecolor='none', markersize=5, markeredgecolor='blue', markeredgewidth=0.5,label='$C_D$')
plt.plot(alpha_real_lst, CDi_real_lst, color='purple', linewidth=1, marker='v', markerfacecolor='none', markersize=5, markeredgecolor='purple', markeredgewidth=0.5,label='$C_{D_i}$')
plt.xlabel("$\\alpha$ [$\\deg$]", fontsize=12)
plt.ylabel("$C_{D}$ [-]", fontsize=12)
plt.grid(True)
plt.legend(fontsize=12)
plt.title("Incuded drag buildup (Experimental data)")
plt.show()

plt.plot(alpha_lstV, CDv_lstV, color='green', linewidth=1, marker='x', markerfacecolor='none', markersize=5, markeredgecolor='green',label='$C_{D_0}$')
plt.plot(alpha_lstV, CDi_lstV, color='blue', linewidth=1, marker='+', markerfacecolor='none', markersize=5, markeredgecolor='blue',label='$C_D$')
plt.plot(alpha_lstV, CD_lstV, color='purple', linewidth=1, marker='v', markerfacecolor='none', markersize=5, markeredgecolor='purple',label='$C_{D_i}$')
plt.xlabel("$\\alpha$ [$\\deg$]", fontsize=12)
plt.ylabel("$C_{D}$ [-]", fontsize=12)
plt.grid(True)
plt.legend(fontsize=12)
plt.title("Incuded drag buildup (Viscous XFLR5 data)")
plt.show()

plt.plot(alpha_lstV, Fake_CDv_XFLR5, color='green', linewidth=1, marker='x', markerfacecolor='none', markersize=5, markeredgecolor='green',label='$C_{D_0}$')
plt.plot(alpha_lstV, Fake_CDi_XFLR5, color='blue', linewidth=1, marker='+', markerfacecolor='none', markersize=5, markeredgecolor='blue',label='$C_{D_i}$ computed using $\\delta$')
plt.plot(alpha_lstV, CD_lstV, color='purple', linewidth=1, marker='v', markerfacecolor='none', markersize=5, markeredgecolor='purple',label='$C_{D}$ output XFLR5')
plt.xlabel("$\\alpha$ [$\\deg$]", fontsize=12)
plt.ylabel("$C_{D}$ [-]", fontsize=12)
plt.grid(True)
plt.legend(fontsize=12)
plt.title("Incuded drag buildup (Viscous XFLR5 data with $\\delta$)")
plt.show()
#print(alpha_lst)

plt.subplot(2, 2, 1)
plt.plot(alpha_lst, CDi_lst, color='green',linewidth=1, marker='x', markerfacecolor='none', markersize=5, markeredgecolor='green', markeredgewidth=0.5, label='XFLR5')
plt.plot(alpha_lstV, Fake_CDi_XFLR5, color='blue',linewidth=1, marker='+', markerfacecolor='none', markersize=5, markeredgecolor='blue', markeredgewidth=0.5, label='XFLR5 with $\\delta$ from experimental')
plt.plot(alpha_real_lst, CDi_real_lst, color='purple',linewidth=1, marker='v', markerfacecolor='none', markersize=5, markeredgecolor='purple', markeredgewidth=0.5, label='Wind Tunnel')
plt.xlabel("$\\alpha$ [$\\deg$]", fontsize=12)
plt.ylabel("$C_{D_i}$ [-]", fontsize=12)
plt.grid(True)
plt.legend(fontsize=12)
plt.title("$C_{D_i}$ of experimental data and XFLR5 data")

plt.subplot(2, 2, 2)
plt.plot(alpha_real_lst, CDv_real_lst, color='green',linewidth=1, marker='x', markerfacecolor='none', markersize=5, markeredgecolor='green', markeredgewidth=0.5, label='$C_{D_0}$')
plt.plot(alpha_real_lst, CD_real_lst, color='purple', linewidth=1, marker='v', markerfacecolor='none', markersize=5, markeredgecolor='purple', markeredgewidth=0.5,label='$C_D$')
plt.plot(alpha_real_lst, CDi_real_lst, color='blue', linewidth=1, marker='+', markerfacecolor='none', markersize=5, markeredgecolor='blue', markeredgewidth=0.5,label='$C_{D_i}$')
plt.xlabel("$\\alpha$ [$\\deg$]", fontsize=12)
plt.ylabel("$C_{D}$ [-]", fontsize=12)
plt.grid(True)
plt.legend(fontsize=12)
plt.title("Drag buildup - Experimental data")

plt.subplot(2, 2, 3)
plt.plot(alpha_lstV, CDv_lstV, color='green',linewidth=1,   label='$C_{D_0}$',marker='x', markerfacecolor='none', markersize=5, markeredgecolor='green',markeredgewidth=0.5)
plt.plot(alpha_lstV, CDi_lstV, color='blue',linewidth=1,  label='$C_{D_i}$',marker='+', markerfacecolor='none', markersize=5, markeredgecolor='blue',markeredgewidth=0.5)
plt.plot(alpha_lstV, CD_lstV, color='purple',linewidth=1, label='$C_{D}$',marker='v', markerfacecolor='none', markersize=5, markeredgecolor='purple', markeredgewidth=0.5)
plt.xlabel("$\\alpha$ [$\\deg$]", fontsize=12)
plt.ylabel("$C_{D}$ [-]", fontsize=12)
plt.grid(True)
plt.legend(fontsize=12)
plt.title("Drag buildup - Viscous XFLR5 data")

plt.subplot(2, 2, 4)
plt.plot(alpha_lstV, Fake_CDv_XFLR5, color='green',linewidth=1, marker='x', markerfacecolor='none', markersize=5, markeredgecolor='green', markeredgewidth=0.5,label='$C_{D_0}$')
plt.plot(alpha_lstV, Fake_CDi_XFLR5, color='blue', linewidth=1, marker='+', markerfacecolor='none', markersize=5, markeredgecolor='blue', markeredgewidth=0.5,label='$C_{D_i}$ computed using $\\delta$')
plt.plot(alpha_lstV, CD_lstV, color='purple',linewidth=1, marker='v', markerfacecolor='none', markersize=5, markeredgecolor='purple', markeredgewidth=0.5,label='$C_{D}$ output XFLR5')
plt.xlabel("$\\alpha$ [$\\deg$]", fontsize=12)
plt.ylabel("$C_{D}$ [-]", fontsize=12)
plt.grid(True)
plt.legend(fontsize=12)
plt.title("Drag buildup - Viscous XFLR5 data with $\\delta$")
plt.tight_layout()
plt.show()