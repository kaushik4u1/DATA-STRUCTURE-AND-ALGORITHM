#How to traverse through a dictionary.

myDict = {'Name':'Sam', 'Age':26, 'Address':'USA'} #dict{}-can use to create a dictionary.
def traverseDict(dicti):
    for key in dicti:
        print(key, dicti[key])
traverseDict(myDict)

#Output: Name Sam
#        Age 26
#        Address USA


#Time Complexity:O(n)
#Space Complexity:O(1)
