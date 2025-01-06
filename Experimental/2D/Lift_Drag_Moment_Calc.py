import numpy as np
from scipy.integrate import trapezoid  # Import trapezoid instead of using np.trapz
import Cp_Calculator as CC  # Importing your existing function
import matplotlib.pyplot as plt

def calculate_cn(Cp_upper, x_upper, Cp_lower, x_lower):
    """
    Calculate normal force coefficient Cn using numerical integration.
    Handles non-uniform spacing and unequal number of points.
    """
    # Ensure numpy arrays for consistency
    Cp_upper = np.array(Cp_upper)
    Cp_lower = np.array(Cp_lower)
    x_upper = np.array(x_upper)
    x_lower = np.array(x_lower)

    # Use scipy.integrate.trapezoid for numerical integration with non-uniform spacing
    integral_upper = 0 # Integral of Cp over x/c (upper)
    for i in range(len(Cp_upper)-1):
        integral_upper += (Cp_upper[i]+Cp_upper[i+1])/2*(-x_upper[i]+x_upper[i+1])
    integral_lower = 0 # Integral of Cp over x/c (lower)
    for i in range(len(Cp_lower)-1):
        integral_lower += (Cp_lower[i]+Cp_lower[i+1])/2*(-x_lower[i]+x_lower[i+1])
    # Compute final Cn
    Cn = integral_lower - integral_upper
    return Cn

def calculate_cm(Cp_upper, x_upper, Cp_lower, x_lower):
    """
    Calculate the moment coefficient Cm using the given equation.
    Assumes that x and Cp values are already normalized.
    """
    # Ensure numpy arrays for consistency
    Cp_upper = np.array(Cp_upper)
    Cp_lower = np.array(Cp_lower)
    x_upper = np.array(x_upper)
    x_lower = np.array(x_lower)

    # Compute the two separate integrals
    integral_upper = trapezoid(Cp_upper * x_upper, x_upper)
    integral_lower = trapezoid(Cp_lower * x_lower, x_lower)

    # Cm is the difference between the two integrals
    Cm = integral_upper - integral_lower
    return Cm

def calculate_cd(Cp_upper, dydx_upper, Cp_lower, dydx_lower, x_upper, x_lower):
    p_upper = Cp_upper[:-1]
    p_lower = Cp_lower[:-1]
    p_upper = np.array(p_upper, dtype=float)
    p_lower = np.array(p_lower, dtype=float)
    yx_upper = np.array(dydx_upper, dtype=float)
    yx_lower = np.array(dydx_lower, dtype=float)
    x_upper = x_upper[:-1]
    x_upper= np.array(x_upper)
    x_lower = x_lower[:-1]
    x_lower = np.array(x_lower)
    Ct = trapezoid(p_upper * yx_upper, x_upper) +  trapezoid(p_lower * yx_lower, x_lower)
    return(Ct)

alphas = []  # List to store angle of attack values
Cm_values = []  # List to store moment coefficient values
Cl_values = []  # List to store lift coefficient values
Cd_values = []  # List to store drag coefficient values
CoP_values = []
dydx_upper = [2.165665525, 0.849096771, 0.548353145, 0.35236511, 0.239465629, 
    0.169963946, 0.121411036, 0.083886391, 0.053005107, 0.026565375, 
    0.002272881, -0.020972626, -0.043606397, -0.065714021, -0.086413264, 
    -0.103453708, -0.116547646, -0.128316243, -0.13902106, -0.147261752, 
    -0.152980211, -0.155104102, -0.151815517, -0.138933748]  
dydx_lower = [-1.32588178, -0.500836345, -0.27688194, -0.155201058, -0.093414928, 
    -0.060490291, -0.039384731, -0.024605121, -0.01298194, -0.003192475, 
    0.00545223, 0.013503413, 0.021308214, 0.029223946, 0.036812585, 
    0.044788818, 0.052690642, 0.060176781, 0.066879119, 0.071721256, 
    0.074426033, 0.075904576, 0.070171935]

for RunNumber in range(6,60):
    # Init CpCalculator
    Cp_upper, x_upper, Cp_lower, x_lower, runXdata = CC.CpCalc(RunNumber)

    # Calculate Values
    Cn = calculate_cn(Cp_upper, x_upper, Cp_lower, x_lower)
    Cm = calculate_cm(Cp_upper, x_upper, Cp_lower, x_lower)
    CmQuarterChord = Cm + 0.25 *Cn 
    CoP = Cm/ -Cn
    Ct = calculate_cd(Cp_upper, dydx_upper, Cp_lower, dydx_lower, x_upper, x_lower)
    alpha = float(runXdata[2]) 
    Cd = Ct * np.cos(alpha*np.pi/180  ) + Cn * np.sin(alpha*np.pi/180  )
    Cl = Cn *(np.cos(alpha*np.pi/180  )+(np.sin(alpha*np.pi/180  )**2)/(np.cos(alpha*np.pi/180  )))-Cd *np.tan(alpha*np.pi/180  )

    alphas.append(alpha)  # Convert alpha to degrees for better visualization
    Cm_values.append(Cm)
    Cl_values.append(Cl)
    Cd_values.append(Cd)
    CoP_values.append(CoP)

    # print(f"Calculated Cn: {Cn:.4f} \nCalculated Cm: {Cm:.4f}\nCalculated Cm0: {CmQuarterChord:.4f}\nCalculated CoP: {CoP:.4f}\nCalculated Cd: {Cd:.4f}\nCalculated Cl: {Cl:.4f}\nAngle of Attack: {alpha:.4f}")

# plt.figure(figsize=(10, 6))
# plt.plot(alphas, Cm_values, label='$C_m$', color='b', marker='o')
# plt.xlabel('Angle of Attack (degrees)')
# plt.ylabel('$C_m$')
# # plt.title('Moment Coefficient ($C_m$) vs Angle of Attack ($\\alpha$)')
# plt.grid(True)
# plt.legend()
# plt.show()

# # Plotting Cl vs Alpha
# plt.figure(figsize=(10, 6))
# plt.plot(alphas, Cl_values, label='$C_l$', color='g', marker='s')
# plt.xlabel('Angle of Attack (degrees)')
# plt.ylabel('$C_l$')
# # plt.title('Lift Coefficient ($C_l$) vs Angle of Attack ($\\alpha$)')
# plt.grid(True)
# plt.legend()
# plt.show()

# # Plotting Cd vs Alpha
# plt.figure(figsize=(10, 6))
# plt.plot(alphas, Cd_values, label='$C_d$', color='r', marker='^')
# plt.xlabel('Angle of Attack (degrees)')
# plt.ylabel('$C_d$')
# # plt.title('Drag Coefficient ($C_d$) vs Angle of Attack ($\\alpha$)')
# plt.grid(True)
# plt.legend()
# plt.show()



# Plotting CoP vs Alpha
plt.figure(figsize=(10, 6))
plt.plot(alphas, CoP_values, label='CoP', color='m', marker='x')
plt.xlabel('Angle of Attack (degrees)')
plt.ylabel('Center of Pressure (CoP)')
# plt.title('Center of Pressure (CoP) vs Angle of Attack ($\\alpha$)')
plt.grid(True)
plt.legend()
plt.show()