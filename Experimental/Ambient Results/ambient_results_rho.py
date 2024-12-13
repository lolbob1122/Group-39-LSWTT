import math
import csv

file_name = 'Experimental\Ambient Results\converted_2D.csv'

def get_ambient_results(file_name): # makes a function so luca can call it
    P_sum = 0
    T_sum = 0
    Delta_P_sum = 0

    mu_zero = 1.716 * 10**(-5) # kg/m*s
    T_zero = 273.15 # K
    S = 110.4 # K
    R = 287 # J/kg*K
    c = 0.16 # m 

    # Reads csv file to find all values for p and T
    with open ( file_name , 'r') as raw_2D_data: 
        reader = csv.reader(raw_2D_data)
        P_bar = []
        T = []
        Delta_P = []
        for row in reader:
            P_bar.append(float(row[4]))
            T.append(float(row[5]))
            Delta_P.append(float(row[3]))

    # Sums all values for the average
    for i in range(len(P_bar)):
        P_sum = P_sum + P_bar[i]
        T_sum = T_sum + T[i]
        Delta_P_sum = Delta_P_sum + Delta_P[i]

    P_avg = P_sum/len(P_bar) * 100 #converts from hectopascals
    T_avg = T_sum/len(T) + 273.15 #conversion to kelvin
    Delta_P_avg = Delta_P_sum/len(Delta_P)

    mu = mu_zero * (( T_avg / T_zero ) ** ( 3 / 2 )) * (( T_zero + S )/( T_avg + S ))
    q_inf = 0.211804 + 1.928442 * Delta_P_avg + (1.879374 * 10 ** (-4)) * Delta_P_avg ** 2
    rho = P_avg / (R * T_avg)
    P_s = P_avg - q_inf
    U_inf = math.sqrt((2 * q_inf)/rho)
    Re = (rho * U_inf * c) / mu

    print(rho)
    print(q_inf)
    print(mu)
    print(P_s)
    print(U_inf)
    print(Re)

    return (mu,q_inf,rho,P_s,P_avg,T_avg,Delta_P_avg,U_inf,Re)

get_ambient_results(file_name)

