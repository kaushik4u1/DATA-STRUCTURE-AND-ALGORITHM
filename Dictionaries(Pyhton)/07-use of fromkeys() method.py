#How to create a new dictionary from the given sequence using 'fromkeys()' method.

#The fromkeys() method creates a new dictionary from the given sequence of elements with a value provided by the user.
#The syntax of fromkeys() method is:
# dictionary.fromkeys(sequence[, value])
#fromkeys() Parameters
#fromkeys() method takes two parameters:

#sequence - sequence of elements which is to be used as keys for the new dictionary
#value (Optional) - value which is set to each each element of the dictionary

myDict = {'a','e','i','u','o'} #dict{}-can use to create a dictionary.
newDict = dict.fromkeys(myDict) 
print(newDict)
value = 'vowel'                #value (Optional) - value which is set to each each element of the dictionary.
newDict = dict.fromkeys(myDict,value) 
print(newDict)   

#Output: {'i': None, 'e': None, 'u': None, 'a': None, 'o': None}
#        {'i': 'vowel', 'e': 'vowel', 'u': 'vowel', 'a': 'vowel', 'o': 'vowel'}
