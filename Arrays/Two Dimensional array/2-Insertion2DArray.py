#Insertion in two dimensional array

import numpy as np

twoArray = np.array([ [1,3,4,5],[11,32,43,54],[23,65,34,41],[22,32,43,54] ])
Addingcolumn=np.insert(twoArray,0,[1,2,3,4],axis=1) #Call "numpy. insert(arr, idx, values, axis=1)" to insert values as a column to the array arr at index idx .
                                                    #Call "numpy. insert(arr, idx, values, axis=0)" to insert values as a row to the array arr at index idx .
print(Addingcolumn)

#Time Complexity:O(mn)
#Space Complexity:O(mn)
