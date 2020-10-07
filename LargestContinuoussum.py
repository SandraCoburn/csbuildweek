'''
Largest Continuous Sum Problem
Given an array of integers (positive and negative) find the largest continous sum
'''

def large_cont_sum(arr):
    #if array is all positive we return the result as summ of all numbers
    #the negative numbers int he array will cause us to need to begin checkin sequences

    ## Check to see if array is Length 0
    if len(arr) == 0:
        return 0

    max_sum = current_sum = arr[0] #equal to first element

    for num in arr[1:]: #We check each number in array not including the first num arr[0]
        current_sum = max(current_sum+num, num) #find out which one is larger: current sum + num or the num

        max_sum = max(current_sum,max_sum) #we keep track of which one is larger
    return max_sum

print(large_cont_sum([1,2,-1,3,4,10,10,-10,-1]))