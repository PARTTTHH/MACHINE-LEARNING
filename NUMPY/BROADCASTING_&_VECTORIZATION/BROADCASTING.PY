import numpy as np

arr = np.array([1,2,3])
arr2 = np.array([2])
result = arr + arr2
print(result)

print()

arr3 = np.array([2,3,4])
arr4 = np.array([[2],[2],[2]])
result2 = arr3 + arr4
print(result2)

print()

arr5 = np.array([3,2,1])
arr6 = np.array([2,2])
result3 = arr5 + arr6
print(result3)          #THIS GIVES ERROR CPZ BROADCASTING NOT ABLE TO ADJEST ARRAYS IN THIS CASE OR SITUATION
