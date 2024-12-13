import numpy as np
import scipy as sp


S = 0.16*0.4169

CL_min = 0.00
CL12 = 0.00

Cm_min = 0.00
Cm12 = 0.00

CD0_min = 0.000
CD12 = 0.000
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

ylst0 = y_span[18:]
chordlst0 = chord[18:]
Ailst0 = Ai[18:]
Cllst0 = Cl[18:]
Cdlst0 = ICd[18:]
Cmlst0 = CmAirf[18:]

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
    y_span10,
    chord10,
    Ai10,
    Cl10,
    PCd10,
    ICd10,
    CmGeom10,
    CmAirf10,
    XTrtop10,
    XTrBot10,
    XCP10,
    BM10,
) = ([], [], [], [], [], [], [], [], [], [], [], [])

# Process each line to extract the values
for line in data_lines:
    # Strip leading/trailing spaces and split by any whitespace (tabs, spaces, etc.)
    columns = line.strip().split()

    # Ensure there are enough columns in each line (12 columns)
    if len(columns) == 12:
        try:
            # Append the values to the respective lists
            y_span10.append(float(columns[0]))
            chord10.append(float(columns[1]))
            Ai10.append(float(columns[2]))
            Cl10.append(float(columns[3]))
            PCd10.append(float(columns[4]))
            ICd10.append(float(columns[5]))
            CmGeom10.append(float(columns[6]))
            CmAirf10.append(float(columns[7]))
            XTrtop10.append(float(columns[8]))
            XTrBot10.append(float(columns[9]))
            XCP10.append(float(columns[10]))
            BM10.append(float(columns[11]))
        except ValueError as e:
            print(f"Error converting data: {e} in line: {line}")
            continue

ylst10 = y_span10[18:]
chordlst10 = chord10[18:]
Ailst10 = Ai10[18:]
Cllst10 = Cl10[18:]
Cdlst10 = ICd10[18:]
Cmlst10 = CmAirf10[18:]
# print(ylst0)  # comment


def interpolate(x, y):
    f = sp.interpolate.interp1d(x, y, kind="linear", fill_value="extrapolate")
    return f


CL0_inter = interpolate(ylst0, Cllst0)
CD0_inter = interpolate(ylst0, Cdlst0)
Cm0_inter = interpolate(ylst0, Cmlst0)
Ai0_inter = interpolate(ylst0, Ailst0)


CL10_inter = interpolate(ylst10, Cllst10)
CD10_inter = interpolate(ylst10, Cdlst10)
Cm10_inter = interpolate(ylst10, Cmlst10)
Ai10_inter = interpolate(ylst10, Ailst10)

chord_inter = interpolate(y_span, chord)


def CLdistr(y, CLd):
    m = (CLd - CL0) / (CL10 - CL0)
    return CL0_inter(y) + m * (CL10_inter(y) - CL0_inter(y))


def CDdistr(y, CDd):
    m = (CDd - CD0) / (CD10 - CD0)
    return CD0_inter(y) + m * (CD10_inter(y) - CD0_inter(y))


def Cmdistr(y, Cmd):
    m = (Cmd - Cm0) / (Cm10 - Cm0)
    return Cm0_inter(y) + m * (Cm10_inter(y) - Cm0_inter(y))


def Aidistr(y, Ad):
    m = Ad / 10
    return Ai0_inter(y) + m * (Ai10_inter(y) - Ai0_inter(y))


CLalpha = sp.interpolate.interp1d(
    [CL0, CL10], [0, 10], kind="linear", fill_value="extrapolate"
)

CLCD = sp.interpolate.interp1d(
    [CL0, CL10], [CD0, CD10], kind="linear", fill_value="extrapolate"
)

CLCm = sp.interpolate.interp1d(
    [CL0, CL10], [Cm0, Cm10], kind="linear", fill_value="extrapolate"
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
