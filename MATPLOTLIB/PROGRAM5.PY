# MATPLOTLIB PLOTTING FUNCTIONS:-
# plt.plot(x,y, color="color name", linestyle="line_style", linewidth=value, marker="marker symbol", label=label name)

import matplotlib.pyplot as plt

months = [1,2,3,4]
sales = [1000, 1500, 1200, 1800]

plt.plot(months, sales, color='orange', linestyle='--', linewidth=2, marker='o', label="2026 YEARS SALES")
plt.xlabel("MONTHS")
plt.ylabel("SALES PER MONTH")
plt.title("MONTHLY SALES REPORT")
plt.legend(loc='lower right', fontsize=10)    # 'best', 'upper right', 'upper left', 'lower left', 'lower right', 'right', 'center left', 'center right', 'lower center', 'upper center', 'center'
plt.grid(color='gray', linestyle='-', linewidth=1)
plt.xlim(1,4)
# plt.ylim(0,2000)
plt.xticks([1,2,3,4], ['M1','M2','M3','M4'])
plt.show()