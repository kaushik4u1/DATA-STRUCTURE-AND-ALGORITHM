#How to Split Integer Into Digits in python.


numbers =12345678       
digits = []                         # Add (12345678%10 = 8) into digits

while numbers >0:
    digits.insert(0,numbers%10)
    numbers = (numbers-numbers%10)//10 # Set numbers equal to (12345678-12345678 % 10)/10 = 1234567
                                       # Repeat because numbers is greater that 0.
    
print(sum(digits))                     #Sum function can be used for summation of all digits.

#Output: 36
