import pandas as pd

Data = {
    "Name" : ['PARTH', 'RAGINI', 'KOMAL'],
    "AGE" : [19,21,21],
    "City" : ['KOLHAPUR', 'MUMBAI', 'PUNE']
}

File = pd.DataFrame(Data)
print(File)

# File.to_csv("OUTPUT.csv", index=False)                #SAVE AS CSV FILE WITH FOLLOWIGN DATA
# File.to_json("OUTPUT.json", index=False)              #SAVE AS JSON FILE WITH FOLLOWING DATA
File.to_excel("OUTPUT.xlsx", index=False)               #SAVE AS EXCEL FILE WITH FOLLOWIGN DATA 