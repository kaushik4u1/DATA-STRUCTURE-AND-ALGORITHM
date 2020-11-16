#How to find factorial of numbers using Recursion?
def factorial(n):
    assert n >=0 and int (n) ==n,'The number can only be positive integer' #for negative/point values
    if n in [0,1]:
         return 1 
    else:
         return n * factotial(n-1)
factorial(n)         



