import math
from ambient_results_rho import Delta_P_avg

q_inf = 0.211804 + 1.928442 * Delta_P_avg + (1.879374 * 10 ** (-4)) * Delta_P_avg ** 2

print(q_inf)