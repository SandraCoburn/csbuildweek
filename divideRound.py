
def devideRound(lst):
    #Take it's mass, divide by three, round down and substract 2
    result = []
    for x in lst:
        x = x//3
        result.append(x-2)
    return sum(result)

    #return sum(y-2 for y in (x//3 for x in lst)) #one line result

print(devideRound([1969]))  #654


def devideRound2(lst):
    ##What is the sum of the fuel requirements for all of the modules on your spacecraft when also taking into account the mass of the added fuel? 
    ##Calculate the fuel requirements for each module separately, then add them all up at the end.
    #the fuel required by a module of mass 100756 and its fuel is: 
    def _fuel(x):
        return max(x//3 - 2, 0)

    def recursive_func(x, acc):
        if x <= 0:
            return 0
        #recursive call:
        fuel = _fuel(x)
        return fuel + recursive_func(fuel, fuel)

    fuel = 0
    for x in lst:
        fuel += recursive_func(x,0)
    return fuel
    #return sum(recursive_func(x,0) for x in lst) ##One line solution

print(devideRound2([100756]))