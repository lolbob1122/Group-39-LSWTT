# 3.2.1 Flow near the aerofoil surface
# Compute pressure coefficient, show a few example curves, and discuss the trend with α (3 marks)
# Relate the Cp curves to separation (tufts) locations (2 marks)

import pandas as pd

# Load the data from the file
file_path = '/mnt/data/raw_2D.txt'

data = pd.read_csv(file_path, sep='\t', skiprows=1)  # Skip first row if it's units

# Extract column headers
data.columns = data.columns.str.strip()

# Create a dictionary of lists for each column
columns = {col: data[col].dropna().tolist() for col in data.columns}

# Print out the dictionary of columns
for column, values in columns.items():
    print(f"Column '{column}': {values[:5]}...")  # Printing first 5 values as a preview

