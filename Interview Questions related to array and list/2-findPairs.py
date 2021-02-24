#Write a program to find pairs that will be exacltly equal to asked target number.

def findPairs(num,target):
    for i in range(len(num)):
        for j in range(i+1,len(num)):
            if num[i] == num[j]:
                break
            elif num[i] + num[j] == target:
                print("By adding index value ",i,j,"," , "we can find a pair for target",target)
                
listnum = [1,2,4,5,3]
findPairs(listnum,7)

#Output:By adding index value  1 3 , we can find a pair for target 7
#       By adding index value  2 4 , we can find a pair for target 7
