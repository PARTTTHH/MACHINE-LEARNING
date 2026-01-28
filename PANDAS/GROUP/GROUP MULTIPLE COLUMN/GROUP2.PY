""""
GROUPING BY MULTIPLE COLUMNS:
SYNTAX:-
    df.gruopby([column1, column2,...])["TARGETED_CLLUMN_HERE].aggregation_method
"""

import pandas as pd

data = {
    "NAME": ['A', 'A', 'B', 'B', 'C'],
    "AGE":  [20, 20, 21, 21, 20],
    "SALARY": [25000, 30000, 20000, 22000, 35000]
}

df = pd.DataFrame(data)
print("ORIGINAL DATAFRAME:-")
print(df)

print()

grouped = df.groupby(["NAME", "AGE"])["SALARY"].sum()
print(grouped)
