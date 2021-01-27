#Deletion of Row/Column in 2D Array.

import numpy as np
twoArray = np.array([ [1,3,4,5],[11,32,43,54],[23,65,34,41],[22,32,43,54] ])

newArray= np.delete(twoArray,1,axis=1) #Syntax:numpy.delete(arr, obj, axis=None) arr=Array Name,obj=index of row/column which you want to delete,axis=0/1(0-row,1-column)
print(newArray)

#Time Comlexity:O(mn)
#Space Complexity:O(1)
