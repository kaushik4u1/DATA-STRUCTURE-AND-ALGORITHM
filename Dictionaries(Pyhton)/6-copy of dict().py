#How to return a shallow copy of a dictionary using 'copy()' method.

original = {1:'one', 2:'two'}
new = original.copy()

print('Orignal: ', original)
print('New: ', new)

#Output: Orignal:  {1: 'one', 2: 'two'}
#        New:  {1: 'one', 2: 'two'}
