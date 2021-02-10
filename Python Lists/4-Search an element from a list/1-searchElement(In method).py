#Search an element from a list by "IN Method".

productlist = [1,2,3,4,5,6,7,8]

if 3 in productlist:
    print("It exists in the list at index:",productlist.index(3))
else:
    print("It does not exist in the list.")
    
#Output:It exists in the list at index: 2


#Time Complexity:O(n)
#Space Complexity:O(1)

