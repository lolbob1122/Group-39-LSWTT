import numpy as np
import scipy as sp


S = 0.16*0.4169

CL_min = 0.00
CL_max = 0.00

Cm_min = 0.00
Cm_max = 0.00

CD_min = 0.000
CD_max = 0.000
CLd_test = 0.5  # Change val
Cmd_test = 0.5  # Change val
Cdd_test = 0.5  # Change val

# Read the text file and extract data from the "Main Wing" section
with open("XFLR5textfiles/MainWing_a=-5.00_v=21.00ms.txt", "r") as file:
    lines = file.readlines()

# Print the first few lines to confirm file is being read correctly
# print("First few lines of the file:")
# print("".join(lines[:10]))  # Print the first 10 lines for verification

# Find the start of the "Main Wing" data
start_idx = None
for i, line in enumerate(lines):
    if "Main Wing" in line.strip():  # Search for the "Main Wing" line
        start_idx = (
            i + 2
        )  # Skip the header and start with the data (2 lines after "Main Wing")
        break

# Check if we found the "Main Wing" section
if start_idx is None:
    print("Error: 'Main Wing' section not found!")
else:
    # print(f"Data starts from line {start_idx}")
    pass

# Extract the rows under the "Main Wing" section
data_lines = lines[start_idx:]

# Initialize lists to store the extracted columns
y_span, chord, Ai, Cl, PCd, ICd, CmGeom, CmAirf, XTrtop, XTrBot, XCP, BM = (
    [],
    [],
    [],
    [],
    [],
    [],
    [],
    [],
    [],
    [],
    [],
    [],
)

# Process each line to extract the values
for line in data_lines:
    # Strip leading/trailing spaces and split by any whitespace (tabs, spaces, etc.)
    columns = line.strip().split()

    # Ensure there are enough columns in each line (12 columns)
    if len(columns) == 12:
        try:
            # Append the values to the respective lists
            y_span.append(float(columns[0]))
            chord.append(float(columns[1]))
            Ai.append(float(columns[2]))
            Cl.append(float(columns[3]))
            PCd.append(float(columns[4]))
            ICd.append(float(columns[5]))
            CmGeom.append(float(columns[6]))
            CmAirf.append(float(columns[7]))
            XTrtop.append(float(columns[8]))
            XTrBot.append(float(columns[9]))
            XCP.append(float(columns[10]))
            BM.append(float(columns[11]))
        except ValueError as e:
            print(f"Error converting data: {e} in line: {line}")
            continue

ylst_min = y_span[18:]
chordlst_min = chord[18:]
Ailst_min = Ai[18:]
Cllst_min = Cl[18:]
Cdlst_min = ICd[18:]
Cmlst_min = CmAirf[18:]

# Read the text file and extract data from the "Main Wing" section
with open("XFLR5textfiles/MainWing_a=12.00_v=21.00ms.txt.txt", "r") as file:
    lines = file.readlines()

# Print the first few lines to confirm file is being read correctly
# print("First few lines of the file:")
# print("".join(lines[:10]))  # Print the first 10 lines for verification

# Find the start of the "Main Wing" data
start_idx = None
for i, line in enumerate(lines):
    if "Main Wing" in line.strip():  # Search for the "Main Wing" line
        start_idx = (
            i + 2
        )  # Skip the header and start with the data (2 lines after "Main Wing")
        break

# Check if we found the "Main Wing" section
if start_idx is None:
    print("Error: 'Main Wing' section not found!")
else:
    # print(f"Data starts from line {start_idx}")
    pass

# Extract the rows under the "Main Wing" section
data_lines = lines[start_idx:]

# Initialize lists to store the extracted columns
(
    y_span_max,
    chord_max,
    Ai_max,
    Cl_max,
    PCd_max,
    ICd_max,
    CmGeom_max,
    CmAirf_max,
    XTrtop_max,
    XTrBot_max,
    XCP_max,
    BM_max,
) = ([], [], [], [], [], [], [], [], [], [], [], [])

# Process each line to extract the values
for line in data_lines:
    # Strip leading/trailing spaces and split by any whitespace (tabs, spaces, etc.)
    columns = line.strip().split()

    # Ensure there are enough columns in each line (12 columns)
    if len(columns) == 12:
        try:
            # Append the values to the respective lists
            y_span_max.append(float(columns[0]))
            chord_max.append(float(columns[1]))
            Ai_max.append(float(columns[2]))
            Cl_max.append(float(columns[3]))
            PCd_max.append(float(columns[4]))
            ICd_max.append(float(columns[5]))
            CmGeom_max.append(float(columns[6]))
            CmAirf_max.append(float(columns[7]))
            XTrtop_max.append(float(columns[8]))
            XTrBot_max.append(float(columns[9]))
            XCP_max.append(float(columns[10]))
            BM_max.append(float(columns[11]))
        except ValueError as e:
            print(f"Error converting data: {e} in line: {line}")
            continue

ylst_max = y_span_max[18:]
chordlst_max = chord_max[18:]
Ailst_max = Ai_max[18:]
Cllst_max = Cl_max[18:]
Cdlst_max = ICd_max[18:]
Cmlst_max = CmAirf_max[18:]
# print(ylst0)  # comment


def interpolate(x, y):
    f = sp.interpolate.interp1d(x, y, kind="linear", fill_value="extrapolate")
    return f


CL0_inter = interpolate(ylst_min, Cllst_min)
CD0_inter = interpolate(ylst_min, Cdlst_min)
Cm0_inter = interpolate(ylst_min, Cmlst_min)
Ai0_inter = interpolate(ylst_min, Ailst_min)


CL10_inter = interpolate(ylst_max, Cllst_max)
CD10_inter = interpolate(ylst_max, Cdlst_max)
Cm10_inter = interpolate(ylst_max, Cmlst_max)
Ai10_inter = interpolate(ylst_max, Ailst_max)

chord_inter = interpolate(y_span, chord)


def CLdistr(y, CLd):
    m = (CLd - CL_min) / (CL_max - CL_min)
    return CL0_inter(y) + m * (CL10_inter(y) - CL0_inter(y))


def CDdistr(y, CDd):
    m = (CDd - CD_min) / (CD_max - CD_min)
    return CD0_inter(y) + m * (CD10_inter(y) - CD0_inter(y))


def Cmdistr(y, Cmd):
    m = (Cmd - Cm_min) / (Cm_max - Cm_min)
    return Cm0_inter(y) + m * (Cm10_inter(y) - Cm0_inter(y))


def Aidistr(y, Ad):
    m = Ad / 10
    return Ai0_inter(y) + m * (Ai10_inter(y) - Ai0_inter(y))


CLalpha = sp.interpolate.interp1d(
    [CL_min, CL_max], [0, 10], kind="linear", fill_value="extrapolate"
)

CLCD = sp.interpolate.interp1d(
    [CL_min, CL_max], [CD_min, CD_max], kind="linear", fill_value="extrapolate"
)

CLCm = sp.interpolate.interp1d(
    [CL_min, CL_max], [Cm_min, Cm_max], kind="linear", fill_value="extrapolate"
)


# angle of attack used to transform L and D to Norm and Tang
def alpha(mass, n, rho, V):  # in degrees
    case_CL = (mass * 9.81 * n) / (0.5 * rho * (V**2) * S)
    return CLalpha(case_CL) * np.pi / 180  # radians


def Lift(y, rho, V, mass, n):
    case_CL = (mass * 9.81 * n) / (0.5 * rho * (V**2) * S)
    return 0.5 * rho * (V**2) * CLdistr(y, case_CL) * chord_inter(y)


def Drag(y, rho, V, mass, n):
    case_CL = (mass * 9.81 * n) / (0.5 * rho * (V**2) * S)
    CD = CLCD(case_CL)
    return 0.5 * rho * (V**2) * CDdistr(y, CD) * chord_inter(y)


def Moment(y, rho, V, mass, n):
    case_CL = (mass * 9.81 * n) / (0.5 * rho * (V**2) * S)
    Cm = CLCm(case_CL)

    return 0.5 * rho * (V**2) * Cmdistr(y, Cm) * chord_inter(y) ** 2


def Alphaind(y, rho, V, mass, n):
    case_CL = (mass * 9.81 * n) / (0.5 * rho * (V**2) * S)
    alpha = CLalpha(case_CL)
    return Aidistr(y, alpha) * np.pi / 180


# fig, axs = plt.subplots(3, 2)
# axs[0][0].plot(ylst0, Lift(ylst0, 1.225, 10, 1000, 4))
# axs[0][0].set_title("Spanwise Lift Distr")

# axs[1][0].plot(ylst0, Drag(ylst0, 1.225, 10, 1000, 4))
# axs[1][0].set_title("Spanwise Drag Distr")

# axs[2][0].plot(ylst0, Moment(ylst0, 1.225, 10, 1000, 4))
# axs[2][0].set_title("Spanwise Moment Distr")

# axs[0][1].plot(ylst0, Alphaind(ylst0, 1.225, 10, 1000, 4))
# axs[0][1].set_title("Spanwise Alpha induced Distr")


# axs[1][1].plot(ylst0, CLdistr(ylst0,0.928089))
# axs[1][1].set_title("Spanwise CL Distr")

# plt.show()
