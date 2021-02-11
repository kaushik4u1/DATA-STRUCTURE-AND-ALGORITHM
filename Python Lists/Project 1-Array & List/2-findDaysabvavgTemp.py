# Find the Days Above Average Temperature using list.

numDays = int(input("How many day's temperature?"))
total = 0
temp=[]
for i in range(numDays):
    nextDays = int(input("Day " + str(i+1) + "'s high temp:"))
    temp.append(nextDays)
    total += temp[i]

avg = round(total/numDays,2)

print("The average is: " +str(avg))
above = 0
for i in temp:
    if i>avg:
        above += 1
print(str(above) + " Day(s) above average")

#Output: How many day's temperature?3
#        Day 1's high temp:1
#        Day 2's high temp:2
#        Day 3's high temp:2
#        The average is: 1.67
#        2 Day(s) above average