import numpy as np
import scipy as sp


S = 0.16*0.4169

CL_min = 0.00
CL_max = 0.00

Cm_min = 0.00
Cm_max = 0.00

CD_min = 0.000
CD_max = 0.000
CLd_test = 0.5  # Change val
Cmd_test = 0.5  # Change val
Cdd_test = 0.5  # Change val

# Read the text file and extract data from the "Main Wing" section
with open("Experimental/3D/raw_3D.txt", "r") as file:
    lines = file.readlines()

# Print the first few lines to confirm file is being read correctly
# print("First few lines of the file:")
# print("".join(lines[:10]))  # Print the first 10 lines for verification
# Find the start of the "Main Wing" data

start_idx = None
for i, line in enumerate(lines):
    if "Main Wing" in line.strip():  # Search for the "Main Wing" line
        start_idx = (
            i + 2
        )  # Skip the header and start with the data (2 lines after "Main Wing")
        break

# Check if we found the "Main Wing" section
if start_idx is None:
    print("Error: 'Main Wing' section not found!")
else:
    # print(f"Data starts from line {start_idx}")
    pass
