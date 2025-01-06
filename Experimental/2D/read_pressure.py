import scipy as sc
import numpy as np
import pandas as pd
import itertools as it
import matplotlib.pyplot as plt
import csv
import math
import sys
from scipy.integrate import quad
sys.path.insert(1, 'Experimental')
#new line for change


def get_ambient_results_new(run_number): # makes a function so luca can call it

    
#### Variable Definitions ####

    ''' Constants needed for the calculations '''
    mu_zero = 1.716 * 10**(-5) # kg/m*s
    T_zero = 273.15 # K
    S = 110.4 # K
    R = 287 # J/kg*K
    c = 0.16 # m 

##############################

    # Reads csv file to find all values for p, delta p and T
    with open ( "Experimental\Ambient_Results\converted_2D.csv" , 'r') as raw_2D_data: 
        reader = csv.reader(raw_2D_data)
        P_bar = []
        T = []
        Delta_P = []
        for row in reader:
            P_bar.append(100*float(row[4]))  #converted to pascals
            T.append(273.15+float(row[5]))  #converted to K
            Delta_P.append(float(row[3]))

########################

#### Formulas for the Calculation of the Needed Values ####
    run_numer_index = int(run_number-6)
    mu = mu_zero * (( T[run_numer_index] / T_zero ) ** ( 3 / 2 )) * (( T_zero + S )/( T[run_numer_index] + S )) 
    q_inf = 0.211804 + 1.928442 * Delta_P[run_numer_index] + (1.879374 * 10 ** (-4)) * Delta_P[run_numer_index] ** 2
    rho = P_bar[run_numer_index] / (R * T[run_numer_index])
    P_s = P_bar[run_numer_index] - q_inf
    U_inf = math.sqrt((2 * q_inf)/rho)
    Re = (rho * U_inf * c) / mu

    return (mu,q_inf,rho,P_s,U_inf,Re)





#change depending on which row
drag_coef=[]

Angle=[]
for p in range(67):
    row_number = p
    row_number_adjusted = row_number + 6

    density=get_ambient_results_new(row_number_adjusted)[2]
    U_inf=get_ambient_results_new(row_number_adjusted)[4]
    q_inf=get_ambient_results_new(row_number_adjusted)[1]



    # Read the data from the file, skipping the first row
    data = pd.read_csv("Experimental/2D/raw_2D.txt", sep='\\s+', skiprows=1)

    # Display the first few rows to verify
    print(data.head(3))

    AoA= data.iloc[row_number,2]
    Angle.append(AoA)
    print(AoA)
    



    #total pressure wake
    x_dist_tot = [
        0, 12, 21, 27, 33, 39, 45, 51, 57, 63, 69, 72, 75, 78, 81, 84, 
        87, 90, 93, 96, 99, 102, 105, 108, 111, 114, 117, 120, 123, 126, 
        129, 132, 135, 138, 141, 144, 147, 150, 156, 162, 168, 174, 180, 
        186, 195, 207, 219
    ]
    #static pressure rake
    x_dist_stat = [
        43.5, 55.5, 67.5, 79.5, 91.5, 103.5, 115.5, 127.5, 139.5, 
        151.5, 163.5, 175.5
    ]

    #making the holes in m
    y_dist_tot=[]
    for i in range(47):
        y= x_dist_tot[i]/1000
        y_dist_tot.append(y)
    #print(y_dist_tot)

    y_dist_stat=[]
    for i in range(12):
        y= x_dist_stat[i]/1000
        y_dist_stat.append(y)
    #print(y_dist_stat)

    # p_tots = []
    # for i in range(57,104,1):
    #     for j in range(68): 
    #         column = data.iloc[j,i]  # Access the first column (0-indexed)
    #         p_tot57.append(column)
    #         print(column)
    #     break
    # print(p_tot57)

    #making the total pressure from rake
    p_tot=[]
    for i in range(57,104,1):
        press= data.iloc[row_number,i]
        p_tot.append(press)

    #the static pressure at the rake
    p_stat=[]
    for i in range(105,117,1):
        stat=data.iloc[row_number,i]
        p_stat.append(stat)


    p_dynamic=[]

    for i in range(47):
        if i <=7:
            dynamic= p_tot[i]-p_stat[0]
            p_dynamic.append(dynamic)
        elif i in range(8,10,1):
            dynamic= p_tot[i]-p_stat[1]
            p_dynamic.append(dynamic)
        elif i in range(10,13,1):
            dynamic= p_tot[i]-p_stat[2]
            p_dynamic.append(dynamic)
        elif i in range(13,17,1):
            dynamic= p_tot[i]-p_stat[3]
            p_dynamic.append(dynamic)
        elif i in range(17,21,1):
            dynamic= p_tot[i]-p_stat[4]
            p_dynamic.append(dynamic)
        elif i in range(21,25,1):
            dynamic= p_tot[i]-p_stat[5]
            p_dynamic.append(dynamic)
        elif i in range(25,29,1):
            dynamic= p_tot[i]-p_stat[6]
            p_dynamic.append(dynamic)
        elif i in range(29,33,1):
            dynamic= p_tot[i]-p_stat[7]
            p_dynamic.append(dynamic)
        elif i in range(33,37,1):
            dynamic= p_tot[i]-p_stat[8]
            p_dynamic.append(dynamic)
        elif i in range(37,40,1):
            dynamic= p_tot[i]-p_stat[9]
            p_dynamic.append(dynamic)
        elif i in range(40,42,1):
            dynamic= p_tot[i]-p_stat[10]
            p_dynamic.append(dynamic)
        else:
            dynamic= p_tot[i]-p_stat[11]
            p_dynamic.append(dynamic)

    velocity=[]
    free_stream=[]
    rho=[]
    for i in range(47):
        speed= math.sqrt(2*p_dynamic[i]/density)
        velocity.append(speed)
        free_stream.append(U_inf)
        rho.append(density)


    #now do it for the small rake
    velocity_rake=[]
    free_stream_rake=[]
    p_dyn_small=[p_tot[6]-p_stat[0],p_tot[8]-p_stat[1],p_tot[10]-p_stat[2],p_tot[14]-p_stat[3],p_tot[17]-p_stat[4],p_tot[17]-p_stat[5],p_tot[21]-p_stat[6],p_tot[29]-p_stat[7],p_tot[33]-p_stat[8],p_tot[37]-p_stat[9],p_tot[39]-p_stat[10],p_tot[41]-p_stat[11]]

    print(p_dyn_small)

    for i in range(12):
        speed_rake=math.sqrt(2*p_dyn_small[i]/density)
        velocity_rake.append(speed_rake)
        free_stream_rake.append(U_inf)

    #This is where the drag part starts
    Integrand_1=[]
    Integrand_2=[]
    Integrand_3=[]



    #Bad Calculation, more accurate version done in the next parts
    # for j in range(47):
    #     value_1= (free_stream[j] - velocity[j]) * velocity[j]
    #     #print(Integrand_1)
        
    #     Integrand_1.append(value_1)
        

    for i in range(12):
        value_2=(p_stat[i])
        Integrand_2.append(value_2)
        value_3=(free_stream_rake[i] - velocity_rake[i]) * velocity_rake[i]
        Integrand_3.append(value_3)
    print(Integrand_3)
    # D=density*np.trapz(Integrand_1,y_dist_tot) + np.trapz(Integrand_2,y_dist_stat)
    # C_d= (D/q_inf)
    # print(D)
    # print(C_d)
    


    D_2=density*np.trapz(Integrand_3,y_dist_stat) + np.trapz(Integrand_2,y_dist_stat)
    C_d2= (D_2/q_inf)



    print(D_2)
    print(C_d2)
    print(q_inf)
    drag_coef.append(C_d2)













# # #plot the thingies
# # plt.plot(x_dist_tot, p_tot)
# # plt.plot(x_dist_stat,p_stat)
# # plt.plot(x_dist_tot,p_dynamic)
# plt.plot(x_dist_tot,velocity)
# plt.plot(x_dist_tot,free_stream, "--")

# # Add a title, axis labels, and a legend
# plt.title("The wake velocity field at {} AoA ".format(AoA))
# plt.xlabel('Position [mm]')
# plt.ylabel('Velocity [ms^-1]')
# plt.legend(("Computed Velocity from wake", "Computed Free Stream velocity"))

# plt.xticks(np.arange(0, 250, step=50))
# plt.yticks(np.arange(15, 26, step=1))

# plt.ylim(15, 24)
# plt.grid()
# # Don't forget to call show()!
# #plt.show()

plt.plot(Angle,drag_coef)
plt.ylim(0,0.01)

plt.show()