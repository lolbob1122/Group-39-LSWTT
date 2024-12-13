import scipy as sc
import numpy as np
import pandas as pd
import itertools as it
import matplotlib.pyplot as plt

#change depending on which row
row_number = 12


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


# #plot the thingies
plt.plot(x_dist_tot, p_tot)
plt.plot(x_dist_stat,p_stat)

# Add a title, axis labels, and a legend
plt.title('One period of the sine and cosine functions')
plt.xlabel('x [rad]')
plt.ylabel('y')
plt.legend(('sin(x)', 'cos(x)'))

# Don't forget to call show()!
plt.show()