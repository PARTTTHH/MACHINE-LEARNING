"""
describe() METHOD FOR TEXT OR CATEGRRICAL DATA 
IT RETURNS THIS INFO 
caount -> NUMS OF NON-MISSIGN VALUES
unique -> NUMBER OF DISTINCT VALUES  [city: ['pune', 'kolhapur', 'mumbai', 'kolhapur'] --- 3
top    -> MOST FREQUENT VALUE (MODE)
freq   -> HOW MANY TIMES TOP VALUES APPERS

-SYNTAX --- 
            df.describe(include="object")

"""

import pandas as pd

data = {
    "City": ["Pune", "Mumbai", "Pune", "Delhi", "Mumbai"],
    "Department": ["IT", "HR", "IT", "HR", "IT"]
}

df = pd.DataFrame(data)
print(df.describe(include="object"))
