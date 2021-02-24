#Given 2D list calculate the sum of diognal elements.

mylist = [[1,2,3],[4,5,6],[7,8,9]]

def sumDiagonal(a):
    summ = 0
    for i in range(len(a[0])): #--------------for right diognal
        for j in range(len(a)):
            if i == j:
                summ += a[i][j]
    return summ
    
print(sumDiagonal(mylist))  

#Output: 15
             
      