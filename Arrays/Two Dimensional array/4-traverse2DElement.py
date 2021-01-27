#Travesing elements in 2D Array.

import numpy as np
twoArray = np.array([ [1,3,4,5],[11,32,43,54],[23,65,34,41],[22,32,43,54] ])
def traverseElement(array):
    for i in range(len(array)): 
         for j in range(len(array)):
              print(array[i][j])
searchElement(twoArray) 

#Time Complexity:O(n^2)
#Space Complexity:O(1)
