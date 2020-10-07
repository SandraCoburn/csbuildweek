import time
start_time = time.time()
'''
Input: a List of integers as well as an integer `k` representing the size of the sliding window
Returns: a List of integers
'''
def sliding_window_max(nums, k):
    # Loop through the array to compare the k numbers and return the max
    #move to the next index and do it all over again
    #how do you get to reach the first k number of elements in the array
    #how do you move to the next three
    #how do you compare the k window values
    #save the max in a variable, save all max var in an array
    #replace the max with the next window's max
    #return the max
    #the end of the array should be defined by using the k value to minus the end of array len(arr[-k])
    allmax = []
    if len(nums) != 0:
        for index,num in enumerate(nums): #O(n)
            #have the window stop before array is over
            window = nums[index:index+k]
            # print("first window",window)
            # print(index, number)
            #compare the first k index and move k to next index
            window_max = max(window)

            #print("window max: ", window_max)
            allmax.append(window_max)
            
            #print("array: ", allmax)
            #Make the window sliding stop before end of array
            if len(nums) < index + (k + 1):
                return allmax
    return allmax

if __name__ == '__main__':
    # Use the main function here to test out your implementation 
    arr = [1, 3, -1, -3, 5, 3, 6, 7]
    arr2 = [70, 37, 100, 66, 1, 45, 27, 62, 75, 57, 92, 66, 9, 39, 15, 69, 46, 72, 35, 68, 54, 51, 35, 36, 13, 27, 27, 24, 6, 33, 83, 97, 55, 5, 25, 85, 56, 4, 100, 38, 38, 83, 29, 1, 11, 27, 64, 99, 64, 29, 41, 95, 59, 46, 75, 67, 40, 49, 62, 30, 56, 88, 71, 77, 43, 79, 27, 65, 24, 18, 74, 50, 23, 47, 45, 60, 62, 84, 53, 2, 90, 29, 99, 75, 59, 44, 71, 7, 59, 59, 27, 72, 6, 89, 90, 40, 51, 45, 43, 86]
    k = 5
#3,3,5,5,6,7
    end_time = time.time()
    
    print(f"Output of sliding_window_max function is: {sliding_window_max(arr, k)}")
    print (f"runtime: {end_time - start_time} seconds")