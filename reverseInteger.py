'''
7. Reverse Integer - Easy
Given a 32-bit signed integer, reverse digits of an integer.

Example 1:

Input: 123
Output: 321
Example 2:

Input: -123
Output: -321
Example 3:

Input: 120
Output: 21
Note:
Assume we are dealing with an environment which could only store integers within the 32-bit signed integer range: [−231,  231 − 1]. For the purpose of this problem, assume that your function returns 0 when the reversed integer overflows.
'''
'''
  rev_num = 0
    n = x
    if x < 0:
        n *= -1
    check using while loop
    while(x>0):
        #build up the reverse integer one digit at a time
        reminder = x % 10 #123456%10 = 6, 12345 % 10 = 5
        rev_num = (rev_num * 10) + reminder #0 * 10 + 6 = 0 + 6 = 6, 60 + 5 = 65
        x = x // 10 #123456 //10 = 12345, 12345 //10 = 1234
        print(x)
    if x<0:
        return "-" + str(rev_num)
    return rev_num
'''

def reverse(x):  
    #initiate value to zero
    neg = x < 0
    if neg:
        rev = int('-' + str(-x)[::-1])
    else:
        rev = int(str(x)[::-1])
    if rev > 2**31 or rev < -2**31 -1:
        return 0
    return rev
  

n = 123456
n2 = -123
print(reverse(n2))