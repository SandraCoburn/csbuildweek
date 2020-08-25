'''
input: a man, a plan, a canal panama
result: amanap lanac a nalp a nam a
# "".join(reversed(list(s)))
'''
# sanitize comas and spaces
# create a copy of string, reverse it
# return only if it's equal to input
## s is a palindrome if:
    ## the first and last characters are the same
    ## and if the substring between the first and last character is palindrome

# one possible solution:
'''
s = re.sub(r'[\W]', '', s ).lower()
s2 = s[::-1] #reverse list
return s == s2
'''
#alternate solution:
"""
        s = "".join(c for c in s if c.isalnum()).lower()
        
        i0 = 0
        i1 = len(s) - 1 
        
        while i1 > i0:
            if s[i0] != s[i1]:
                return False
            
            i0 += 1
            i1 -= 1
            
        return True
        """
'''
     if s == "":
            return True
        
        i0 = 0
        i1 = len(s) - 1 
        
        while i1 > i0:
            if not s[i0].isalnum():
                i0 += 1
                continue
                
            if not s[i1].isalnum():
                i1 -= 1
                continue
                
            if s[i0].lower() != s[i1].lower():
                return False
            
            i0 += 1
            i1 -= 1
            
        return True
'''

import re

def isPalindrome(s):
    #s is len 0 or 1 (Base case)
    #s = "".join(c for c in s if c.isalnum()).lower
    if len(s) < 2:
        return True
    # the first and last characters are the same and if the substring between the fist and last chrac is a palindorme
    return s[0] == s[-1] and isPalindrome(s[1:-1])


string = "a man, a plan, a canal panama"
str2 = "kayak"
print(isPalindrome(str2))