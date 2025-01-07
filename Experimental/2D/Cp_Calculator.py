import sys
sys.path.insert(1, 'Experimental')

import Ambient_Results.ambient_results_rho as ar

def CpCalc(runNumber):
    Data2D = []

    # Read the text file and extract data from the "Freestream speed" section
    with open("Experimental/2D/raw_2DNew.txt", "r") as file:
        lines = file.readlines()

    # Find the start of the "Freestream speed" data
    start_idx = None
    for i, line in enumerate(lines):
        if "Run_nr" in line.strip():  # Search for the "Freestream speed" line
            start_idx = (
                i + 2
            )  # Skip the header and start with the data (2 lines after "Freestream speed")
            break

    # Check if we found the "Freestream speed" section
    if start_idx is None:
        print("Error: 'Run_nr' section not found!")
    else:
        # print(f"Data starts from line {start_idx}")
        pass

    # Extract the rows under the "Freestream speed" section
    data_lines = lines[start_idx:]


    # Process each line to extract the values
    for line in data_lines:
        # Strip leading/trailing spaces and split by any whitespace (tabs, spaces, etc.)
        columns = line.strip().split() #columns = one row of data starting from row 3
        Data2D.append(columns)
        
    runXdata = Data2D[runNumber-6] #select only one run
    # print(runXdata)
    pValues = runXdata[8:57]
    name = "Experimental\\Ambient_Results\\converted_2D.csv"
    q_inf = ar.get_ambient_results_new(name, runNumber)[1]
    # print(q_inf)
    Cp = []
    for i in range(len(pValues)):
        Cp.append((float(pValues[i]) - (float(runXdata[104])-q_inf))/ q_inf )

    # print(Cp)
    PosList = []
    with open("Experimental\\2D\\Airfoil_Tap_Positions.txt", "r") as file:
        for line in file.readlines():
            columns = line.strip().split()
            PosList.append(columns)

    # print(PosList)
    # Extract the second column from PosList and convert it to floats
    x_values = [float(row[1]) for row in PosList]  # Only take the first 49 entries
    x_values_first = x_values[:25]
    Cp_first = Cp[:25]

    x_values_second = x_values[25:]
    Cp_second = Cp[25:]

    x_values_first_percent = [x / 100 for x in x_values_first]  # Normalize to 0-1
    x_values_second_percent = [x / 100 for x in x_values_second] 
    return(Cp_first, x_values_first_percent, Cp_second, x_values_second_percent, runXdata)


