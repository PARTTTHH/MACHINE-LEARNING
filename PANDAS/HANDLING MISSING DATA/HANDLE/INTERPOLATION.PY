""" 
INTERPOLATION MEANS FILLING MISSING VALUES INTERLLIGENTLY USING PATTERNS IN DATA
        ESTIMATION = INTERPOLATION
SO INTERPOLATION IS BETTER FOR NUMERIC, ORDERED DATA (TIME, SEQUENCE, INDEX)
        
SYNTAX:-
        df.interpolate()

TYPES OF INTERPOLATION:---
    1. LINEAR:-                                         Time series, Gradual change data
        ASSUMES STRAIGHT LINE BETWEEN VALUES
            SYNTAX:-  df.interpolate(method='linear')

    2. POLYNOMIAL :-                                    Scientific data, ml preproccessing 
        USES CURVES (MATH HEAVY)
            SYNTAX:- df.interpolate(method='polynomial', order=2)
"""

import pandas as pd

data = {
        "ROLL_NUMS":[1,2,3,4,5,6,7,8,9,10],
        "VALUE":[10,20,None,40,None,60,70,80,None,100],
        "SOMETHING":[5,25,None,65,85,None,125,145,None,185]
}

df = pd.DataFrame(data)
print("THIS IS SAMPLE DATAFRAME-1")
print(df)

print()

# LINEAR INTERPOLATION
df["VALUE"] = df['VALUE'].interpolate(method='linear')
print("AFTER MISSING VALUES FILLING USING LINEAR INTERPOLATION:-")
print(df)

print()

# POLYNOMIAL INTERPOLATION
df["SOMETHING"] = df['SOMETHING'].interpolate(method='polynomial', order=2)
print("AFTER FILLING MISSING VALUES USING POLYNOMIAL INTERPOLATION:-")
print(df)


"""
NOTE:-
    When NOT to Use Interpolation
    Categorical/text data
    Random or unordered data
    IDs, names, phone numbers
✔ Only numeric + ordered data

NOTE:
Polynomial interpolation requires the SciPy library.
If SciPy is not installed, Pandas will raise an ImportError.
"""