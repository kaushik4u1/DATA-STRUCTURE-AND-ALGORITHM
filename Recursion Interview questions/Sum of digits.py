#How to find the sum of digits of a positive/negative integer number using recursion?
def sum(n):
     if n < 0:
        n = -1*n
     if n in [0]:
        return n
     else:
          return int(n%10) + sum(int(n/10))        

sum(n) 
