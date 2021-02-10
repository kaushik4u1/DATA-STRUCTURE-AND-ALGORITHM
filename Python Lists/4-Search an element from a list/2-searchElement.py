#Search an element from a list by linear search method.

productlist = [1,2,3,4,5,6,7,8]

def pro_list(list,value):
    for i in list:
        if i == value:
            return 'it exist in the list at index:',list.index(value)
    return 'It does not exist in the list'
print(pro_list(productlist,2)) 
print(pro_list(productlist,12))

        

#Output:('it exist in the list at index:', 1)
#       It does not exist in the list

#Time Complexity:O(n)
#Space Complexity:O(1)

