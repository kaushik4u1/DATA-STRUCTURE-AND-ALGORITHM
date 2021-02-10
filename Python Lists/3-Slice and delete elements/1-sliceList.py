#Slice items from a product list.

productlist = [1,2,3,4,5,6,7,8]
print(productlist[:]) #The slice() function returns a slice object that can use used to slice strings, lists, tuple etc.

productlist[0:2] = ['x','y'] #By this we can change the starting 2 elements.
print(productlist)

productlist[-2] = ['w','U'] #By this we can insert new list at the  2nd end  position.
print(productlist)



#Output:[1, 2, 3, 4, 5, 6, 7, 8]
#       ['x', 'y', 3, 4, 5, 6, 7, 8]
#       ['x', 'y', 3, 4, 5, 6, ['w', 'U'], 8]


#Time Complexity:O(n)
#Space Complexity:O(1) 