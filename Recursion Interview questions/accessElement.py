#Check if the asked array value is available in the given array.

from array import*

arr1 = array('i',[1,2,3,4,5,6,7])
def accessElement(array,index):
    if index > len(array):
         print("This index does not exist")
    else:
         print(array[index])

accessElement(arr1,index)           
