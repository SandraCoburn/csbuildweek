'''
    Given an encoded string, return its decoded string.

    The encoding rule is: k[encoded_string], where the encoded_string inside the square brackets is being repeated exactly k times. Note that k is guaranteed to be a positive integer.

    You may assume that the input string is always valid; No extra white spaces, square brackets are well-formed, etc.

    Furthermore, you may assume that the original data does not contain any digits and that digits are only for those repeat numbers, k. For example, there won't be input like 3a or 2[4].

    Example 1:

    Input: s = "3[a]2[bc]"
    Output: "aaabcbc"
    Example 2:

    Input: s = "3[a2[c]]"
    Output: "accaccacc"
'''
def decodeString(s):
    # create a stack
    new_str = []
    # k is the number letters will be multiplied by. Initialize it
    k = 0
    #variable to hold the decoded string
    curr = ""
    #loop through the string
    for l in s:
        print(l)
        if l == "[":
            new_str.append((curr, k))
            #reset variables
            curr, k = "", 0
        elif l == "]":
            #End of single array. Duplicate current from new_string stack
            last_letter, last_k = new_str.pop(-1)
            curr = last_letter + last_k * curr
        elif l.isnumeric():
            k = k * 10 + int(l)
        else: 
            curr += l
    return curr       

input1 = "3[a]2[bc]"
print(decodeString(input1))
