#Accessing an element in two dimensional array

import numpy as np

twoArray = np.array([ [1,3,4,5],[11,32,43,54],[23,65,34,41],[22,32,43,54] ])

def accessElement(array,rowidx,colidx):
    if rowidx >= len(array) and colidx >= len(array[0]):
         print("Invalid Index")
    else:
         print(array[rowidx][colidx])

accessElement(twoArray,rowidx,colidx)      

#Time Complexity:O(1)
#Space Complexity:O(1)
