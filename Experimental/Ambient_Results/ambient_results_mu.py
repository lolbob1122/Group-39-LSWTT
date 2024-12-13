from ambient_results_rho import rho,T_avg
import math

mu_zero = 1.716 * 10**(-5) # kg/m*s
T_zero = 273.15 # K
S = 110.4 # K

mu = mu_zero * (( T_avg / T_zero ) ** ( 3 / 2 )) * (( T_zero + S )/( T_avg + S ))
print( mu )