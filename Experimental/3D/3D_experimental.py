import pandas as pd

# Define the file path
file_path = "Experimental/3D/raw_3D.txt"

# Read the file into a DataFrame, inferring column names from the first row of data
data = pd.read_csv(file_path, delim_whitespace=True, header=1)

# Extract column names dynamically
column_names = data.columns

# Create individual lists for each parameter based on the dynamic column names
parameter_lists = {name: data[name].tolist() for name in column_names}

# Print each parameter list with its name (example)
for parameter, values in parameter_lists.items():
    print(f"{parameter}: {values[:5]} ...")  # Print the first 5 values as a preview
