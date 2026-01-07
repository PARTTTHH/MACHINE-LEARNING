"""AFTER ALL ONE MORE FUNCTION IS LEFT WHICH IS 
                    np.isinf(arr)
   THIS FUNCTION HELPS TO DETAICT INFINITE VALUES IN OUR ARRAY 
   AGAIN IT IS RETUERNS A BOOLEAN ARRAY FOR REPLACE THAT INF VALUES WE CAN USE nan_to_num FUNCTION
   TO REPLACE THAT VALUE THERE WE HAVE TWO OPTIONS POSSITIVE INFITINE AND NEGATIVE INFINITE 
   LETS SEE IN EXAMPLE    
                    posinf = possitive infinite 
                    neginf = positive infinite
"""

import numpy as np

arr = np.array([1,2,3,np.inf,4,5,6,-np.inf])

print(np.isinf(arr))

cleaner_array = np.nan_to_num(arr, posinf=100, neginf=-100)
print(cleaner_array)