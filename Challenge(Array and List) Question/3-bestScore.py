#Given a list,Write a function to get first,second best scores from the list. List may contain duplicates.

myList = [23,43,55,67,7,89,76,44,56,78,98]
myList1 = [43,45,67,87,54,32,21,43,55,67,76]

def firstSecond(givenList):
    firstmax = 0
    secondmax = 0
    for i in givenList:
        if i >= firstmax:
            secondmax = firstmax
            firstmax = i
    
        elif i < firstmax and i > secondmax:
             secondmax = i
    return firstmax,secondmax
             
print(firstSecond(myList))
print(firstSecond(myList1))

#Output: (98, 89)
#        (87, 76)

#Time Complexity: O(n)
#Space Complexity: O(1)