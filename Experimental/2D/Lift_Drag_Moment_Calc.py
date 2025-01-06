import numpy as np
from scipy.integrate import trapezoid  # Import trapezoid instead of using np.trapz
import Cp_Calculator as CC  # Importing your existing function


# Example usage with RunNumber
RunNumber = 5  # Change this to the actual run number you want to analyze


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


# Fetch Cp and x/c data using your CpCalc function
Cp_upper, x_upper, Cp_lower, x_lower = CC.CpCalc(RunNumber)

# Calculate Cn
Cn = calculate_cn(Cp_upper, x_upper, Cp_lower, x_lower)
print(f"Calculated Cn for Run {RunNumber}: {Cn:.4f}")
