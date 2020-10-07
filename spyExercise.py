def uncover_spy(n, trust):
    # Input:
    # n: 3
    # trust:
    # [[1,2], 
    #  [2,3]]
    # traverse throught the array and add them to two dictionaries, one the key will be the trust people and the value will be the is trusted person. The other dictionary will have the istrusted person as the key and value will be trust person
    ## Check if n is in any of the trust key
    ## Check if n is in any of the is trusted key
    ## if n is not in the trust keys - return n
    ## if n is in the trust key - return -1
    ## if one of the numbers is never the key in trust dictionary, return that number
    t = {}
    isTrusted = {}
    for k,v in enumerate(trust): #Get the values in the individual array of pairs
        a = v[0]
        b = v[1]
        t.setdefault(a, []).append(b) #{1:[2], 2:[3]} {1:[3], 2:[3]}
        
        isTrusted.setdefault(b, []).append(a) #{2:[1], 3:[2]} {3:[1], 3[2]}
        print("trust", t)
        print("isTrusted", isTrusted)

    possible_spies =[]


n = 3
trust = [[1, 3], [2, 3]]
tr = [[1,2],[2,3]]
trust2 = [[1, 3], [2, 3], [3, 1]]
uncover_spy(n, trust)