"""
VECTORIZATION MEANS PERFORMING OPERATIONS ON ENTIRE ARRAY AT ONCE 
INSTEAD OF USING LOOPS
    -NUMPY OPERATIONS RUN IN COMPITED C
    -USES CPU cache EFFICIENTLY
    -NO LOOPS 
    -MORE SPEED
    -CLEANER CODE
"""
import numpy as np

arr = np.array([1,2,3,4,5,6,7,8,9,10])

result = []
result = arr*2
print(result)


"""
result=[]
for i in arr:               WHEN WE HAVE BIG DATASETS ITS SLOW
    result.append(arr*2)
"""