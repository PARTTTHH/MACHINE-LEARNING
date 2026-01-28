"""
QUATION--- WHATS IS THE NAME OF COLUMNS IN A DATASET

        .columns -ATTRIBUTE

SYNTAX --- 
                DataFrame.columns
"""

import pandas as pd

data = {
    "NAME":['RAJ','SHUBHAM','RAM','VISHAVARAJ','SARTHAK'],
    "AGE":[21,22,19,20,23],
    "ROLL_NUMBER":[1,2,3,4,5],
    "ADDRESS":['KOLHAPUR','PUNE','MUMBAI','SATARA','SANGALI']
}


df = pd.DataFrame(data)

print(f"THE NAME OF COLUMNS IN DATASET IS :- {df.columns}")