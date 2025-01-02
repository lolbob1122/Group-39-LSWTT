from math import pi, sin, sqrt
import numpy as np
import csv
import matplotlib.pyplot as plt

# Constants
mu_zero = 1.716 * 10**(-5) # kg/m*s
T_zero = 273.15 # K
S = 110.4 # K
R = 287 # J/kg*K
c = 0.16 # m 

def get_ambient_results_new(): # makes a function so luca can call it
##############################
    # Reads csv file to find all values for p, delta p and T
    with open ('Experimental\\2D\\converted_2DCopy.csv', 'r') as raw_2D_data: 
        reader = csv.reader(raw_2D_data)
        P_bar = []
        T = []
        Delta_P = []
        alpha = []
        for row in reader:
            P_bar.append(100*float(row[4]))  #converted to pascals
            T.append(273.15+float(row[5]))  #converted to K
            Delta_P.append(float(row[3]))
            alpha.append(float(row[2]))
    alpha_lst = alpha
    T_lst = T
    mu_lst = []
    q_inf_lst = []
    rho_lst = []
    P_s_lst = []
    U_inf_lst = []
    Re_lst = []
    for i in range(len(T)):
        mu = mu_zero * (( T[i] / T_zero ) ** ( 3 / 2 )) * (( T_zero + S )/( T[i] + S )) 
        q_inf = 0.211804 + 1.928442 * Delta_P[i] + (1.879374 * 10 ** (-4)) * Delta_P[i] ** 2
        rho = P_bar[i] / (R * T[i])
        P_s = P_bar[i] - q_inf
        U_inf = sqrt((2 * q_inf)/rho)
        Re = (rho * U_inf * c) / mu

        mu_lst.append(mu)
        q_inf_lst.append(q_inf)
        rho_lst.append(rho)
        P_s_lst.append(P_s)
        U_inf_lst.append(U_inf)
        Re_lst.append(Re)

    return (mu_lst, q_inf_lst, rho_lst, P_s_lst, U_inf_lst, Re_lst, alpha_lst, T_lst)

mu_List = get_ambient_results_new()[0]
q_inf_List = get_ambient_results_new()[1]
rho_List = get_ambient_results_new()[2]
U_inf_List = get_ambient_results_new()[4]
Re_List = get_ambient_results_new()[5]
alpha_List = get_ambient_results_new()[6]
T_infty = get_ambient_results_new()[7]

# Test data !!! NOT REAL !!!

# np.linspace(-0.3, 1.2, 68):
Cl_u_test = [-0.3, -0.27761194, -0.25522388, -0.23283582, -0.21044776, -0.1880597, -0.16567164, -0.14328358, -0.12089552, -0.09850746, -0.0761194, -0.05373134, -0.03134328, -0.00895522, 0.01343284, 0.0358209, 0.05820896, 0.08059701, 0.10298507, 0.12537313, 0.14776119, 0.17014925, 0.19253731, 0.21492537, 0.23731343, 0.25970149, 0.28208955, 0.30447761, 0.32686567, 0.34925373, 0.37164179, 0.39402985, 0.41641791, 0.43880597, 0.46119403, 0.48358209, 0.50597015, 0.52835821, 0.55074627, 0.57313433, 0.59552239, 0.61791045, 0.64029851, 0.66268657, 0.68507463, 0.70746269, 0.72985075, 0.75223881, 0.77462687, 0.79701493, 0.81940299, 0.84179104, 0.8641791, 0.88656716, 0.90895522, 0.93134328, 0.95373134, 0.9761194, 0.99850746, 1.02089552, 1.04328358, 1.06567164, 1.0880597, 1.11044776, 1.13283582, 1.15522388, 1.17761194, 1.2]

# np.linspace(0, 1.4, 68):
Cd_u_test = [0.0, 0.02089552, 0.04179104, 0.06268657, 0.08358209, 0.10447761, 0.12537313, 0.14626866, 0.16716418, 0.1880597, 0.20895522, 0.22985075, 0.25074627, 0.27164179, 0.29253731, 0.31343284, 0.33432836, 0.35522388, 0.3761194, 0.39701493, 0.41791045, 0.43880597, 0.45970149, 0.48059701, 0.50149254, 0.52238806, 0.54328358, 0.5641791, 0.58507463, 0.60597015, 0.62686567, 0.64776119, 0.66865672, 0.68955224, 0.71044776, 0.73134328, 0.75223881, 0.77313433, 0.79402985, 0.81492537, 0.8358209, 0.85671642, 0.87761194, 0.89850746, 0.91940299, 0.94029851, 0.96119403, 0.98208955, 1.00298507, 1.0238806, 1.04477612, 1.06567164, 1.08656716, 1.10746269, 1.12835821, 1.14925373, 1.17014925, 1.19104478, 1.2119403, 1.23283582, 1.25373134, 1.27462687, 1.29552239, 1.31641791, 1.33731343, 1.35820896, 1.37910448, 1.4]

# np.linspace(-0.04, 0.11, 68):
Cm_u_test = [-0.04, -0.03776119, -0.03552239, -0.03328358, -0.03104478, -0.02880597, -0.02656716, -0.02432836, -0.02208955, -0.01985075, -0.01761194, -0.01537313, -0.01313433, -0.01089552, -0.00865672, -0.00641791, -0.0041791, -0.0019403, 0.00029851, 0.00253731, 0.00477612, 0.00701493, 0.00925373, 0.01149254, 0.01373134, 0.01597015, 0.01820896, 0.02044776, 0.02268657, 0.02492537, 0.02716418, 0.02940299, 0.03164179, 0.0338806, 0.0361194, 0.03835821, 0.04059701, 0.04283582, 0.04507463, 0.04731343, 0.04955224, 0.05179104, 0.05402985, 0.05626866, 0.05850746, 0.06074627, 0.06298507, 0.06522388, 0.06746269, 0.06970149, 0.0719403, 0.0741791, 0.07641791, 0.07865672, 0.08089552, 0.08313433, 0.08537313, 0.08761194, 0.08985075, 0.09208955, 0.09432836, 0.09656716, 0.09880597, 0.10104478, 0.10328358, 0.10552239, 0.10776119, 0.11]

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

def get_corrected_CdClCmalpha_lst(T_infty, Cd_u, Cl_u, Cm_u, alpha_u, q_infty, rho):
    Es_lst = []
    Ew_lst = []
    Esep_lst = []
    Et_lst = []
    alpha_c_lst = []
    Cl_c_lst = []
    Cd_c_lst = []
    Cm_c_lst = []
    q_inf_ratio_lst = []
    Re_ratio_lst = []

    Cdm = min(Cd_u)
    for i in range(len(alpha_u)):
        mu = mu_zero * ((T_infty[i] / T_zero ) ** ( 3 / 2 )) * (( T_zero + S )/( T_infty[i] + S )) 
        U_infty = (q_infty[i]/(0.5*rho[i]))**0.5
        M = U_infty/(1.4*287*T_infty[i])**0.5
        beta = (1-M**2)**0.5
        tcRatio = 0.1037
        c = 0.16  # m
        h = 1.25  # change value
        A = Area  # change value
        Cdi = Cl_u[i]*sin(alpha_u[i]/180*pi)  # Check and add Cdi to variable input for function 
        Cd_s = Cd_u[i]-Cdi-Cdm
        Re_u = c*rho[i]*U_infty/mu

        # Interference factors
        Es = 0.524*(1+1.2*beta*tcRatio)*A/(beta**3*h**2)
        Ew = 0.25*c/h*(1+0.4*M**2)/(beta**2)*Cd_u[i]
        Esep = 0.5*0.96*c/h*Cd_s
        Et = Es+Ew+Esep

        # Coefficient changes
        DeltaCd_g = -(Cdm+Cd_s)*(1+0.4*M**2)*Es
        DeltaAlpha = pi*c**2/(96*beta*h**2)*(Cl_u[i]+4*Cm_u[i])-7*pi**3*c**4*Cl_u[i]/(30720*beta**3*h**4)
        DeltaCl = Cl_u[i]*(-pi**2/48*(c/(beta*h))**2+7*pi**4/3072*(c/(beta*h))**4)
        DeltaCm = Cl_u[i]*(pi**2/192*(c/(beta*h))**2-7*pi**4/15360*(c/(beta*h))**4)

        # Ambient changes
        Vc = U_infty*(1+Et)
        q_c = q_infty[i]*(1+Et*(2.0-M**2))
        Re_c = (1-0.7*M**2)*Et*Re_u

        q_inf_ratio_lst.append(q_infty[i]/q_c)
        Re_ratio_lst.append(Re_u/Re_c)


        # Final alpha and coefficients 
        alpha_c = alpha_u[i] + DeltaAlpha
        Cl_c = (Cl_u[i]+DeltaCl)*q_infty[i]/q_c
        Cd_c = (Cd_u[i]+DeltaCd_g)*q_infty[i]/q_c
        Cm_c = (Cl_u[i]+DeltaCm)*q_infty[i]/q_c

        # Add results to lists
        Es_lst.append(Es)
        Ew_lst.append(Ew)
        Esep_lst.append(Esep)
        Et_lst.append(Et)
        alpha_c_lst.append(alpha_c)
        Cl_c_lst.append(Cl_c)
        Cd_c_lst.append(Cd_c)
        Cm_c_lst.append(Cm_c)

    plt.plot(alpha_c_lst, Es_lst, color='red', label='$\\epsilon_s$')
    plt.plot(alpha_c_lst, Ew_lst, color='green', label='$\\epsilon_w$')
    plt.plot(alpha_c_lst, Esep_lst, color='blue', label='$\\epsilon_{sep}$')
    plt.plot(alpha_c_lst, Et_lst, color='black', label='$\\epsilon_t$')
    plt.xlabel("$\\alpha_c$ [$\\deg$]")
    plt.ylabel("Interference factors $\\epsilon$ [-]")
    plt.grid(True)
    plt.legend()
    plt.title("Variation of interference factors with $\\alpha_c$")
    plt.show()

    plt.plot(alpha_u, q_inf_ratio_lst, color='red', label='$\\frac{q_{\\infty_u}}{q_{\\infty_c}}$')
    plt.plot(alpha_u, Re_ratio_lst, color='green', label='$\\frac{Re_u}{Re_c}$')
    plt.xlabel("$\\alpha$ [$\\deg$]")
    plt.ylabel("Ratio's of uncorrected to corrected flow properties")
    plt.grid(True)
    plt.legend()
    plt.title("Ratio's of corrected flow properties")
    plt.show()

    plt.plot(alpha_u, Es_lst, color='red', label='$\\epsilon_s$')
    plt.plot(alpha_u, Ew_lst, color='green', label='$\\epsilon_w$')
    plt.plot(alpha_u, Esep_lst, color='blue', label='$\\epsilon_{sep}$')
    plt.plot(alpha_u, Et_lst, color='black', label='$\\epsilon_t$')
    plt.xlabel("$\\alpha_u$ [$\\deg$]")
    plt.ylabel("Interference factors $\\epsilon$ [-]")
    plt.grid(True)
    plt.legend()
    plt.title("Variation of interference factors with $\\alpha_u$")
    plt.show()

    plt.plot(alpha_c_lst, Cl_c_lst, color='red', label='$C_{l_c}$')
    plt.plot(alpha_u, Cl_u, color='blue', label='$C_{l_u}$')
    plt.xlabel("$\\alpha$ [$\\deg$]")
    plt.ylabel("Lift coefficient $C_l$ [-]")
    plt.grid(True)
    plt.legend()
    plt.title("Lift curve comparison")
    plt.show()

    plt.plot(alpha_c_lst, Cd_c_lst, color='red', label='$C_{d_c}$')
    plt.plot(alpha_u, Cd_u, color='blue', label='$C_{d_u}$')
    plt.xlabel("$\\alpha$ [$\\deg$]")
    plt.ylabel("Drag coefficient $C_d$ [-]")
    plt.grid(True)
    plt.legend()
    plt.title("Drag curve comparison")
    plt.show()

    plt.plot(Cd_c_lst, Cl_c_lst, color='red', label='Corrected')
    plt.plot(Cd_u, Cl_u, color='blue', label='Uncorrected')
    plt.xlabel("Drag coefficient $C_d$ [-]")
    plt.ylabel("Lift coefficient $C_l$ [-]")
    plt.grid(True)
    plt.legend()
    plt.title("Drag polar comparison")
    plt.show()

    plt.plot(alpha_c_lst, Cm_c_lst, color='red', label='$C_{m_c}$')
    plt.plot(alpha_u, Cm_u, color='blue', label='$C_{m_u}$')
    plt.xlabel("$\\alpha$ [$\\deg$]")
    plt.ylabel("Moment coefficient $C_m$ [-]")
    plt.grid(True)
    plt.legend()
    plt.title("Moment coefficient comparison")
    plt.show()
    return alpha_c_lst, Cl_c_lst, Cd_c_lst, Cm_c_lst

print(get_corrected_CdClCmalpha_lst(T_infty, Cd_u_test, Cl_u_test, Cm_u_test, alpha_List, q_inf_List, rho_List))