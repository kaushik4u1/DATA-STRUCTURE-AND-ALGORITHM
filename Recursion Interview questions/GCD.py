#How to find GCD(Greatest Common Devisor) of two numbers using recursion?
def gcd(a,b):
     assert int(a) == a and int (b) ==b,'The number must be integer only!' #for point values
     if a < 0:
        a = -1*a
     if b < 0:
        b = -1*b    
     if b ==0:
          return a 
     else:
          return gcd(b,a%b)       

gcd(a,b)