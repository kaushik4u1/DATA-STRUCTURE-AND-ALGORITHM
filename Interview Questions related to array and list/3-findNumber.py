# Finding a number in an Array.

import numpy as np
mylist = np.array([1,2,3,54,6,7,5,3,67,11,12,13,14,15,16.17,18,19,20])

def searchElement(arr,num):
    for i in range(len(arr)):
        if arr[i] == num:
            print("Yes, it exist at index poition:",i)
            
searchElement(mylist,3)

#Output: Yes, it exist at index poition: 2
#        Yes, it exist at index poition: 7