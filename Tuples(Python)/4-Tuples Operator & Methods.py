#Tuples Operators/Functions(Methods)

#1-'+' Operator

myTuple = (1,3,4,5,7,8)
myTuple1 = (4,6,3,2,7,8)

print(myTuple + myTuple1) #'+' Operator is used to add multiple tuples and creates a new tuple.

#Output: (1, 3, 4, 5, 7, 8, 4, 6, 3, 2, 7, 8)

#Time Complexity:O(1)
#Space Complexity:O(n)

#2-'*' Operator
myTuple = (1,3,4,5,7,8)

print(myTuple * 4) #'*' Operator is used to create a new tuples where each element will be n times.

#Output:(1, 3, 4, 5, 7, 8, 1, 3, 4, 5, 7, 8, 1, 3, 4, 5, 7, 8, 1, 3, 4, 5, 7, 8)

#Time Complexity:O(1)
#Space Complexity:O(n)

#3-in Operator

myTuple = (1,3,4,5,7,8)

print(4 in myTuple) #Returns True if a sequence with the specified value is present in the object.

#Output:True

#Time Complexity:O(1)
#Space Complexity:O(1)





#Tuples Methods(Functions)

#There are only two methods in tuples.
#1-count() methods

myTuple = (1,3,4,5,7,8,3)

print(myTuple.count(3)) #count() method counts the occurrence of an element in the tuple. It returns the occurrence of the the element passed during call. It required a parameter which is to be counted. It returns error if the parameter is missing.

#Output:2 #Because element 3 came 2 times in myTuple.

#Time Complexity:O(1)
#Space Complexity:O(1)


#2-index() Method(Function)
myTuple = (1,3,4,5,7,8)

print(myTuple.index(3)) #index() method searches for the given element in a tuple and returns its position. It returns first occurrence of the element in the tuple. Index starts from 0 and end at n-1 where n is length of tuple.

#Output:1 #Because element 3 positioned at index 1.

#Time Complexity:O(1)
#Space Complexity:O(1)

#3- tuple function

myTuple = [1,3,4,5,7,8]

print(tuple(myTuple)) #tuple() function is used to convert the list into tuples.

#Output:(1, 3, 4, 5, 7, 8)

#Time Complexity:O(1)
#Space Complexity:O(1)






