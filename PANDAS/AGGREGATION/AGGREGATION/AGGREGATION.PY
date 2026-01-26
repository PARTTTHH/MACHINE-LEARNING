"""
AGGREGATON:- 
        AGGREGATION MEANS REDUCING MULTIPLE VALUES INTO ONE SUMMARY VALUES 

COMMON AGGREGATION FUNCTIONS:--
        FUNCTION	    MEANING
        sum()	  --->  TOTAL
        mean()	  --->  AVERAGE
        max()	  --->  HIGHST VALUE
        min()	  --->  LOWEST VALUE
        count()	  --->  NUMBER OF NON-NULL VALUES
        median()  --->  MIDDLE VALUE
        std()	  --->  STANDARD DEVIATION
        var()	  --->  VARIANCE

"""

import pandas as pd

# AGGREGATION ON SERIES
s = pd.Series([10,20,30,40,50])
print("SERIES:-")
print(s)

print("SUM:", s.sum())
print("MEAN:", s.mean())
print("MAX:", s.max())
print("MIN:", s.min())

print()

# AGGREGATION ON DATAFRAME
data = {
    "MARKS":[45,78,88,56,90],
    "AGE":[20,21,20,22,21]
}
df = pd.DataFrame(data)
print("ORIGINAL DATAFRAME:-")
print(df)

df_mean = df.mean()
df_sum = df.sum()
df_min = df.min()
df_max = df.max()

print()
# DEFAULT BEHAVIOUR axis = 0 (column-wise)
print(f"MEAN----------- \n{df_mean}")
print(f"SUM---------- \n{df_sum}")
print(f"MIN---------- \n{df_min}")
print(f"MAX---------- \n{df_max}")

print()

# PANDAS PROVIDES agg() FOR USING MULTIPLE AGGREGATION AT ONCE
print(
    df.agg({        
        "MARKS": ["min", "max", "sum"],
        "AGE": ["min", "max", "mean"]
    })
)
print()

# AGGREGATION WITH groupby()
data2 = {
    "DEPARTMENT":["IT", "IT", "HR", "HR", "IT"],
    "SALARY":[50000, 60000, 45000, 40000, 70000]
}

df2 = pd.DataFrame(data2)

print(
    df2.groupby("DEPARTMENT")["SALARY"].mean()
)