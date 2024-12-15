# 3.2.1 Flow near the aerofoil surface
# Compute pressure coefficient, show a few example curves, and discuss the trend with α (3 marks)
# Relate the Cp curves to separation (tufts) locations (2 marks)

import pandas as pd
import matplotlib.pyplot as plt

# Load the data from the file
raw_data = 'Experimental\\2D\\raw_2D.txt'

_2Ddata = pd.read_csv(raw_data, sep='\t', skiprows=1)  # Skip first row if it's units

# Extract column headers
_2Ddata.columns = _2Ddata.columns.str.strip()

# Create a dictionary of lists for each column
columns = {col: _2Ddata[col].dropna().tolist() for col in _2Ddata.columns}

# Print out the dictionary of columns
for column, values in columns.items():
    print(f"Column '{column}': {values[:5]}...")  # Printing first 5 values as a preview
# Function to plot a specific run
# Specify the run number to plot
run_number = 3  # Change this number to the desired run

# Assume 'X/C' is column 1, and each run's data is spread across columns after
xc_column = _2Ddata.iloc[:, 0]  # First column is X/C
y_column = _2Ddata.iloc[:, run_number - 1]  # Adjust for 0-indexing


plt.figure(figsize=(10, 6))
plt.plot(xc_column, y_column, marker='o', linestyle='-', color='b')
plt.xlabel('X/C (Percentage)')
plt.ylabel(f'Run {run_number} Data')
plt.title(f'Run {run_number}: X/C vs Pressure')
plt.grid(True)
plt.show()
