#Create an array and traverse it.

from array import*

arr1 = array('i',[1,2,3,4,5,6,7])
def searchElement(array):
    for i in array:
         print(i)
searchElement(arr1) 

#Time Complexity:O(n)
#Space Complexity:O(1)
