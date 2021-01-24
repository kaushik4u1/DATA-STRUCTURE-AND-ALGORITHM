#Search for an element in array.

from array import*

arr1 = array('i',[1,2,3,4,5,6,7])
def searchElement(array,value):
    for i in array:
        if i == value:
             return array.index(value)
    else:
         return "This element does not exist in this array."  
searchElement(arr1,value) 



Time Complexity:O(n)
Space Complexity:O(1)
