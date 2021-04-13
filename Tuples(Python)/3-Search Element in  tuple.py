#How to search an Element in tuples.

ab = ('a','b','c','d','e','y')
def searchElement(myTuple,n):
    for i in myTuple:
        if i == n:
            return myTuple.index(i)
    return 'This Element Does Not Exist.'
print(searchElement(ab,'b'))
print(searchElement(ab,'m'))

#Output:1
#       This Element Does Not Exist.

#Time Complexity:O(n)
#Space Complexity:O(1)

