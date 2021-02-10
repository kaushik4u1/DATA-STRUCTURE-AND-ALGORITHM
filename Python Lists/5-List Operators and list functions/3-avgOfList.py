#function Operators.
#Write a program to find the average of elements in given list.

mylist = list()
while(True):
    inp = input("Enter the input:")
    if inp =='done': break
    value =float(inp)
    mylist.append(value)
average = sum(mylist)/len(mylist)

print("Average:",average)
#Output:Enter the input:4
#       Enter the input:5
#       Enter the input:6
#       Enter the input:done
#       Average: 5.0







