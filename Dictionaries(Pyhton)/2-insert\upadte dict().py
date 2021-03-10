#How to update/insert in a dictionary.

engTosp = {"Name":"Sam","Age":"26"} #dict{}-can use to create a dictionary.
engTosp['Age']= 27 #Like this we can update any value.
print(engTosp)

#Output: {'Name': 'Sam', 'Age': 27}

#Time Complexity:O(1)
#Space Complexity:O(1)

#If we want to insert the new key:value pair in dictionary we can do this like:
engTosp["Address"]="USA"
print(engTosp)

#Output: {'Name': 'Sam', 'Age': 27, 'Address': 'USA'}

#Time Complexity:O(1)
#Space Complexity:amortized O(1)
