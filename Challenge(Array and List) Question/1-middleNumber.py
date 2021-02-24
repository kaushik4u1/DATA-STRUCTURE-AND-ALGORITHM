#Write a function called middle that takes a list and return a new list that contains all but the first and last elements.

mylist = [1,2,3,4,5,6]

def middle(lst):
    list1 = lst[1:-1]
    return list1
    
    
print(middle(mylist))  

#Output: [2, 3, 4, 5]

#Time Complexity: O(1)
#Space Complexity: O(1)