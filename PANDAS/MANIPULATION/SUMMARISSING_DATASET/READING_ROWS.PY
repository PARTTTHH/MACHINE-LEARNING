"""
READING DATA FOR THIS PANDAS PROVIDES TWO BUIT-IN FUNCTIONS FOR IT 
        1. file_name.head(n)        THIS FUNCTION DISPLAYS N NUMS FO LINES FROM START
        2. file_name.tail(n)        THIS FUNCTION DISPLAYS N NUMS FO LINES FROM LAST
        NOTE--- N IS BY DEFAULT 5
        
    HELPS IN DATA MONITORING OR FILE PRIVING 
"""


import pandas as pd

file = pd.read_csv("PANDAS/FOUNDATION/FILE_READING/sales_data_sample.csv", encoding="latin1")

print("READING FIRST 10 LINES OF THE DATA:---")
print(file.head(10))

print("READING LAST 10 LINES OF THE DATA:---")
print(file.tail(10))