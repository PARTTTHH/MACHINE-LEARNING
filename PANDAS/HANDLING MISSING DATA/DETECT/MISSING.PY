"""
TO HANDLING MISSING DATA IN A DATAFAME
 .isnull() METHOD

WHICH RETURNS 
        True ---> FOR MISSING VALUES 
        False ---> FOR NON-MISSING VALUES

SYNTAX:-
    DataFrame.isnull()
"""

import pandas as pd

data = {
    "NAME":['RAJ','SHUBHAM','RAM',None,'SARTHAK'],
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

#TO DETECT MISSING OR NONE VALUES 
print("LETS DETECT MISSING VALUES:-")
print(df.isnull()) 

print()
print()

""".sum() RETURNS A SERIES WHICH REPRESENTS HOW MANY VALUES ARE MISSING IN THAT COLUMNS"""
print("NUMS OF MISSING VALUES USING .sum() METHOD:-")
print(df.isnull().sum()) 