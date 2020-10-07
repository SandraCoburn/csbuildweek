'''
Consider an array of non-negative integers. A second array is formed by shuffling the
elements of the first array and deleting a random element.
given these two arrays, find which element is missing in the second array.
Here is an example input, the first array is shuffled and the number 5 is removed
to construc the second array
input:
finder([1,2,3,4,5,6,7],[3,7,2,1,4,6])
output:
5 is the missing number
'''
import collections
def finder(arr1,arr2):
    #sort the arrays
    arr1.sort()
    arr2.sort()
    for num1, num2 in zip(arr1,arr2):
        if num1 != num2:
            return num1

    return arr1[-1]
print(finder([5,5,7,7], [5,7,7]))

def finder2(arr1,arr2):
    #check if the key already exist, it doesn't give an error it just add it
    d = collections.defaultdict(int)

    for num in arr2:
        d[num] += 1
    for num in arr1:
        if d[num] == 0:
            return num
        else:
            d[num] -= 1

print(finder2([5,5,7,7],[5,7,7]))

def finder3(arr1,arr2):
    result=0

    #Perform an XOR (exclusive OR) between the numbers in the arrays ^
    #shows the outputs true whenever the inputs are the same(differ)
    for num in arr1+arr2: #it concatanate the two arrays
        result^=num
        print([result])
    return result

print(finder3([5,5,7,7],[5,7,7]))