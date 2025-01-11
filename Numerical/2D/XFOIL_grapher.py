import matplotlib.pyplot as plt
import matplotlib.ticker as ticker


def parse_xfoil_polar(filepath):
    """
    Parses an XFOIL polar output file and returns lists (or arrays) of:
    alpha, CL, CD, CDp, CM, Top_Xtr, Bot_Xtr
    """

    alpha_list = []
    cl_list = []
    cd_list = []
    cdp_list = []
    cm_list = []
    top_xtr_list = []
    bot_xtr_list = []

    with open(filepath, 'r') as f:
        lines = f.readlines()

    # Find the line index where the data columns start.
    # Usually, the columns start after the line containing the headers:
    # "  alpha     CL        CD       CDp       CM    Top_Xtr Bot_Xtr"
    header_found = False
    start_index = None

    for i, line in enumerate(lines):
        if line.strip().startswith('alpha') and 'CL' in line and 'CD' in line:
            header_found = True
            start_index = i + 2
            break

    if not header_found:
        raise ValueError("Could not find the header line with column titles.")

    # Now parse each data line after the header
    for line in lines[start_index:]:
        line = line.strip()
        if not line:
            # Skip any blank lines
            continue

        # XFOIL polar lines typically look like:
        # alpha   CL      CD      CDp     CM      Top_Xtr  Bot_Xtr
        # e.g. "  -5.000  -0.3605  0.01064 0.00502 -0.0342   0.8465  0.0082"
        # We can split on whitespace
        parts = line.split()

        # Sometimes XFOIL outputs trailing lines or messages. We can do a sanity check:
        if len(parts) < 7:
            # Not a valid data line—maybe an extra info line at the bottom
            break

        # Convert columns to floats
        alpha_val = float(parts[0])
        cl_val = float(parts[1])
        cd_val = float(parts[2])
        cdp_val = float(parts[3])
        cm_val = float(parts[4])
        top_xtr_val = float(parts[5])
        bot_xtr_val = float(parts[6])

        alpha_list.append(alpha_val)
        cl_list.append(cl_val)
        cd_list.append(cd_val)
        cdp_list.append(cdp_val)
        cm_list.append(cm_val)
        top_xtr_list.append(top_xtr_val)
        bot_xtr_list.append(bot_xtr_val)

    return (alpha_list, cl_list, cd_list, cdp_list, cm_list, top_xtr_list, bot_xtr_list)


def plot_cl_curve(alpha, cl):
    plt.figure(figsize=(8, 5))

    # Plot the curve
    plt.plot(alpha, cl, '-', color='blue', label=r'$C_L$', linewidth=1.5)

    # Formatting the graph
    plt.xlabel("Angle of Attack (deg)", fontsize=12)
    plt.ylabel(r"$C_L$", fontsize=12)

    # Customize grid lines
    ax = plt.gca()
    ax.xaxis.set_major_locator(ticker.MultipleLocator(2))
    ax.xaxis.set_minor_locator(ticker.MultipleLocator(0.5))
    ax.yaxis.set_major_locator(ticker.MultipleLocator(0.2))
    ax.yaxis.set_minor_locator(ticker.MultipleLocator(0.05))

    plt.grid(visible=True, which='major', color='black', linestyle='-', alpha=0.5)
    plt.grid(visible=True, which='minor', color='gray', linestyle='--', alpha=0.3)

    # Customize origin lines
    ax.spines['bottom'].set_color('black')  # x-axis
    ax.spines['left'].set_color('black')  # y-axis
    ax.spines['bottom'].set_linewidth(1.5)
    ax.spines['left'].set_linewidth(1.5)

    # Hide unnecessary spines
    ax.spines['top'].set_color('none')
    ax.spines['right'].set_color('none')

    # Add a legend
    plt.legend(fontsize=12, loc='upper left', frameon=True)

    plt.tight_layout()
    plt.show()



def plot_cd_curve(alpha, cd):
    plt.figure(figsize=(8, 5))

    # Plot the curve
    plt.plot(alpha, cd, '-', color='green', label=r'$C_D$', linewidth=1.5)

    # Formatting the graph
    plt.xlabel("Angle of Attack (deg)", fontsize=12)
    plt.ylabel(r"$C_D$", fontsize=12)

    # Customize grid lines
    ax = plt.gca()
    ax.xaxis.set_major_locator(ticker.MultipleLocator(2))
    ax.xaxis.set_minor_locator(ticker.MultipleLocator(0.5))
    ax.yaxis.set_major_locator(ticker.MultipleLocator(0.02))
    ax.yaxis.set_minor_locator(ticker.MultipleLocator(0.005))

    plt.grid(visible=True, which='major', color='black', linestyle='-', alpha=0.5)
    plt.grid(visible=True, which='minor', color='gray', linestyle='--', alpha=0.3)

    # Customize origin lines
    ax.spines['bottom'].set_color('black')  # x-axis
    ax.spines['left'].set_color('black')  # y-axis
    ax.spines['bottom'].set_linewidth(1.5)
    ax.spines['left'].set_linewidth(1.5)

    # Hide unnecessary spines
    ax.spines['top'].set_color('none')
    ax.spines['right'].set_color('none')

    # Add a legend
    plt.legend(fontsize=12, loc='upper left', frameon=True)

    plt.tight_layout()
    plt.show()



def main():
    # Path to your XFOIL polar output file.
    # Replace 'polar_output.txt' with the actual filename.
    filepath = 'XFLR5textfiles/Viscous21ms/XFOIL_RE_4x10^5_2.txt'

    alpha, cl, cd, cdp, cm, top_xtr, bot_xtr = parse_xfoil_polar(filepath)
    plot_cl_curve(alpha, cl)
    plot_cd_curve(alpha, cd)


if __name__ == "__main__":
    main()

