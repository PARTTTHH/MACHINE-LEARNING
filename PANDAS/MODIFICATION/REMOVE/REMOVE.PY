#REMOVING COLUMN FROM DATAFRAME
        # .drop(columns = [columns_name], inplace=True) METHOD
                                            # /\  THIS ATTRIBUTES GIVES PERMISSION TO MOFIFY MAIN DATAFRAME
                                             # OTHERWISE IT RETURNS A COPY OF ORIGNAL "CAN'T MAKE ANY CHANEG IN ORIGINAL DATFRAME"
"""
SYNTAX:-
        df.drop(solumns=["columns name"]) --- THIS IS FOR REMOVING SINGLE COLUMN
        df.drop(solumns=["columns1", "column2"....])
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

#LETS REMOVER ADDRESS COLUMN:-
df.drop(columns=["ADDRESS"], inplace=True)
print("AFTER REMOVING ADDRESS COLUMN:-")
print(df)

print()
print()


data2 = {
    "NAME":['RAJ','SHUBHAM','RAM','VISHAVARAJ','SARTHAK'],
    "AGE":[25,22,19,18,23],
    "PERFORMANCE_SCORE":[72,86,70,98,89],
    "SALARY":[55000,45000,90000,35000,65000],
    "ADDRESS":['KOLHAPUR','PUNE','MUMBAI','SATARA','SANGALI']
}

df2 = pd.DataFrame(data2)

# REMOVING MULTIPLE COLUMNS "AGE , ADDRESS":
df2.drop(columns = ["ADDRESS", "AGE"], inplace=True)
print("AFTER REMOVING ADRESS AND AGE COLUMNS FROM DF2:-")
print(df2)