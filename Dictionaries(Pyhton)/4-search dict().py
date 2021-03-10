#How to search for a value in dictionary.

myDict = {'Name':'Sam', 'Age':26, 'Address':'USA'} #dict{}-can use to create a dictionary.
def searchVal(dicti,value):
    for key in dicti:
        if dicti[key] == value:
           return key, value
    return 'This value does not exist.' 
    
print(searchVal(myDict,26))
print(searchVal(myDict,27))

#Output: ('Age', 26)
#        This value does not exist.


#Time Complexity:O(n)
#Space Complexity:O(1)
