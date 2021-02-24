#Write a function to find the missing number in a given integer array of 1 to 100.

MyList = [1,2,3,5,6]

def missingNumber(myList,totalCount):
    sum1 = totalCount*(totalCount+1)/2
    sum2 = sum(myList)
    return int(sum1-sum2)
    
print(missingNumber(MyList,6))

#Output: 4

#Time Complexity:O(1)
#Space Complexity:O(1)