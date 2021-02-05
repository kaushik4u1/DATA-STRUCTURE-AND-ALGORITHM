#Updating items in a product list.

productlist = [1,2,3,4,5,6,7,8]
print(productlist)

productlist[3]= 33
print(productlist) #1st Updated List

productlist[5]= 55
print(productlist) #2nd Updated List

#Output:[1, 2, 3, 4, 5, 6, 7, 8]
#       [1, 2, 3, 33, 5, 6, 7, 8]
#       [1, 2, 3, 33, 5, 55, 7, 8]

#Time Complexity:O(1)
#Space Complexity:O(1) 