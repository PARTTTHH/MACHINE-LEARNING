# HERE WE CONVERT A LIST INTO A NP ARRAY NUMPY PROVIDES A FUNCTION FOR IT 
# np.array([list here])  FUNCTION 

import numpy as np

arr = np.array([1, 2, 3, 4, 5])
print(arr)
print()

l = [2, 4, 6, 8, 10]   # OUR LIST TO CONVERT INTO ARRAY
print("LETS CHECK TYPE OF l FIRST THEN CONVERT INTO ARR AND CHECK AGAIN")
print(f"l = {l}")
print(type(l)) 

print()

arr_f_list = np.array(l)     
print(arr_f_list)
print(type(arr_f_list))
