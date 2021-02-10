#delete an element from a list.

productlist = [1,2,3,4,5,6,7,8]
productlist.pop(2) #The pop() method removes the item at the given index from the list and returns the removed item.
print(productlist)

del productlist[3:5] #del is a Python keyword. And, obj_name can be variables, user-defined objects, lists, items within lists, dictionaries etc.
print(productlist)

productlist.remove(2) #The remove() method removes the first matching element (which is passed as an argument) from the list.
print(productlist)

#Output:[1, 2, 4, 5, 6, 7, 8]
#       [1, 2, 4, 7, 8]
#       [1, 4, 7, 8]

#Time Complexity:O(n) #Time complexity for pop() method can be O(1).
#Space Complexity:O(1)

