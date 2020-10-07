'''
Unique Characters in String Problem
Given a string, dtermine if it is compreised of all unique characters. 
For example, the string "abcde" has all unique characters and should return True.
The string "aabcde" contains duplicate characters and should return false
'''
def uni_char(s):
    return len(set(s)) == len(s)
print(uni_char("abcde"))


def uni_char2(s):
    chars = set()

    for let in s:
        if let in chars:
            return False
        else:
            chars.add(let)
    return True

print(uni_char2("abcdea"))