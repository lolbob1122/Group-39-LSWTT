import numpy as np
from scipy.integrate import trapezoid  # Import trapezoid instead of using np.trapz
import Cp_Calculator as CC  # Importing your existing function


# Example usage with RunNumber
RunNumber = 10  # Change this to the actual run number you want to analyze


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

    # Check if the x values are of unequal length, adjust the size by interpolation
    if len(Cp_upper) != len(Cp_lower):
        # You can interpolate the lower Cp values to match the upper Cp values
        x_common = np.linspace(x_lower[0], x_lower[-1], len(Cp_upper))
        Cp_lower = np.interp(x_common, x_lower, Cp_lower)
        x_lower = x_common

    # Use scipy.integrate.trapezoid for numerical integration with non-uniform spacing
    integral_upper = trapezoid(Cp_upper, x_upper)  # Integral of Cp over x/c (upper)
    integral_lower = trapezoid(Cp_lower, x_lower)  # Integral of Cp over x/c (lower)

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

