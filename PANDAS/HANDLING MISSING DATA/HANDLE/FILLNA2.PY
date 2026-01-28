"""
FORWARD-FILL METHOD IN FILLNA()
    THIS METHOD USES SAME DATA FROM PRIVIOUS ONE FROM MISSING VALUE 
SYNTAX :-
        df.ffill(inplace=True/False)

BACKWARD-FILL METHOD
    THIS METHOD USES SAME DATA FROM NEXT ONE FROM THE MISSING VALUE
SYNTAX :- 
        df.bfill(inplace=True/False)

NOTE :--
        ffill ---> FORWARD FILL METHOD
        bfill ---> BACKWARD FILL METHOD
        BOTH MAINLY USED IN TIME-SERIES DATA,LOGS, SENSOR REASINGS, AND SEQUENTIAL DATASETS
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
print("HERE I HAVE THIS SAMPLE DATA:-")
print(df)

print()
print()

df2 = df.ffill(inplace=False)
print("DATAFRAME-2 AFTER FILLING MISSING VALUES WITH FORWARD FILL METHOD:-")
print(df2)

print()
print()

df3 = df.bfill(inplace=False)
print("DATAFRAME-3 AFTER FILLING MISSING VALUES WITH BACKWARD FILL METHOD:-")
print(df3)