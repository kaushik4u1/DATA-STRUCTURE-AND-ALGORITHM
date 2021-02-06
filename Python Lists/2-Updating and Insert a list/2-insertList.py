#Inserting items in a product list.

productlist = [1,2,3,4,5,6,7,8]
secondproductlist = ['Milk','Salt','Rice']
print(productlist)

productlist.insert(0,11) #The list insert() method inserts an element to the list at the specified index.
print(productlist) #1st inserted List

productlist.append(55) #The append() method adds an item to the end of the list.
print(productlist) #2nd Updated List

productlist.extend(secondproductlist) #The extend() method adds all the elements of an iterable (list, tuple, string etc.) to the end of the list.
print(productlist)


#Output:[1, 2, 3, 4, 5, 6, 7, 8]
#       [11, 1, 2, 3, 4, 5, 6, 7, 8]
#       [11, 1, 2, 3, 4, 5, 6, 7, 8, 55]
#       [11, 1, 2, 3, 4, 5, 6, 7, 8, 55, 'Milk', 'Salt', 'Rice']

#Time Complexity:O(n) (for append time complexity will be O(1))
#Space Complexity:O(n) (for append and insert space complexity will be O(1))
