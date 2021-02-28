#How to Split Integer Into Digits in python.


numbers =12345678       
digits = []                            # Add (12345678%10 = 8) into digits

while numbers >0:
    digits.insert(0,numbers%10)
    numbers = (numbers-numbers%10)//10 # Set numbers equal to (12345678-12345678 % 10)/10 = 1234567
                                       # Repeat because numbers is greater that 0.
    
print(digits)


#Output: [1, 2, 3, 4, 5, 6, 7, 8]
