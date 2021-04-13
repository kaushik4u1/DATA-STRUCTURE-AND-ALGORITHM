#A tuple in Python is similar to a list. The difference between the two is that we cannot change the elements of a tuple once it is assigned whereas we can change the elements of a list.

#Creating a Tuple
#A tuple is created by placing all the items (elements) inside parentheses (), separated by commas. The parentheses are optional, however, it is a good practice to use them.

#A tuple can have any number of items and they may be of different types (integer, float, list, string, etc.).

# Different types of tuples

# Empty tuple
my_tuple = ()
print(my_tuple)

# Tuple having integers
my_tuple = (1, 2, 3)
print(my_tuple)

# tuple with mixed datatypes
my_tuple = (1, "Hello", 3.4)
print(my_tuple)

# nested tuple
my_tuple = ("mouse", [8, 4, 6], (1, 2, 3))
print(my_tuple)

#Output:()
#       (1, 2, 3)
#       (1, 'Hello', 3.4)
#       ('mouse', [8, 4, 6], (1, 2, 3))

#A tuple can also be created without using parentheses. This is known as tuple packing.

my_tuple = 3, 4.6, "dog"
print(my_tuple)

# tuple unpacking is also possible
a, b, c = my_tuple

print(a)      # 3
print(b)      # 4.6
print(c)      # dog
Output

#Output:(3, 4.6, 'dog')
#        3
#        4.6
#        dog
