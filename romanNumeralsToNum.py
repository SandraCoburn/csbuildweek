'''
There are 7 letter(symbols) that are used to represent Roman numerals:
I, V, X, L, C, D and M
Their values are:
I=1
V=5
X=10
L=50
C=100
D=500
M=1000
For example, two is written as II in Roman numeral, just two one's added togethrer.
Thirteen is written as XIII , The number seventeen is written as XVII
Roman numerals are usually written largest to smalles from left to right.
However, the numerals for four is not III bu IV.
Because the one is before the five we subtract it making four.
The same principle applies to the number nine, which is witten as IX.
There are six instances where subtraction is used:
I can be placed before V (5) and X (10) to make 4 and 9.
X can be placed before L (50) and C (100) to make 40 and 90
C can be placed before D (500) and 
'''

# If current > previous:
    ## current substract previous

def romanTonum(str):
    #initializa all romans str and our number
    romans = {"I":1, "V":5, "X":10, "L":50, "C":100, "D":500, "M":1000}
    num = 0
    #combine string to a list
    theList = list(str)
    ## iterate over list to get each character
    for index, i in enumerate(theList):
    ## evaluate the numerals, add a value of roman numeral into number
        num = num + romans[i]
    ## if it's grater than zero, we gonna check if is greater than previous
        if index > 0:
            continue


        ## current decreased by previous. Value add to increment number
    ## return number
    return num
print(romanTonum("X"))
