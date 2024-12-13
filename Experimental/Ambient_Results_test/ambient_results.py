import math
import csv
P_sum = 0

def P_infcalc():
    with open ('Experimental\Ambient Results\converted_2D.csv' , 'r') as raw_2D_data:
        reader = csv.reader(raw_2D_data)
        P_bar = []
        for row in reader:
            P_bar.append(float(row[4]))

    P_bar = P_bar[2:]

    for i in range(len(P_bar)):
        P_sum = P_sum + P_bar[i]

    P_avg = P_sum/len(P_bar)
    print(P_avg)
    return P_avg


