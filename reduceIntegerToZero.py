'''
Given a non-negative integer num, return the number of steps to reduce it to zero. 
If the current number is even, you have to divide it by 2, otherwise, you have to substract 1 from it.
examle:
input: num = 14
Output: 6
Explanation:
step 1) 14 is even; divide by 2 and obtain 7.
step 2) 7 is odd; substract 1 and obtain 6
step 3) 6 is even; divide by 2 and obtain 3
step 4) 2 is odd; substract 1 and obtain 2
step 5) 2 is even; divide by 2 and obtain 1
step 6) 1 is odd: substract 1 and obtain 0
'''

def reduceToZero(num):
    # copy numbers
    copyNum = num
    iterNum = 0 #number of iterations
    #loop while num > 0
    while copyNum > 0:
        # make variable for is Even
        isEven = copyNum % 2 == 0
        # if isEven is true, divide by 2
        if isEven:
            copyNum = copyNum / 2
        else:
            copyNum -= 1 #looping to go to zero
        iterNum += 1
    return iterNum
print(reduceToZero(14))
