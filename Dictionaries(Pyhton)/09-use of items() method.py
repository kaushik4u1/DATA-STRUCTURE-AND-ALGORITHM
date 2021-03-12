                                    #Python Dictionary items()
#The items() method returns a view object that displays a list of dictionary's (key, value) tuple pairs.
#The syntax of items() method is:-----------dictionary.items()

#items() method is similar to dictionary's viewitems() method in Python 2.7.

#tems() Parameters
#items() method doesn't take any parameters.

#Return value from items()
#items() method returns a view object that displays a list of a given dictionary's (key, value) tuple pair.

#Example 1: Get all items of a dictionary with items()

# random sales dictionary
sales = { 'apple': 2, 'orange': 3, 'grapes': 4 }

print(sales.items())
#Output:dict_items([('apple', 2), ('orange', 3), ('grapes', 4)])



#Example 2: How items() works when a dictionary is modified?
# random sales dictionary
sales = { 'apple': 2, 'orange': 3, 'grapes': 4 }

items = sales.items()
print('Original items:', items)

# delete an item from dictionary
del[sales['apple']]
print('Updated items:', items)

#Output:Original items: dict_items([('apple', 2), ('orange', 3), ('grapes', 4)])
#       Updated items: dict_items([('orange', 3), ('grapes', 4)])



#The view object items doesn't itself return a list of sales items but it returns a view of sales's (key, value) pair.
#If the list is updated at any time, the changes are reflected on the view object itself, as shown in the above program.
