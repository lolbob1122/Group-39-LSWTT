import math
import csv

P_sum = 0
T_sum = 0
Delta_P_sum = 0

R = 287 # J/kg*K

# Reads csv file to find all values for p and T
with open ('Experimental\Ambient Results\converted_2D.csv' , 'r') as raw_2D_data: 
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

rho = P_avg / (R * T_avg)

print(rho)



