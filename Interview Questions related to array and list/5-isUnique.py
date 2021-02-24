# Check if the given list is Unique or not!

mylist = [1,2,3,54,6,7,5,67,11,12,12,13,14,15,16.17,18,19,20]

def isUnique(array):
    a=[]
    for i in array:
        if i in a:
            print(i)
            return False
        else:
            a.append(i)
    return True

print(isUnique(mylist))


#Output:12
#       False
 