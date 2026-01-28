"""
QUATION--- WHATS IS THE NUMBERS OF ROWS AND COLUMNS OF A DATASET
        .shape -ATTRIBUTE

SYNTAX --- 
                DataFrame.shape
OUTPUT ---
    RETURNS IN A TUPLE FROMAT
                    (NUM_OF_ROWS , NUM_OF_CLUMNS)
"""

import pandas as pd

data = {
    "NAME":['RAJ','SHUBHAM','RAM','VISHAVARAJ','SARTHAK'],
    "AGE":[21,22,19,20,23],
    "ROLL_NUMBER":[1,2,3,4,5],
    "ADDRESS":['KOLHAPUR','PUNE','MUMBAI','SATARA','SANGALI']
}


df = pd.DataFrame(data)

print(f"THE SHAPE OF DATASET IS {df.shape}")