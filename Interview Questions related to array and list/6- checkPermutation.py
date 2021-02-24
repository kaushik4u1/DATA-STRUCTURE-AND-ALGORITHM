#write a program to Check if the given lists is permutation or not.


mylist1 = [1,2.2,3.4,5]
mylist2 = [2.2,5,1,3.4]

mylist3 = [2,4,3,6,7]
mylist4 = [4,3,6,7,9]

mylist5 = ['joe','kar','tom']
mylist6 = ['tom','joe','kar']

def checkPermutation(list1,list2):
    if len(list1) != len(list2):
        return False
    list1.sort()
    list2.sort()
    if list1 == list2:
        return True
    else:
        return False
    
print(checkPermutation(mylist1,mylist2)) #----------------------Checking for float values.
print(checkPermutation(mylist3,mylist4)) #--------------------Checking for integer values.
print(checkPermutation(mylist5,mylist6)) #---------------------Checking for string values.

#Output: True
#        False
#        True

