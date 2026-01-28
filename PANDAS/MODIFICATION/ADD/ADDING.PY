"""
ADDING / INSERTING NEW COLUMN IN DATAFRAME 
THERE ARE TWO OPTIONS FOR ADDING COLUMN IN DATAFRAME 
        1. DIRECT ALIGNING  -- THIS IS STRAINGH FORWORD WAY

        SYNTAX:-
        df["column_name"] = some_data

        2. USING INSERT()   -- THIS IS RECCOMENTED AND REAL-WORD USES THIS ONE ALSO GIVES US FREEDOM TO INSERT THAT COLUMN AT APECIFIC POSSITION

        SYNTAX:-
        df.insert(location, "column_name", some_data)

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

#FIRST METHOD:-
df["BONUS"] = df["SALARY"] * 0.1

print("AFTER ADDING NEW COLUMN '/BONUS'/ USING FIRST METHOD :-")
print(df)

print()
print()

#SECOND METHOD:-
df.insert(0, "EMPLOYEE_ID", [200, 201, 202, 203, 204])

print("AFTER ADDING NEW COLUMN '/EMPLOYEE_ID'/ USING SECOND METHOS :-")
print(df)