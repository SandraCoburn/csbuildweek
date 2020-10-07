'''
String Compression Problem
Given a string in the form "AAAABBBBCCCCCDDEEEE" compress it to become "A4B4C5D2E4"
For this problem, you can falsely "compress" strings of single or double letters. For instance,
it is okay for AAB to return A2B1 even though this technically takes more space.
The function shoudl also be case sensitive, so that a string "AAAaaa" returns "A3a3"
'''

def compress(s):
    #run lenght compress algorithm
    run = ""
    lenght = len(s)

    #check edge cases
    if lenght == 0:
        return ""
    if lenght == 1:
        return s + "1"
    last = s[0] #market in case it's needed
    count = 1
    index = 1

    while index < lenght:
        if s[index] == s[index -1]:
            count += 1
        else: 
            run = run + s[index - 1] + str(count) #Build the section of the run with the last previous element plust count
            count = 1 #reset the counter
        index += 1
    run = run + s[index -1] + str(count)

    return run

print(compress("AABCCCDDDDEE"))

