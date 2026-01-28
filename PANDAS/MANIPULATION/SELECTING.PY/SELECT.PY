"""
SYNTAX--- 
    FOR SINGLE SELECTION
        selected_column = df["column_name_here"]

    FOR MULTIPLE SELECTION
        seleced_columns = df[["column1", "column2"]]

NOTE :- 
        1. IF YOU SELECT A SINGLE COLUMN THEN ITS OUTPUT IS A SERIES --- ALSO PRINTS ACTUL NAME OF COLUMN AND DATA-TYPE OF THAT COLUMN
        2. IF YOU SELECT MULTIPLE COLUMNS THEN IT COME AS DATAFRAME

"""

import pandas as pd

data = {
    "NAME":['RAJ','SHUBHAM','RAM','VISHAVARAJ','SARTHAK'],
    "AGE":[21,22,19,20,23],
    "ROLL_NUMBER":[1,2,3,4,5],
    "ADDRESS":['KOLHAPUR','PUNE','MUMBAI','SATARA','SANGALI']
}

df = pd.DataFrame(data)

print("SAMPLE DATA IS :-")
print(df)

print()
print()

print("SELECTING SINGLE COLUMN:-")

AGE = df["AGE"]
print(AGE)

print()
print()

print("SELECTING MULTIPLE COLUMNS:-")

NAME_WITH_AGE = df[["NAME", "AGE"]]
print(NAME_WITH_AGE)