# STARTING LERNING PANDAS 
# PANDAS IS A POWERFULL AND POPULAR PYHTON LIBRARY DESIGNED FOR DATA MANIPULATON(CLEANING,TRANSFORMING,STRUCTURING)
# AND DATA ANALYSIS(FINDING PATTERNS, TREADS AND INSIGHTS)

"""IN THIS FILE WE LERN HOW TO READ DATA FROM FILES LIKE CSV,JSON,EXCEL FILES 
WITH THE HELP OF BUIT-IN FUNCTIONS LIKE 
    read_csv(file_path_here) FOR CVS FILES
    read_json(file_path_here) FOR JSON FILES
    read_excel(file_path_here) FOR ECEL FILES
"""


import pandas as pd

print("CSV FILE:---")
read_csv = pd.read_csv("PANDAS/FOUNDATION/FILE_READING/sales_data_sample.csv", encoding="latin1")
print(read_csv)

print()

print("JSON FILE:---")
read_json = pd.read_json("PANDAS/FOUNDATION/FILE_READING/sample_Data.json")
print(read_json)

print()

print("EXCEL FILE:---")
read_excel = pd.read_excel("PANDAS/FOUNDATION/FILE_READING/SampleSuperstore.xlsx")
print(read_excel)