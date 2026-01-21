"""
LETS REPLACE MISSING VALUES USING fillna() METHOD

-THERE ARE TWO OPTIONS TO REPLACE THE MISSING VALUES:-
    1. REPLACE ALL MISSING VALUES WITH SPECIFIC VALUE LIKE 0 OR SOMETHING LIKE THAT
SYNTAX:-
        df.fillna(here_that_specific_values , inplace=True/False)
        ex - df.fillna(00, inplace=False)

    2. REPLACE WITH A CALCULATED VALUE
SYNTAX:-
        df["column_name"].fillna(df["column_name"].mean()/median()/mode(), inplace=True/False)
        ex - df3["AGE"].fillna(df3['AGE'].mean(), inplace=True)
             df3["SALARY"].fillna(df3['SALARY'].median(), inplace=True)

        
"""

import pandas as pd

data = {
    "NAME":['RAJ','SHUBHAM','RAM','PRATIK','SARTHAK'],
    "AGE":[25,22,19,None,23],
    "PERFORMANCE_SCORE":[72,86,70,None,89],
    "SALARY":[55000,45000,90000,None,65000],
    "ADDRESS":['KOLHAPUR','PUNE','MUMBAI',None,'SANGALI']
}

df = pd.DataFrame(data)

print("SAMPLE DATA:-")
print(df)


print()
print()

# LETS REPLACE THAT MISSING VALUES WITH 00
print("DATAFRAME-2")
df2 = df.fillna(00, inplace=False)
print(df2)

print()
print()

#LETS CREATE A NEW COPY OF DF AND REPLACE MISSING VALUES WITH CALCULATED VALUES
print("DATAFRAME-3")
df3 = df
df3["AGE"].fillna(df3['AGE'].mean(), inplace=True)      #REPLACING MISSING AGE WITH CALCULATING MEAN OF AGES
df3["SALARY"].fillna(df3['SALARY'].median(), inplace=True)     #REPLACE MISSING SALARY WITH CALCULATING MEDIAN OF SALARY COLUMN
df3["PERFORMANCE_SCORE"].fillna(df3['PERFORMANCE_SCORE'].mean(), inplace=True)  #SAME LIKE AGE HERE
print(df3)