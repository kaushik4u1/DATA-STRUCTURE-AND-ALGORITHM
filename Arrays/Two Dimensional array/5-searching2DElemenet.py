#Searching for an element in 2D Array.

import numpy as np
twoArray = np.array([ [1,3,4,5],[11,32,43,54],[23,65,34,41],[22,32,43,54] ])
def searchElement(array,value):
    for i in range(len(array)): 
         for j in range(len(array[0])):
              if array[i][j] == value:
                      return 'The Value is located at index:'+'row-'+str(i)+" "+'column-'+str(j)
    else:
         return 'This value is invalid'            
searchElement(twoArray,18) 

#Time Complexity:O(n^2)
#Space Complexity:O(1)
