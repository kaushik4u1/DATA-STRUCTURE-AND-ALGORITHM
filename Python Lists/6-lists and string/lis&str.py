#String and list.

a = ('spam')
b = ('spam spam2 spam3')
delimiter ='a'

print(list(a)) #The list() constructor returns a list in Python.

c = b.split(delimiter) #The split() method breaks up a string at the specified separator and returns a list of strings.
print(c)

print(delimiter.join(c)) #The join() string method returns a string by joining all the elements of an iterable, separated by a string separator.


#Output:['s', 'p', 'a', 'm']
#       ['sp', 'm sp', 'm2 sp', 'm3']
#       spam spam2 spam3











