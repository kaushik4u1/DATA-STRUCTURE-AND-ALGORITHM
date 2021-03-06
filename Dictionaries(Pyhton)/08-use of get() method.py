#How to get any element and value from the given dictionary.

#The get() method returns the value for the specified key if key is in dictionary.
#get() Parameters
#get() method takes maximum of two parameters:

#key - key to be searched in the dictionary
#value (optional) - Value to be returned if the key is not found. The default value is None.


#Example 1: How get() works for dictionaries?

person = {'name': 'Phill', 'age': 22}

print('Name: ', person.get('name'))
print('Age: ', person.get('age'))

# value is not provided
print('Salary: ', person.get('salary'))

# value is provided
print('Salary: ', person.get('salary', 0.0))

#Output:Name:  Phill
#       Age:  22
#       Salary:  None
#       Salary:  0.0

#Python get() method Vs dict[key] to Access Elements
#get() method returns a default value if the key is missing.

#However, if the key is not found when you use dict[key], KeyError exception is raised.

person = {}

# Using get() results in None
print('Salary: ', person.get('salary'))

# Using [] results in KeyError
print(person['salary'])
#Output:Salary:  None
#Traceback (most recent call last):
# File "", line 7, in 
#   print(person['salary'])
#KeyError: 'salary'
