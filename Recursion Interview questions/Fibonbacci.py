#How to find Fibonacci numbers using Recursion?
def fibbonacci(n):
    assert n >=0 and int (n) ==n,'The number can only be positive integer' #for negative/point values
    if n in [0,1]:
         return n 
    else:
         return fibbonacci(n-1) + fib(n-2)
fibbonacci(n)         