# Calculate Average Temperature

numDays = int(input("How much day(s) temperature?"))
total = 0
nextDays=0
for i in range(1,numDays+1):
    nextDays = int(input("Day " + str(i) + "'s high temp:"))
    total += nextDays
    
    
avg = round(total/numDays,2)    
print("The average is: " +str(avg))

#Output: How much day(s) temperature?2
#        Day 1's high temp:3
#        Day 2's high temp:4
#        The average is: 3.5
