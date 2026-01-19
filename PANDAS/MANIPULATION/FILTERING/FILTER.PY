"""
FILTERING ALSO POSSIBLE IN PANDAS FOR THAT ALSO WE HAVE OPTIONS 
    1. FILTERING BASED ON SINGLE CONDITION

    syntax:- 
            filtered_data = df[df['apply_condition_on_this_column'] operation/condition here operant here]
                ex--    High_Salary = df[df['SALARY'] > 50000]

    2. FILTERING BASED ON MULTIPLE CONDITIONS 
                ex--    High_Salary = df[(df['SALARY'] > 50000) & (df['AGE] > 20)]

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

print("SAMPLE DATASET :-")
print(df)

print()
print()

print("FILTERING BASED ON SINGLE CONDITION :-")

High_Salary = df[df['SALARY'] > 50000]
print(High_Salary)

print()
print()

print("FILTERING DATA BASED ON MULTIPLE CONDITION :-")

SOMETHING = df[(df['SALARY'] > 50000) & (df['AGE'] > 20)]
print(SOMETHING)

print()
print()

print("FILTERING DATA BASED ON MULTIPLE CONDITION BUT EVEN IF ONE IS SATISFIED IS OKAY FOR THAT WE USE OR OPERATOR :-")

FILTERING_EX = df[(df['SALARY'] > 50000) | (df['PERFORMANCE_SCORE'] > 90)]
print(FILTERING_EX)