'''
Anagram Check Problem
Given two strings, check to see if they are anagrams. An anagrm is when the two string can be written using the exact same letters(so youcan just rearrange the letters to get a different phrase or word)
For example:
"public relations" is an anagram of "crap built on lies"
"clint eastwood" is an anagram of "old west action"
'''
def anagram(s1, s2):
    #Clean up the strings
    s1 = s1.replace(' ', ' ').lower()
    s2 =s2.replace(' ', ' ').lower()

    #edge case check
    if len(s1) != len(s2):
        return False
    count = {}
    for letter in s1:
        if letter in count:
            count[letter] += 1
        else: 
            count[letter] =1
    for letter in s2:
        if letter in count:
            count[letter] -= 1
        else:
            count[letter] = 1
    for k in count: 
        if count[k] != 0:
            return False
    return True

print(anagram('dog', 'god'))
print(anagram('clint eastwood', "old west action"))