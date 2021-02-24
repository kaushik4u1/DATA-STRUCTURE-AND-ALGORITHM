#Write a function to find the duplicate numbers on given integer array/list.

MyList = ([1,2,2,3,5,6,6,7,9,9])


def removeDuplicates(myList):
    return list(set(myList))
    
print(removeDuplicates(MyList))   

#Output: [1, 2, 3, 5, 6, 7, 9]

#Time Complexity:O(1)
#Space Complexity:O(1)