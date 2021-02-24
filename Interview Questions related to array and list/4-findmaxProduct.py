# How to find maximum product of two integers in an array where all the elements are positive.

import numpy as np
mylist = np.array([1,2,3,54,6,7,5,3,67,11,12,13,14,15,16.17,18,19,20])

def maxProduct(array):
    maxProduct = 0    
    for i in range(len(array)):
        for j in range(i+1,len(array)): 
            if array[i] * array[j] > maxProduct:
                maxProduct = array[i] * array[j]
                pairs = str(array[i]) + " & " + str(array[j]) 
    print("The pair for maximum product will be:",pairs)
    print("And the maximum product will be:",maxProduct)
            
maxProduct(mylist)

#Output: The pair for maximum product will be: 54.0 & 67.0
#        And the maximum product will be: 3618.0
 