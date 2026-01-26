"""
SORTING:-
        SORTING MEANS ARRANGING DATA IN A SPECIFIC ORDER
        1. ASCENDING ORDER [SMALL-BIG]
        2. DESCENDING ORDER [BIG-SMALL]
    
    USED EVERYWHERE: DATA ANALYSIS
                     RANKING
                     CLEANING DATA
                     ML PREPROCESSING
        
    SYNTAX:-
            df.sort_values(by="Column_name", ascending=T/F, inplace=T/F)
"""

import pandas as pd

# SORTING A SERIES
s = pd.Series([60,40,80,20,90,30,10,50,70,100])
print("ORIGINAL SERIES:-")
print(s)

print()
print()

s.sort_values(ascending=True, inplace=True)        #DONT NEED TO PASSING COLUMN NAME HERE
print("AFTER SORTING VALUES:-")
print(s)

print()
print()

#SORTING A DATAFRAME
data = {
    "NAME":['A', 'Q', 'C', 'R', 'Y', 'S' , 'K'],
    "MARKS":[45, 34, 50, 32, 42, 39, 40]
}
df = pd.DataFrame(data)
print("ORIGINAL DATAFRAME:-")
print(df)

print()
print()

df.sort_values(by="NAME", ascending=True, inplace=True)
# df.sort_values(by="MARKS", ascending=True, inplace=True)
print("DATAFRAME AFTER SORTING:-")
print(df)

print()
print()

# SORTING BY DESCENDING ORDER EX
s2 = pd.Series([1,2,3,4,5,6,7,8,9,10])
print(s2)

print()
print()

s2.sort_values(ascending=False, inplace=True)
print(s2)