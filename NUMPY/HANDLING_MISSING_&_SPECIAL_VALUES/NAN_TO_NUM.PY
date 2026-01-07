"""
WE SEE WHY WE CAN FIND MISSING OR NOT A NUMBER VALUE LETS SEE HOW WE CAN REPLCE THAT VALUES WITH 
OUR REAL VALUES BUT BEFOR THAT WE NEED TO CONVERT THAT ARRAY INTO NUMS AGAIN FOR THAT WE HAVE 
AGAIN A BUIT-IN NUMPY FUNTION 
                        np.nan_to_num(arr)          
BY DEFAULT NAN VALUE GET 0 
"""
import numpy as np

arr = np.array([1,2,3,np.nan,4,5,np.nan])

cleaner_arr = np.nan_to_num(arr)

print(cleaner_arr)