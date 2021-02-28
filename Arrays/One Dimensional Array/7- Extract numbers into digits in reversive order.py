#How to Split Integer Into Digits in reversive order.


numbers =12345678       
digits = []                         # Add (12345678%10 = 8) into digits

while numbers >0:
    digits.append(numbers%10)          # we can use append for reversive order.
    numbers = (numbers-numbers%10)//10 # Set numbers equal to (12345678-12345678 % 10)/10 = 1234567
                                       # Repeat because numbers is greater that 0.
    
print(digits)



#Output: [8, 7, 6, 5, 4, 3 ,2, 1]
