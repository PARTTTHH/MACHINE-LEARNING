"""
SYNTAX:-
        df.merge(df1, df2, on="BASIS_COLUMN", how=TYPE OF JOIN)

TYPE OF JOINS:-
inner  --> RETURNS ONLY MATCHING ROWS FROM BOTH DATAFRAMES
left   --> RETURNS ALL ROWS FROM LEFT DATAFRAME + MATCHING FROM RIGHT
right  --> RETURNS ALL ROWS FROM RIGHT DATAFRAME + MATCHING FROM LEFT
outer  --> RETURNS ALL ROWS FROM BOTH DATAFRAMES (MATCH + NO MATCH)
cross  --> RETURNS CARTESIAN PRODUCT (EVERY ROW COMBINES WITH EVERY ROW)

"""

import pandas as pd

df_Customers = pd.DataFrame({
    "CustomerID":[1,2,3],
    "CustomerName":["SURESH", "RAMESH", "KALPESH"]
})

df_Orders = pd.DataFrame({
    "CustomerID":[1,2,4],
    "OrderAmount":[250, 450, 350]
})

#MARGE
df_Marge1 = pd.merge(df_Customers, df_Orders, on="CustomerID", how="inner")
print("\nMERGE USING inner:-")
print(df_Marge1)

# OUTER
df_Marge2 = pd.merge(df_Customers, df_Orders, on="CustomerID", how="outer")
print("\nMERGE USING outer:-")
print(df_Marge2)

# LEFT
df_Marge3 = pd.merge(df_Customers, df_Orders, on="CustomerID", how="left")
print("\nMERGE USING left:-")
print(df_Marge3)

# RIGHT
df_Marge4 = pd.merge(df_Customers, df_Orders, on="CustomerID", how="right")
print("\nMERGE USING right:-")
print(df_Marge4)

# CROSS   
print("\nMERGE USING cross:-")
df_Marge5 = pd.merge(df_Customers, df_Orders, how="cross")
print(df_Marge5)