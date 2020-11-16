#How to convert a number from decimal to binary using recursion?
def decimaltobinary(n):
     assert int(n) == n,'The number must be integer only' #for point values
     if n == 0:
          return 0
     else:   
          return n%2 + 10 * decimaltobinary(int(n/2))

decimaltobinary(n)

