import numpy as np
import scipy as sp
import math


S = 0.16*0.4169
A = 0.4169**2/S

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

alpha_lst = alpha[:35]
CL_lst = CL[:35]
CDi_lst = CDi[:35]
CD_lst = CD[:35]
Qinf_lst = Qinf[:35]
#print(alpha_lst)

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


# def interpolate(x, y):
#     f = sp.interpolate.interp1d(x, y, kind="linear", fill_value="extrapolate")
#     return f


# CL0_inter = interpolate(ylst_min, Cllst_min)
# CD0_inter = interpolate(ylst_min, Cdlst_min)
# Cm0_inter = interpolate(ylst_min, Cmlst_min)
# Ai0_inter = interpolate(ylst_min, Ailst_min)


# CL10_inter = interpolate(ylst_max, Cllst_max)
# CD10_inter = interpolate(ylst_max, Cdlst_max)
# Cm10_inter = interpolate(ylst_max, Cmlst_max)
# Ai10_inter = interpolate(ylst_max, Ailst_max)

# chord_inter = interpolate(y_span, chord)


# def CLdistr(y, CLd):
#     m = (CLd - CL_min) / (CL_max - CL_min)
#     return CL0_inter(y) + m * (CL10_inter(y) - CL0_inter(y))


# def CDdistr(y, CDd):
#     m = (CDd - CD_min) / (CD_max - CD_min)
#     return CD0_inter(y) + m * (CD10_inter(y) - CD0_inter(y))


# def Cmdistr(y, Cmd):
#     m = (Cmd - Cm_min) / (Cm_max - Cm_min)
#     return Cm0_inter(y) + m * (Cm10_inter(y) - Cm0_inter(y))


# def Aidistr(y, Ad):
#     m = Ad / 10
#     return Ai0_inter(y) + m * (Ai10_inter(y) - Ai0_inter(y))


# CLalpha = sp.interpolate.interp1d(
#     [CL_min, CL_max], [0, 10], kind="linear", fill_value="extrapolate"
# )

# CLCD = sp.interpolate.interp1d(
#     [CL_min, CL_max], [CD_min, CD_max], kind="linear", fill_value="extrapolate"
# )

# CLCm = sp.interpolate.interp1d(
#     [CL_min, CL_max], [Cm_min, Cm_max], kind="linear", fill_value="extrapolate"
# )


# # angle of attack used to transform L and D to Norm and Tang
# def alpha(mass, n, rho, V):  # in degrees
#     case_CL = (mass * 9.81 * n) / (0.5 * rho * (V**2) * S)
#     return CLalpha(case_CL) * np.pi / 180  # radians


# def Lift(y, rho, V, mass, n):
#     case_CL = (mass * 9.81 * n) / (0.5 * rho * (V**2) * S)
#     return 0.5 * rho * (V**2) * CLdistr(y, case_CL) * chord_inter(y)


# def Drag(y, rho, V, mass, n):
#     case_CL = (mass * 9.81 * n) / (0.5 * rho * (V**2) * S)
#     CD = CLCD(case_CL)
#     return 0.5 * rho * (V**2) * CDdistr(y, CD) * chord_inter(y)


# def Moment(y, rho, V, mass, n):
#     case_CL = (mass * 9.81 * n) / (0.5 * rho * (V**2) * S)
#     Cm = CLCm(case_CL)

#     return 0.5 * rho * (V**2) * Cmdistr(y, Cm) * chord_inter(y) ** 2


# def Alphaind(y, rho, V, mass, n):
#     case_CL = (mass * 9.81 * n) / (0.5 * rho * (V**2) * S)
#     alpha = CLalpha(case_CL)
#     return Aidistr(y, alpha) * np.pi / 180


# # fig, axs = plt.subplots(3, 2)
# # axs[0][0].plot(ylst0, Lift(ylst0, 1.225, 10, 1000, 4))
# # axs[0][0].set_title("Spanwise Lift Distr")

# # axs[1][0].plot(ylst0, Drag(ylst0, 1.225, 10, 1000, 4))
# # axs[1][0].set_title("Spanwise Drag Distr")

# # axs[2][0].plot(ylst0, Moment(ylst0, 1.225, 10, 1000, 4))
# # axs[2][0].set_title("Spanwise Moment Distr")

# # axs[0][1].plot(ylst0, Alphaind(ylst0, 1.225, 10, 1000, 4))
# # axs[0][1].set_title("Spanwise Alpha induced Distr")


# # axs[1][1].plot(ylst0, CLdistr(ylst0,0.928089))
# # axs[1][1].set_title("Spanwise CL Distr")

# # plt.show()
