"""
PANDAS PROVIDES ONE MORE ATTRIBUTE FOR DESCRIBE METHOD WHICH IS 'all'

GIVES ---
NUMERICAL SUMMARY
TEXT SAMMARY
DATA SAMMARY (IF AVAILABLE)

NOTE -- ITS TRIES TO SAMMARIZE EVERY COLUMN

-SYNTAX -- 
            df.describe(include="all")

"""

import pandas as pd

data = {
    "Name": ["A", "B", "C", "A"],
    "Age": [20, 25, 30, 20],
    "Salary": [30000, 40000, 50000, 30000]
}

df = pd.DataFrame(data)
print(df.describe(include="all"))



"""
---OUTPUT NOTE :-
Why Some Values Are NaN?
Text columns → no mean, std, min, max
Numeric columns → no unique, top, freq
"""