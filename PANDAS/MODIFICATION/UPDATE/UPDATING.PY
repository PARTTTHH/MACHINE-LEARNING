"""
UPDATING DATA IN A ROW 
HAVE TWO OPTIONS

    1. UPDATE SINGLE SPECIFIC VALUE
            .loc[] METHOD 
    SYNTAX:-
        df.loc[row_index, "Column_name"] = New_Value

    2. UPDATE A EXISTING COLUMN
           CONDITION BASED UPDATE
        df["SALARY"] = df["SALARY"] * 1.10

"""

import pandas as pd

data = {
    "NAME":['RAJ','SHUBHAM','RAM','VISHAVARAJ','SARTHAK'],
    "AGE":[25,22,19,18,23],
    "PERFORMANCE_SCORE":[72,86,70,98,89],
    "SALARY":[55000,45000,90000,35000,65000],
    "ADDRESS":['KOLHAPUR','PUNE','MUMBAI','SATARA','SANGALI']
}

df = pd.DataFrame(data)

print("SAMPLE DATA:-")
print(df)

print()
print()

#LETS UPDATES RAJ'S PERFORMANCE_SCORE 72 -> 82
df.loc[0, "PERFORMANCE_SCORE"] = 82
print("AFTER UPDATING RAJ'S PERFORMANCE SCORE:-")
print(df)

print()
print()

#LETS UPDATE SALARY INCREASING BY 10% FOR EVERYONE
df["SALARY"] = df["SALARY"] * 1.10
print("AFTER UPDATE SALARY COLUM:-")
print(df)
