#How to delete/remove an element from dictionary.

myDict = {'Name':'Sam', 'Age':26, 'Address':'USA'} #dict{}-can use to create a dictionary.

myDict.pop('Name') #The pop() method removes and returns an element from a dictionary having the given key.
print(myDict)

myDict.popitem()   #The Python popitem() method removes and returns the last element (key, value) pair inserted into the dictionary.
print(myDict)

myDict.clear()     #The clear() method removes all items from the dictionary.
print(myDict)

#Output: {'Age': 26, 'Address': 'USA'}
#        {'Age': 26}
#        {}


#Time Complexity:Amorized O(n)
#Space Complexity:O(1)
