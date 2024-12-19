import scipy as sc
import numpy as np
import pandas as pd
import itertools as it
import matplotlib.pyplot as plt
import math
import sys
sys.path.insert(1, 'Experimental')






import Ambient_Results.ambient_results_rho as ar

#change depending on which row
row_number = 12

density=ar.get_ambient_results_new(row_number)[0]
print(density)


# Read the data from the file, skipping the first row
data = pd.read_csv("Experimental/2D/raw_2D.txt", sep='\\s+', skiprows=1)

# Display the first few rows to verify
print(data.head(3))



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
for i in range(47):
    speed= math.sqrt(p_dynamic[i]/density)







# #plot the thingies
plt.plot(x_dist_tot, p_tot)
plt.plot(x_dist_stat,p_stat)
plt.plot(x_dist_tot,p_dynamic)

# Add a title, axis labels, and a legend
plt.title('One period of the sine and cosine functions')
plt.xlabel('x [rad]')
plt.ylabel('y')
plt.legend(('sin(x)', 'cos(x)',"cool line"))

# Don't forget to call show()!
plt.show()

print(len(x_dist_tot))