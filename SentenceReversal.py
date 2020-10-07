'''
Given a string of words, reverse all the words. For example:
Given:
"this is the best"
return:
"best the is This"

You should remove all leading and trailing whitespace. 
'''

def rev_word(s):
    return " ".join(reversed(s.split()))

print(rev_word('   space before'))

def rev_word2(s):
    return " ".join(s.split()[::-1])

print(rev_word2('Hi John,   are you ready to go?'))

def rev_word3(s):
    words = []
    length = len(s)
    spaces = [" "]

    i =0

    while i < length:
        if s[i] not in spaces:
            word_start = i
            while i < length and s[i] not in spaces:
                i += 1
            words.append(s[word_start:i])
        i += 1
    return " ".join(reversed(words))
print(rev_word3('  Hello John   how are you  '))
