import numpy as np
from scipy.integrate import trapezoid  # Import trapezoid instead of using np.trapz
import Cp_Calculator as CC  # Importing your existing function


# Example usage with RunNumber
RunNumber = 27  # Change this to the actual run number you want to analyze


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


def calculate_cd(rho, U_inf, p_inf, chord):
    D = 0

    u1 =  
    y1 = 
    p1 = 



    Cd = D/( rho * U_inf ** 2 * chord )

    return(Cd)
# Init CpCalculator
Cp_upper, x_upper, Cp_lower, x_lower, runXdata = CC.CpCalc(RunNumber)


Cn = calculate_cn(Cp_upper, x_upper, Cp_lower, x_lower)
Cm = calculate_cm(Cp_upper, x_upper, Cp_lower, x_lower)
Cm0 = Cm + 0.25 *Cn 
CoP = Cm/ -Cn
Cd = 1 #TODO still
alpha = float(runXdata[2])
Cl = Cn *(np.cos(alpha)+(np.sin(alpha)**2)/(np.cos(alpha)))-Cd *np.tan(alpha)

print(f"Calculated Cn: {Cn:.4f} \nCalculated Cm: {Cm:.4f}\nCalculated Cm0: {Cm0:.4f}\nCalculated CoP: {CoP:.4f}\nCalculated Cd: {Cd:.4f}\nCalculated Cl: {Cl:.4f}\nAngle of Attack: {alpha:.4f}")

# print(CC.CpCalc(RunNumber))