import matplotlib.pyplot as plt


run_number = 1

p_inf = 1
q_inf = 1
raw_data = 'Experimental\\2D\\Adjusted_data.csv'
p0 = []
with open(raw_data, "r") as file:
    lines = file.readlines()
    for line in lines:
        # Strip leading/trailing whitespace and split by commas (assuming CSV format)
        line = line.strip().split(",")  # Adjust the split delimiter as needed
        p0.append(line)  # Add the row (list) to the main list

print(p0)