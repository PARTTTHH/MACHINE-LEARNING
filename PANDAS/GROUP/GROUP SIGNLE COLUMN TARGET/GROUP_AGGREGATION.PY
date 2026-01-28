
import pandas as pd

# AGGREGATION WITH groupby()
data = {
    "DEPARTMENT":["IT", "DEV", "IT", "HR", "DEV", "HR", "IT"],
    "SALARY":[50000, 70000, 60000, 45000, 85000, 40000, 70000]
}

df = pd.DataFrame(data)

grouped = df.groupby("DEPARTMENT")["SALARY"].sum()
print(grouped)


"""
groupby() METHOD GROUPS DATA BASED ON THE GIVEN COLUMN,
AND THEN WE CAN APPLY AGGREGATION FUNCTION LIKE sum(), mean(), max(), etc. 

THINK OF groupby() AS TEO STEP PROCESS:-
1. SPLIT:-
    IT  → 50000, 60000, 70000
    DEV → 70000, 85000
    HR  → 45000, 40000

2. APPLY:-
    sum(), mean(), max(), min(), count()

3. COMBINE:-
    RETURN AS SERIES OR DATAFRAME
    
"""