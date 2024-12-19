from math import pi
import numpy as np

# Read the text file and extract data from the "Freestream speed" section
with open("Experimental\\2D\\AE2130II_Coordinates.txt", "r") as file:
    lines = file.readlines()

# Find the start of the "Freestream speed" data
start_idx = None
for i, line in enumerate(lines):
    if "SD6060-104-88_180" in line.strip():  # Search for the "Freestream speed" line
        start_idx = (
            i + 1
        )  # Skip the header and start with the data (2 lines after "Freestream speed")
        break

# Check if we found the "Freestream speed" section
if start_idx is None:
    print("Error: 'SD6060-104-88_180' section not found!")
else:
    # print(f"Data starts from line {start_idx}")
    pass

# Extract the rows under the "Freestream speed" section
data_lines = lines[start_idx:]

# Initialize lists to store the extracted columns
(
    xCoord,
    yCoord,
) = ([], [])

# Process each line to extract the values
for line in data_lines:
    # Strip leading/trailing spaces and split by any whitespace (tabs, spaces, etc.)
    line = line.replace(',', '')
    columns = line.strip().split()

    # Ensure there are enough columns in each line (12 columns)
    if len(columns) == 2:
        try:
            # Append the values to the respective lists
            xCoord.append(0.16*float(columns[0]))
            yCoord.append(0.16*float(columns[1]))
        except ValueError as e:
            print(f"Error converting data: {e} in line: {line}")
            continue


def polygonArea(x, y):
    # Ensure the number of points is greater than 2
    if len(x) != len(y) or len(x) < 3:
        raise ValueError("There must be at least 3 points")

    n = len(x)
    area = 0

    # Apply the Shoelace Theorem
    for i in range(n):
        j = (i + 1) % n  # Next point, wrap around to the first point at the end
        area += x[i] * y[j] - y[i] * x[j]

    return abs(area) / 2
Area = polygonArea(xCoord, yCoord)
print(Area)

def get_corrected_CdClCmalpha(U_infty, T_infty, Cd_u, Cdm, Cdi, Cl_u, Cm_u, alpha_u, q_infty, rho, mu):
    M = U_infty/(1.4*287*T_infty)**0.5
    beta = (1-M**2)**0.5
    tcRatio = 0.1037
    c = 0.16  # m
    h = 1.25  # change value
    A = Area  # change value
    Cd_s = Cd_u-Cdi-Cdm
    Re_u = c*rho*U_infty/mu

    # Interference factors
    Es = 0.524*(1+1.2*beta*tcRatio)*A/(beta**3*h**2)
    Ew = 0.25*c/h*(1+0.4*M**2)/(beta**2)*Cd_u
    Esep = 0.5*0.96*c/h*Cd_s
    Et = Es+Ew+Esep

    # Coefficient changes
    DeltaCd_g = -(Cdm+Cd_s)*(1+0.4*M**2)*Es
    DeltaAlpha = pi*c**2/(96*beta*h**2)*(Cl_u+4*Cm_u)-7*pi**3*c**4*Cl_u/(30720*beta**3*h**4)
    DeltaCl = Cl_u*(-pi**2/48*(c/(beta*h))**2+7*pi**4/3072*(c/(beta*h))**4)
    DeltaCm = Cl_u*(pi**2/192*(c/(beta*h))**2-7*pi**4/15360*(c/(beta*h))**4)

    # Ambient changes
    Vc = U_infty*(1+Et)
    q_c = q_infty*(1+Et*(2.0-M**2))
    Re_c = (1-0.7*M**2)*Et*Re_u

    # Final alpha and coefficients 
    alpha_c = alpha_u + DeltaAlpha
    Cl_c = (Cl_u+DeltaCl)*q_infty/q_c
    Cd_c = (Cd_u+DeltaCd_g)*q_infty/q_c
    Cm_c = (Cl_u+DeltaCm)*q_infty/q_c

    return alpha_c, Cd_c, Cl_c, Cm_c, Vc, Re_c
