#How to calculate the power of a number using recursion?
def power(base, exponent):
    if exponent < 0:
         d=negpower(base,-exponent)    
         return d
    if exponent == 0:
         return 1
    if exponent == 1:
         return base
    else:
         return base * power(base,exponent-1) 
         
def negpower(base,exponent):
    if exponent == 0:
         return 1
    else:
         return 1/(base * power(base,exponent-1))
         
power(base,exponent)         