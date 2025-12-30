# SOMETIMES WE JUST WANT A ARRAY'S WITH JUST
# A DEFALUT VALUES AND AFTER SOME TIME WE REPLCE 
# THAT DEFALUT VALUES WITH OUR ACTUAL VALUES, FOR THAT
# NUMPY PROVIDES A BUILT IN FUCTIONS FOR IT 
# 1. ZEROS FUNCTION     np.zeros((shape))
# 2. ONES FUNCTION      np.ones((shape))
# WE HAVE ONE MORE OPTION FOR CREATING ARRAYS WITH SPECIFIC VALUES FUNCTION NAMED FULL FUNCTION
# 3. FULL FUNCTION      np.full((shape), value)

import numpy as np

# ZEROS FUNCTION 
print("ZEROS DEFALUT VALUE FUNCTION IN NUMPY")
arr1 = np.zeros((3,3))
print(arr1)
print()

# ONES FUNCTION 
print("ONES DEFALUT VALUE FUNCTION IN NUMPY")
arr2 = np.ones((3,3))
print(arr2)
print() 

# FULL FUNCTION 
print("FULL FUNCTION WITH OUR SPECIFIC VALUE!")
arr3 = np.full((3,3),5)
print(arr3) 


arr = np.array([1,2,3,4,5,6,7,8,9,10])
arr2 = np.array([1,2,3,4,5,6,7,8,9,10])
arr3 = arr + arr2 
print(arr3)
