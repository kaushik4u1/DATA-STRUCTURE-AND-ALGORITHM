#Count the frequency of words appearing in a string in python.

n = input('Enter your String:')
l = n.split()
d = {}
for i in l:
    if i not in d.keys():
        d[i] = 0
    d[i] = d[i] + 1   
print(d)    

#Output:Enter your String:hello kam hello
#       {'hello': 2, 'kam': 1}
    
#Count the frequency of words appearing in a string in python by another method

n = input('Enter your String:')
l = n.split()
d = {}
for i in l:
    d[i] = d.get(i, 0) + 1   
print(d)    

#Output:Enter your String:hello kam hello
#       {'hello': 2, 'kam': 1}
    
