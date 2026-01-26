""" 
LETS SORT MULTIPLE COLUMNS AT ONCE
FOR THAT JUST NEED TO PASS A LIST THAT CONTAIN NAMES OF COLUMNS

SYNTAX:-
        df.sort_values(by=['column1', 'column2', ....], ascending=T/F, inplace=T/F)

RULE:
- First column = PRIMARY sort key
- Second column = SECONDARY sort key (used only when primary values are equal)

"""

import pandas as pd

data = {
    "A":[3,5,2,1,4],
    "B":[30,20,40,50,10]
}

df = pd.DataFrame(data)
print("ORIGINAL DATAFRMAE:-")
print(df)

df.sort_values(by=['A','B'], ascending=[True, False], inplace=True)
print("AFTER SORTING DATAFRAME:-")
print(df)


"""
HOW PANDAS SORTS HERE:

1. Pandas FIRST sorts by column 'A' (PRIMARY KEY)
   -> All rows with A = 1 come first
   -> Then all rows with A = 2

2. Pandas THEN sorts by column 'B'
   -> BUT ONLY WITHIN THE SAME 'A' GROUP
   -> Rows where A = 1 are sorted by B
   -> Rows where A = 2 are sorted by B
"""