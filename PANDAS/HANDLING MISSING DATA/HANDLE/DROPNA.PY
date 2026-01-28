"""
1. REMOVE THAT DIRECTLY
    dropna()
SYNTAX:-
        df.dropna()  --> (axis=0/1 inplace = True/False)
                            axis = 0 MEANS REMOVE THAT ROW
                            axis = 1 MEANS REMOVE THAT COLUMN
                            inplace = True MEANS MAKE CHNAGE IN ORIGINAL ONE DATASET OR DATAFRAME
                            inplance = False MEANS DONT MAKE CHANGE IN OGIGINAL ONE DATASET OR DATAFRAME


2. REPLACE THAT WITH ANOUTHER VALUE 
    fillna()
SYNTAX:-
        df.fillna(value, inplace=True/False)
                        #     -- SAME WORK LIKE dropna() METHODS inplace

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

#LETS REMOVE ALL NULL OR MISSING VALUES
print("DATAFRAME-2")
df2 = df.dropna(inplace=False)                  #CREATES A NEW DATAFRAME WITH NO MISSING VALUES ALL REMOVES WITH THE HELP OF dropna() METHOD
print(df2)                                     
print()
print()

print("DATAFRAME-3")
df3 = df.dropna(inplace=False, axis=1)          #RETURNS A EMPTY DATAFRAME BECOUSE EVERY COLUMN HAVES A MISSING VALUES SO PANDAS REMOVES EVERY COLUMN AND MAKES A EMPTY DF
print(df3)



print()
print()
print(type(df))
print(type(df2))
print(type(df3))



""" 
EXTRA BUT NOT FQUENTLY USED:---

-DROP ROWS ONLY IF ALL VALUES ARE MISSING:-
SYNTAX:-
        df.dropna(how="all")

--KEEP ROWS WITH AT LEAST N NON-NULL VALUES:-
SYNTAX:-
        df.dropna(thresh=3)

---DROP BASED ON SPECIFIC COLUMNS:=
SYNTAX:-
        df.dropna(subset=["AGE", "SALARY"])
"""